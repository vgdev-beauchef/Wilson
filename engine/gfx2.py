import libtcodpy as ld
import traceback
import sys
import locale

_SCREEN_WIDTH  = 80
_SCREEN_HEIGHT = 40

_colors = {
	0		:ld.black,
	1		:ld.red,
	2		:ld.green,
	3		:ld.yellow,
	4		:ld.blue,
	5		:ld.magenta,
	6		:ld.cyan,
	7		:ld.white,
	226		:ld.pink,
	95		:ld.grey,
	227		:ld.light_yellow,
	21		:ld.dark-blue,
	83		:ld.dark-green,
	129		:ld.fuchsia,
	246		:ld.dark-grey,
	124		:ld.azure,
	41		:ld.dark-lime,
	29		:ld.darker-green,
	236		:ld.darker-grey,
	71		:ld.dark-yellow,
	18		:ld.darker-blue,
	30		:ld.darker-green,
	197		:ld.dark-fuchsia,
	254		:ld.darker-grey,
	28		:ld.dark-azure,
	29		:ld.darker-lime,
	23		:ld.darkest-green,
	197		:ld.red,
	162		:ld.dark-amber,
	167		:ld.darker-sepia,
	248		:ld.lighter-grey
}

_keymap = {

}

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

def draw(x, y, char, ventana, color=7):
	c = ord(char)
	h, w = _screen.getmaxyx()
    if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w - 1, h - 1):
        ventana.addch(x, y, c, color)

def write(x, y, string, ventana, color=7):
    h, w = _screen.getmaxyx()
    length = len(string)
    if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w - 1, h - 1):
        ventana.addstr(x, y, string, color)

def refresh():

def clear():
	ld.console_clear(0)

class Ventana:
	def __init__(self, x, y, pos_x=0, pos_y=7):
		self.win = ld.console_new(x, y)
		self.w = x
		self.h = y
		ld.console_set_default_background(self.win, ld.black)
		ld.console_set_background_flag(self.win, ld.TCOD_BKGND_NONE)
		ld.console_set_background_flag(self.win, TCOD_BKGND_NONE)
		ld.console_set_alignment(self.win, TCOD_LEFT)

	def addch(self, x, y, c, color=0):
		realColor = _colors[color]
		ld.console_set_char_foreground(self.win, 2 * x, y, realColor)
		ld.console_set_char(self.win, 2 * x, y, c)

	def addstr(self, x, y, string, color=7):
		realColor = _colors[color]
		ld.console_print_rect(self.win, x, y, self.w, self.h, string)

	def refresh(self):
		ld.console_blit(self.win, 0, 0, 0, 0, 0, pos_x, pos_y)

	def clear(self):
		ld.console_clear(self.win)
