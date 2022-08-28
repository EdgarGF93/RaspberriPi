
import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setmode(GPIO.BCM)
dict_numbers = {0:[1,2,4,6,7,8], 1:[8,4], 2:[6,8,5,1,2],
		3:[6,8,5,4,2], 4:[7,5,8,4], 5:[6,7,5,4,2],
		6:[7,1,2,4,5], 7:[6,8,4],
		8:[1,2,4,5,6,7,8], 9:[7,6,8,5,4], 'dot':[3],
		}

dict_letters = {'O':[1,2,4,6,7,8], 'L':[7,1,2], 'G':[6,7,1,2,4,5], 'A':[1,7,6,8,4,5], 'E':[6,7,5,1,2],
		'D':[1,7,6,8,4,2], 


}

#list_outputs = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [1,1,1,0]]
dict_outputs = {3:[0,1,1,1], 2:[1,0,1,1], 1:[1,1,0,1], 0:[1,1,1,0]}
dict_dig = {3:1, 2:2, 1:3, 0:4}


class display4d():
	def __init__(self, pins_digs, pins_segments):
#		self.dict_pins_digs = self.get_dict(pins_digs)
		self.list_pins_segs = pins_segments
		self.dict_pins_seg = self.get_dict(pins_segments)
		self.list_pins_digs = pins_digs
		self.setup(pins_digs)
		self.setup(pins_segments)


	def write(self, word):
		if len(word) == 4:
			self.write_4(word)

	def write_4(self, word):
		while True:
			for ind,x in enumerate(reversed(range(4))):
				let = word[ind]
				# Digit
				self.on_digit(dict_outputs[x])
				# Letter
				self.on_let(let)
				time.sleep(0.001)



	def hour(self):
		while True:
			now = datetime.now()
			h = now.hour
			m = now.minute
			num = h * 100 + m
			self.on_number(num, digit_dot=2)

	def setup(self, pins):
		GPIO.setup(pins, GPIO.OUT)
		return

	def get_dict(self, list_pins):
		dict_pins = {}
		for ind,pin in enumerate(list_pins):
			dict_pins[ind+1] = pin
		return dict_pins

	def dot(self):
		pin = self.dict_pins_seg[3]
		self.on(pin)

	def on_number(self, number, wait=0, digit_dot=False):
		digits = len(str(number))
		st = time.perf_counter()
		end_time = time.perf_counter() - st
		if wait == 0:
			end_time = -1
		while end_time < wait:
			for ind,digit in enumerate(reversed(range(digits))):
				num = int(str(number)[ind])

				# Activate one digit at once
				list_outputs = dict_outputs[digit]
				self.on_digit(list_outputs)

				# Activate the segments
				self.on_unit(num)

				# Dot
				if dict_dig[digit] == digit_dot:
					self.dot()
				time.sleep(0.001)
				end_time = time.perf_counter() -st

	def on_digit(self, list_outputs):
		GPIO.output(self.list_pins_digs, list_outputs)


	def on_let(self, let, wait=0):
		self.clear_segs()
		list_segs = dict_letters[let]
		for seg in list_segs:
			pin_seg = self.dict_pins_seg[seg]
			self.on(pin_seg, wait=wait)

	def on_unit(self, number, wait=0):
		self.clear_segs()
		list_segs = dict_numbers[number]
		for seg in list_segs:
			pin_seg = self.dict_pins_seg[seg]
			self.on(pin_seg, wait=wait)

	def flush_number(self):
		for seg in range(8):
			pin = self.dict_pins_seg[seg+1]
			self.off(pin)

	def on_segment(self, seg):
		pin_seg = self.dict_pins_seg[seg]
		self.on(pin_seg)

	def on(self, pin, wait=0):
		GPIO.output(pin, 1)
		if wait > 0:
			time.sleep(wait)
			GPIO.output(pin, 0)
		elif wait == 0:
			return

	def off(self, pin):
		GPIO.output(pin, 0)

	def clear_segs(self):
		for pin in self.list_pins_segs:
			GPIO.output(pin, 0)


	def reset(self):
		GPIO.cleanup()

