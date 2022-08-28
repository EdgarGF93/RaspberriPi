from humidity import HumiditySensor
from lcd_module import LCD162
import time

pin_rs = 21
pin_en = 20
pins_d = [26,19,13,6]

pin_hsensor = 16

h = HumiditySensor(pin_hsensor)
lcd162 = LCD162(pin_rs, pin_en, pins_d)


while True:
	state_hum = h.state_hum()
	lcd162.message(state_hum)
	time.sleep(1)
