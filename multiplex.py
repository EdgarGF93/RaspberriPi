import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dict_gates = {0:[0,0,0,0], 1:[1,0,0,0], 2:[0,1,0,0], 3:[1,1,0,0], 4:[0,0,1,0],
              5:[1,0,1,0], 6:[0,1,1,0], 7:[1,1,1,0], 8:[0,0,0,1], 9:[1,0,0,1],
              10:[0,1,0,1], 11:[1,1,0,1], 12:[0,0,1,1], 13:[1,0,1,1], 14:[0,1,1,1], 15:[1,1,1,1],
              }

class Multiplexer:
	def __init__(self, pins_gates, pin_signal):
		self.pins_gates = pins_gates
		self.pin_signal = pin_signal
		self.setup_gpio(pins_gates)
		self.setup_gpio(pin_signal)

	def setup_gpio(self, pins):
		if isinstance(pins, int):
			GPIO.setup(pins, GPIO.OUT)
			return
		if isinstance(pins, list):
			for pin in pins:
				GPIO.setup(pin, GPIO.OUT)
			return

	def on_sig(self):
		self.on(self.pin_signal)

	def off_sig(self):
		self.off(self.pin_signal)

	def on_ch(self, channel):
		# from dict_gates import dict_gates
		list_gates = dict_gates[channel]
		for ind,gate in enumerate(list_gates):
			if gate == 1:
				self.on(self.pins_gates[ind])
			elif gate == 0:
				self.off(self.pins_gates[ind])

	def on(self, pin):
		GPIO.output(pin, 1)
		return

	def off(self, pin):
		GPIO.output(pin, 0)
		return

	def clean(self):
		GPIO.cleanup()
