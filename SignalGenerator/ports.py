import datetime
from datetime import datetime
from time import sleep
from SignalGenerator.base import IPort
from serial import Serial


class DefaultPort(IPort):
    """
    DefaultPort 默认端口： 
    至少间隔0.5s 可以向控制台发送数据，用于程序逻辑的验证
    """

    def __init__(self) -> None:
        super().__init__()

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
        if(self._is_on):
            print("[%s] Port send: %s" % (datetime.now(), data))
        else:
            raise IOError("端口打开异常！")


class SerialPort(Serial, IPort):
    def __init__(self, *args, **kwargs):
        super(IPort, self).__init__()
        super().__init__(*args, **kwargs)

    def turn_on(self):
        if(not self.isOpen()):
            self.open()

    def turn_off(self):
        if(self.isOpen()):
            self.close()
            return super().turn_off()

    def wait_port_available(self):

        while not self.writable():
            sleep(0.001)
            break

    def send_data(self, data: any):
        if(self.isOpen()):
            self.write(str.encode("%s\n\r" % data[0]))
            sleep(0.1)  # 防止发送速度过快，人眼看不清
        else:
            raise IOError("端口打开异常！")
