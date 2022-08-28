import RPi.GPIO as GPIO
import time, os
from datetime import datetime
GPIO.setmode(GPIO.BCM)

class HumiditySensor():
	def __init__(self, pin_input):
		self.pin_input = pin_input
		self.setup_input(pin_input)

	def setup_input(self, pins):
		GPIO.setup(pins, GPIO.IN)

	def print_hum(self, interval=1):
		while True:
			state = self.state_hum()
			print(state)
			time.sleep(interval)

	def state_hum(self) -> str:
		bit = GPIO.input(self.pin_input)
		if bit == 1:
			state = 'Dry'
		elif bit == 0:
			state = 'Wet'
		return state

	def get_hum_header(self):
		str_header = f'{"*"*100}\n\nState of humidity: Dry/Wet\n\n{"*"*100}\n'
		str_header += f'Datetime \t Humidity state\n'
		return str_header

	def save_hum(self, main_dir, name='', interval=1):
		if name == '':
			name += 'log_humidity'
		name = os.path.splitext(name)[0]
		name += f'{self.get_datetime()}.txt'
		full_txt_output = os.path.join(main_dir, name)
		# Start the list
		list_datetimes, list_states = [], []
		with open(full_txt_output, 'a') as f:
			f.write(self.get_hum_header())
			while True:
				state = self.state_hum()
				date_state = self.get_datetime()
				f.write(f'{str(date_state)} \t {str(state)}')
				f.write('\n')
				time.sleep(interval)


	def get_datetime(self):
		now = datetime.now()
		date_str = f'{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}'
		return date_str
