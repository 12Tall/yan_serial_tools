

from time import sleep
from SignalGenerator import Generator, SinFunction, SerialPort


bg = Generator(1, [SinFunction()], [SerialPort("COM6", 9600,)])
bg.turn_on()  # 开启
bg.resume()   # 开始输出
sleep(3)

bg.pause()    # 暂停
sleep(3)

bg.resume()   # 继续输出
sleep(5)

bg.reset()    # 中间重置状态
sleep(2.5)

bg.stop()     # 停止
sleep(3)
