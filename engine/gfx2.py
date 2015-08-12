import libtcodpy as ld
import traceback
import sys
import locale

_SCREEN_WIDTH  = 80
_SCREEN_HEIGHT = 40

while not ld.console_is_window_closed():
	ld.console_set_default_foreground(0, ld.white)
	ld.console_put_char(0, 1, 1, '@', ld.BKGND_NONE)
	ld.console_flush()

def start():
	ld.console_set_custom_font('resources/fonts/arial12x12.png', ld.FONT_TYPE_GREYSCALE | ld.FONT_LAYOUT_TCOD)
	ld.console_init_root(_SCREEN_WIDTH, _SCREEN_HEIGHT, 'Wilson', False)
	ld.console_set_default_background(0, ld.black)
	ld.console_set_default_foreground(0, ld.white)

def stop():
	pass

def get_input():
	key = ld.console_wait_for_keypress(False)
	return key.c

def draw(x, y, char, ventana, color=0):
	c = ord(char)
	h, w = _screen.getmaxyx()
    if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w - 1, h - 1):
        ventana.addch(x, y, c, color)

def write(x, y, string, ventana, color=0):
    h, w = _screen.getmaxyx()
    length = len(string)
    if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w - 1, h - 1):
        ventana.addstr(x, y, string, color)

def refresh():

def clear():
	ld.console_clear(0)

class Ventana:
	def __init__(self, x, y, pos_x=0, pos_y=0):
		self.win = ld.console_new(x, y)
		ld.console_set_default_background(self.win, ld.black)
		ld.console_set_background_flag(self.win, ld.TCOD_BKGND_NONE)
		ld.console_clear(self.win)
		ld.console_blit(self.win, 0, 0, 0, 0, 0, pos_x, pos_y)

	def addch(self, x, y, c, color=0):
		ld.console_set_char_foreground(self.win, 2 * x, y, color)
		ld.console_set_char(self.win, 2 * x, y, c)

	def addstr(self, x, y, string, color=0):
		ld.console_print_ex(self.win, x, y, flag, alignment, fmt)