import abc
from threading import Event, Thread


class IPort(abc.ABC):
    """
    IPort 信号发生器的输出接口    
    内置了一个状态标志self._is_on = False
    """

    def __init__(self) -> None:
        super().__init__()
        self._is_on = False

    @abc.abstractmethod
    def turn_on(self):
        """
        打开端口，而且只能打开一次。
        最后需要修改self._is_on = True
        """

    @abc.abstractmethod
    def turn_off(self):
        """
        关闭端口。
        需要修改self._is_on = False 
        """

    @abc.abstractmethod
    def wait_port_available(self):  # 等待端口可用
        """
        等待端口可用
        """

    @abc.abstractmethod
    def send_data(self, data: any):  # 等待端口可用
        """
        向端口写入数据
        """

    def send(self, data: any):
        if self._is_on:
            self.wait_port_available()
            self.send_data(data)
        else:
            raise IOError("端口未打开或不可用")


class IGenerator(abc.ABC):
    """
    IGenerator 抽象类，包含最基本的发送数据的接口函数。
    而在send 方法中应首先生成数据  
    """

    @abc.abstractmethod
    def __init__(self):
        """
        初始化信号发生器
        """

    @abc.abstractmethod
    def send_data(self):
        """
        核心函数：用于生成并发送数据
        """


class Engine(Thread):
    """
    Engine 相当于信号发生器的CPU  
    比较绕的逻辑是：  
      Engine 每一步都会调用信号发生器生成数据，但逻辑上信号发生器是包含Engine 的
      于是便形成了循环引用的代码结构              
    """

    def __init__(self, generator: IGenerator):
        """
        初始化：
        1. 设置为守护线程，跟随主线程退出  
        2. 指定函数发生器实例对象  
        3. self.pause_flag = Event() 默认为False，会造成self.pause_flag.wait 方法阻塞  
        4. self.stop_flag = Event() 默认为False，会造成self.stop_flag.wait 方法阻塞

        """
        Thread.__init__(self)
        self.daemon = True  # 设置为守护线程，当主线程退出时自动结束
        self.generator = generator
        self.pause_flag = Event()
        self.stop_flag = Event()

    def resume(self):
        """
        设置暂停标志为True，使代码继续运行
        """
        self.pause_flag.set()

    def pause(self):
        """
        设置暂停标志为False，使代码继续阻塞
        """
        self.pause_flag.clear()

    def stop(self):
        """
        设置停止标志为True，结束线程
        """
        self.stop_flag.set()

    def run(self):
        while True:
            self.pause_flag.wait()  # 暂停线程
            if self.stop_flag.is_set():
                break  # 退出线程
            self.generator.send_data()  # 生成并发送数据


class Generator(IGenerator):
    """
    Generator 信号发生器基类，内置了：
    1. 一个计数器self.counter = 0. 用于生成输出信号的函数中  
    2. 一个状态标志self._is_on = False 
    3. 一个CPU self.engine = Engine(self) 用于循环生成并发送数据
    """

    def __init__(self, port: IPort, deltaT=0.001) -> None:
        """
        deltaT: 采样周期，单位是s
        """
        super().__init__()
        self.port = port
        self._is_on = False
        self.counter = 0.
        self.deltaT = deltaT
        self.engine = Engine(self)

    @abc.abstractmethod
    def generate_data(self):
        """
        数据生成，可以使用信号发生器对象中的所有属性
        """

    @abc.abstractmethod
    def reset(self):
        """
        重置信号发生器  
        """

    @abc.abstractmethod
    def send_data(self):
        """
        发送数据，记得在send 函数开始先调用self.generate_data()  
        """

    def turn_on(self):
        """
        信号发生器启动，但并不开始运行
        """
        if not self._is_on:
            self.engine.start()  # 开启线程，此方法只能执行一次
            self._is_on = True
        else:
            raise RuntimeError("信号发生器不能重复打开")

    def resume(self):
        """
        信号发生器开始（继续）运行
        """
        self.engine.resume()

    def pasue(self):
        """
        信号发生器暂停运行
        """
        self.engine.pause()

    def stop(self):
        """
        信号发生器停止运行，此操作会更换engine 线程，但是没啥影响
        """
        self.engine.stop()
        self.port.turn_off()
        self.engine = Engine(self)  # 为开始新一轮任务做准备
        self._is_on = False
