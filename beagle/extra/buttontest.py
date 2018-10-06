import rcpy
import rcpy.button as button
import rcpy.gpio as gpio
from rcpy.button import mode, pause

if mode.pressed():
	print('<MODE> pressed!')

if mode.released():
	print('<MODE> released!')

pause_button = gpio.Input(gpio.PAUSE_BTN)

if pause_button.low():
	print('Got <PAUSE>!')

