from math import sin
from SignalGenerator.base import IFunction


class DefaultFunction(IFunction):
    """
    默认信号产生函数，返回值是时间本身
    """

    def call(self):
        self.value = self.timer
        self.timer += self.deltaT
        return self.value

    def reset(self):
        self.timer = 0.
        self.value = 0.


class DIntTFunction(IFunction):
    """
    离散时间的积分信号
    """

    def call(self):
        self.value += self.timer * self.deltaT
        self.timer += self.deltaT
        return self.value

    def reset(self):
        self.timer = 0.
        self.value = 0.


class CIntTFunction(IFunction):
    """
    连续时间的积分信号
    """

    def call(self):
        self.value = self.timer*self.timer*0.5
        self.timer += self.deltaT
        return self.value

    def reset(self):
        self.timer = 0.
        self.value = 0.


class SinFunction(IFunction):
    """
    连续时间的积分信号
    """

    def __init__(self, A=1., omega=1., phi=0., deltaT=0.001):
        super().__init__(deltaT)
        self.A = A
        self.omega = omega
        self.phi = phi

    def call(self):
        self.value = self.A*sin(self.omega*self.timer+self.phi)
        self.timer += self.deltaT
        print(self.value)
        return self.value

    def reset(self):
        self.timer = 0.
        self.value = 0.
