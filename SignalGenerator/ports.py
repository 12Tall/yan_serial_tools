import datetime
from datetime import datetime
from time import sleep
from SignalGenerator.base import IPort


class DefaultPort(IPort):
    """
    DefaultPort 默认端口： 
    至少间隔0.5s 可以向控制台发送数据，用于程序逻辑的验证
    """

    def __init__(self) -> None:
        super().__init__()
        self._is_on = False

    def turn_on(self):
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        self._is_on = False

    def wait_port_available(self):
        while True:
            sleep(0.5)
            break

    def send_data(self, data: any):
        print("[%s] Port send: %s" % (datetime.now(), data))
