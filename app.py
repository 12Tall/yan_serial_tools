
from time import sleep
from SignalGenerator import DefaultGenerator, DefaultPort


dg = DefaultGenerator(DefaultPort())

dg.turn_on()
# dg.turn_on()
dg.resume()

sleep(3)
dg.pasue()
sleep(3)
dg.resume()
sleep(3)