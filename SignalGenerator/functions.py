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
