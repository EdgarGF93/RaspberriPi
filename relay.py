import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class Relay():
	def __init__(self, pins_in):
		self.pins_in = pins_in
		self.setup(pins_in)
		self.dict_pins = {}
		self.get_dict_pins(pins_in)


	def get_dict_pins(self, pins):
		if isinstance(pins, int):
			self.dict_pins[1] = pins
		if isinstance(pins, list):
			for ind,pin in enumerate(pins):
				self.dict_pins[ind+1] = pin

	def setup(self, pins):
		if isinstance(pins, int):
			GPIO.setup(pins, GPIO.OUT)
			return
		if isinstance(pins, list):
			for pin in pins:
				GPIO.setup(pin, GPIO.OUT)
			return


	def on_relay(self, relay_n, time=1, off=True):
		pin = self.dict_pins[relay_n]
		self.off(pin)
		sleep(time)
		self.on(pin)

	def off_relay(self, relay_n, time=1):
		pin = self.dict_pins[relay_n]
		self.on(pin)
		sleep(time)

	def on(self, pin):
		GPIO.output(pin, 1)
		return

	def off(self, pin):
		GPIO.output(pin, 0)
		return

	def reset(self):
		GPIO.cleanup()
