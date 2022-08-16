from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
import serial
from serial.tools.list_ports import comports
from SignalGenerator import Ui_MainWindow, SinFunction, Generator, SerialPort


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init()
        self.inited = False
        self.pausable = False

        self.ui.sg_btn_RefreshCOM.clicked.connect(self.init_sg_com_list)
        self.ui.sg_btn_Start.clicked.connect(self.start)
        self.ui.sg_btn_Stop.clicked.connect(self.stop)

    # 控制按钮的逻辑，包括开始、暂停、停止的功能
    def start(self):
        if self.pausable == True:
            self.generator.pause()
            self.ui.sg_btn_Start.setText("继续")
            self.pausable = False
            return
        if not self.inited:
            self.init_port()
        self.generator.resume()
        self.ui.sg_btn_Start.setText("暂停")
        self.pausable = True

    def stop(self):
        self.generator.stop()
        self.generator.resume()  # 需要确保信号产生的线程已退出
        self.ui.sg_btn_Start.setText("开始")
        self.pausable = False
        self.inited = False

    # 根据图形界面信息初始化COM 口
    def init_port(self):
        self.inited = True
        self.port = SerialPort(self.ui.sg_slt_COMList.currentData(),
                               int(self.ui.sg_txt_Baudrate.text()),
                               int(self.ui.sg_slt_Databit.currentData()),
                               self.ui.sg_slt_Paritybit.currentData(),
                               float(self.ui.sg_slt_Stopbit.currentData()),
                               )
        self.generator = Generator(float(self.ui.txt_signal_Freq.text()), SinFunction(
            float(self.ui.txt_signal_A.text()),
            float(self.ui.txt_signal_Omega.text()),
            float(self.ui.txt_signal_Phi.text())), self.port)
        self.generator.turn_on()

    # 图形界面的初始化工作
    def init(self):
        self.init_sg_com_list()
        self.init_sg_data_bit()
        self.init_sg_stop_bit()
        self.init_sg_parity_bit()

    def init_sg_com_list(self):
        self.ui.sg_slt_COMList.clear()
        for com in comports():
            self.ui.sg_slt_COMList.addItem(com.name, com.name)

    def init_sg_data_bit(self):
        self.ui.sg_slt_Databit.clear()
        for i in range(8, 4, -1):
            self.ui.sg_slt_Databit.addItem(str(i), i)

    def init_sg_stop_bit(self):
        self.ui.sg_slt_Stopbit.clear()
        for i in [1, 1.5, 2]:
            self.ui.sg_slt_Stopbit.addItem(str(i), i)

    def init_sg_parity_bit(self):
        self.ui.sg_slt_Paritybit.clear()
        for name in serial.PARITY_NAMES:
            self.ui.sg_slt_Paritybit.addItem(
                serial.PARITY_NAMES[name], serial.PARITY_NAMES[name][0])

    def init_sg_signal_dt(self):
        """发送间隔时间
        - 目前是按Python 最小sleep 周期发送的
        """


if __name__ == "__main__":
    app = QApplication()

    win = MainWindow()
    win.show()
    exit(app.exec_())
