import abc
from threading import Event, Thread
from typing import List, Union

from matplotlib.pyplot import cla


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
        if not self._is_on:
            self._is_on = True

    @abc.abstractmethod
    def turn_off(self):
        """
        关闭端口。
        需要修改self._is_on = False 
        """
        self._is_on = False

    @abc.abstractmethod
    def wait_port_available(self):  # 等待端口可用
        """
        等待端口可用
        """

    @abc.abstractmethod
    def send_data(self, data: List[float]):
        """
        向端口写入数据
        可以自定义写入数据的格式
        """

    def send(self, data: List[float]):
        """
        等待端口可用后写入数据
        """
        if self._is_on:
            self.wait_port_available()
            self.send_data(data)
        else:
            raise IOError("端口未打开或不可用")


class IFunction(abc.ABC):
    """
    信号产生函数，包含以下属性：  
    - timer: 计数器  
    - value: 输出结果的缓存  
    - deltaT: 0.001s 函数产生的步长，在Generator 中自动设定
    """

    def __init__(self, deltaT=0.001):
        self.timer = 0.
        self.value = 0.
        self.setDeltaT(deltaT)

    def setDeltaT(self, deltaT=0.001):
        self.deltaT = deltaT

    @abc.abstractmethod
    def call(self):
        """
        进行一步计算，返回信号值
        """

    @abc.abstractmethod
    def reset(self):
        """
        重置函数：计数器、当前值等
        """


class Generator(Thread):
    """
    Generator 信号发生器类:
    本质上是一个线程，其中包含一个run() 函数，用于不间断地产生信号。此线程为守护线程，会在主线程退出后自动结束。 
    """

    def __init__(self, deltaT: float, funcs: Union[IFunction, List[IFunction]], ports: Union[IPort, List[IPort]]):
        """ 
        参数说明：  
        - deltaT: 产生信号的步长，非负数；  
        - funcs: 用于产生信号的函数规则集合；  
        - ports: 用于发送信号的（物理）端口，数据会以list 的形式传递给port 端口。  


        私有属性：  
        - self.pause_flag = Event() 默认为False，会造成self.pause_flag.wait 方法阻塞  
        - self.stop_flag = Event() 默认为False，会造成self.stop_flag.wait 方法阻塞
        """
        Thread.__init__(self)
        self.daemon = True  # 设置为守护线程，当主线程退出时自动结束
        self.deltaT = deltaT if deltaT > 0. else 0.001
        self.funcs = funcs if isinstance(funcs, list) else [funcs]
        self.ports = ports if isinstance(ports, list) else [ports]

        # 私有属性
        self.pause_flag = Event()
        self.stop_flag = Event()

        self.setDeltaT()

    def setDeltaT(self):
        """
        更改信号产生的步长
        """
        for func in self.funcs:
            func.setDeltaT(self.deltaT)

    def turn_on(self):
        for port in self.ports:
            port.turn_on()
        self.start()

    def resume(self):
        """
        继续执行
        """
        self.pause_flag.set()

    def pause(self):
        """
        暂停执行
        """
        self.pause_flag.clear()

    def reset(self):
        """
        重置所有的函数  
        在信号发生器运行时执行此函数可能造成意料之外的后果
        """
        for func in self.funcs:
            func.reset()

    def stop(self):
        """
        停止执行并退出
        """
        self.stop_flag.set()
        for port in self.ports:
            port.turn_off()

    def run(self):
        while True:
            self.pause_flag.wait()  # 暂停线程
            if self.stop_flag.is_set():
                break  # 退出线程
            data = [func.call() for func in self.funcs]
            for port in self.ports:
                port.send(data)
