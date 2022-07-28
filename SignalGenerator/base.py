from datetime import datetime
from threading import Event, Thread
from time import sleep


class IPort(object):
    """
    IPort 输出接口
    需要重写接口函数
    """

    def __init__(self) -> None:
        self._is_on = False
        pass

    def turn_on(self):
        # 模拟端口打开，需要避免重复打开
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        # 端口关闭
        self._is_on = False

    def wait_writable(self):  # 等待端口可用
        while True:
            sleep(0.5)
            break

    def write(self, data: any):
        print("[%s] Port send: %s" % (datetime.now(), data))

    ##################################################
    # send 方法可以不用重写
    ##################################################
    def send(self, data: any):
        # 模拟端口发送数据的过程
        if self._is_on:  # 模拟检查端口状态，如果端口已关闭就不再发送
            self.wait_writable()
            self.write(data)


class IGenerator(object):
    """
    IGenerator 只包含信号产生与发送的关键方法
    """

    def __init__(self, port: IPort = IPort()) -> None:
        self.port = port  # 定义输出端口
        pass

    def reset(self):
        pass

    def generate_data(self):
        pass

    def send(self):
        self.port.send()


class Executor(Thread):
    """
    信号发生器独立线程，主要包含以下方法用于线程的控制：  
    0. start   线程的默认方法，只能被调用一次
    1. resume  开始输出，因为start 方法已经被占用，这里只好用resume    
    2. pause   暂停输出  
    3. stop    停止输出
    """

    def __init__(self, generator: IGenerator):
        Thread.__init__(self)
        self.daemon = True  # 设置为守护线程，当主线程退出时自动结束
        self.generator = generator
        self.pause_flag = Event()
        self.stop_flag = Event()

    def resume(self):
        self.pause_flag.set()

    def pause(self):
        self.pause_flag.clear()

    def stop(self):
        self.stop_flag.set()

    def run(self):
        while True:
            self.pause_flag.wait()
            if self.stop_flag.is_set():
                break
            self.generator.send()


class BaseGenerator(IGenerator):
    """
    信号发生器基类，其子类需要重写：  
    1. reset 方法  
    2. generate_data 方法
    3. send 方法，需要在send 方法中调用self.port.send 向实际接口发送数据

    可直接调用的方法：  
    1. turn_on 开启但无输出，此方法只能执行一次  
    2. resume  开始输出  
    3. pause   暂停输出  
    4. stop    停止输出
    """

    def __init__(self, deltaT=0.001, port: IPort = IPort()) -> None:
        """
        deltaT: 采样周期，单位是s
        """
        super().__init__()
        self.port = port
        self._is_on = False
        self.counter = 0.
        self.deltaT = deltaT
        self.exe = Executor(self)

    def generate_data(self):
        self.counter += self.deltaT

    def reset(self):
        self.counter = 0.

    def send(self):
        self.port.turn_on()   # 保证端口已经打开
        self.generate_data()  # 生成信号
        self.port.send(self.counter)  # 模拟发送数据

    ###########################################################
    # 将Executor 嵌套进信号发生器，将会使我们的代码更整洁
    # 而且只需要在基类中定义一次以下方法就好了
    ###########################################################

    def turn_on(self):
        if not self._is_on:
            self.exe.start()  # 开启线程，此方法只能执行一次
            self._is_on = True

    def resume(self):
        self.exe.resume()

    def pasue(self):
        self.exe.pause()

    def stop(self):
        self.exe.stop()
        self.port.turn_off()
        self.exe = Executor(self)  # 为开始新一轮任务做准备
        self._is_on = False
