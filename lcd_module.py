from time import sleep
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono
from datetime import datetime

# Number of the pins MUST be the GPIO numbers, not the pin numbers
class LCD162():
	def __init__(self, pin_rs, pin_en, pins_d, lcd_columns=16, lcd_rows=2):
		self.lcd_rs = eval(f'DigitalInOut(board.D{pin_rs})')
		self.lcd_en = eval(f'DigitalInOut(board.D{pin_en})')
		self.lcd_d4 = eval(f'DigitalInOut(board.D{pins_d[0]})')
		self.lcd_d5 = eval(f'DigitalInOut(board.D{pins_d[1]})')
		self.lcd_d6 = eval(f'DigitalInOut(board.D{pins_d[2]})')
		self.lcd_d7 = eval(f'DigitalInOut(board.D{pins_d[3]})')
		self.lcd_columns = lcd_columns
		self.lcd_rows = lcd_rows
		self.lcd = Character_LCD_Mono(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5,
				self.lcd_d6, self.lcd_d7, lcd_columns, lcd_rows)

	def message(self, msg='Hello World!'):
		self.lcd.message = msg
		return

	def show_datetime(self):
		dict_week = {0:'Monday',1:'Tuesday',2:'Wednesday',
		3:'Thursday', 4:'Friday',5:'Saturday',6:'Sunday'}
		while True:
			now = datetime.now()
			day_week = dict_week[datetime.today().weekday()]
			upper_line = f'{now.hour}:{now.minute}:{now.second}'
			bottom_line = f'{now.day}-{now.month}-{now.year} {day_week}'
			msg = f'{upper_line}\n{bottom_line}'
			self.message(msg)
			sleep(1)
