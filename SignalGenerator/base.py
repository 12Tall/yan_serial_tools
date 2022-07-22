from datetime import datetime
from threading import Event, Thread
from time import sleep

class IGenerator(object):
    """
    IGenerator 只包含信号产生与发送的关键方法
    """
    def __init__(self) -> None:
        pass

    def reset(self):
        pass

    def generate_data(self):
        pass

    def send(self):
        print("job is running")
        sleep(0.2)


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
            self.generator.generate_data()
            self.generator.send()


class BaseGenerator(IGenerator):
    """
    信号发生器基类，其子类需要重写：  
    1. reset 方法  
    2. generate_data 方法
    3. send 方法
    
    可直接调用的方法：  
    1. turn_on 开启但无输出，此方法只能执行一次  
    2. resume  开始输出  
    3. pause   暂停输出  
    4. stop    停止输出
    """
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0
        self.exe = Executor(self)

    def generate_data(self):
        self.counter += 1

    def reset(self):
        self.counter = 0

    def send(self):
        print("[%s] send data: %s"%(datetime.now(),self.counter))
        sleep(0.5)
    

    ###########################################################    
    # 将Executor 嵌套进信号发生器，将会使我们的代码更整洁  
    # 而且只需要在基类中定义一次以下方法就好了
    ###########################################################
    def turn_on(self):  
        self.exe.start()  # 开启线程，此方法只能执行一次  
    
    def resume(self):  
        self.exe.resume() 
    
    def pasue(self):
        self.exe.pause()
    
    def stop(self):  
        self.exe.stop()
        self.exe = Executor(self)  # 为开始新一轮任务做准备