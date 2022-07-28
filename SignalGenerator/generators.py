from SignalGenerator.base import Generator, IPort


class DefaultGenerator(Generator):
    def __init__(self, port: IPort, deltaT=0.001) -> None:
        super().__init__(port, deltaT)

    def generate_data(self):
        self.counter += self.deltaT

    def reset(self):
        self.counter = 0.

    def send_data(self):
        self.port.turn_on()   # 保证端口已经打开
        self.generate_data()  # 生成信号
        self.port.send(self.counter)  # 模拟发送数据
