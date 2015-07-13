import curses
import traceback, sys

_screen = None
_keymap = {
	curses.KEY_DOWN : "down",
	curses.KEY_UP   : "up",
	curses.KEY_LEFT : "left",
	curses.KEY_RIGHT: "right",
	curses.KEY_ENTER: "enter",
	-1:				  None
}

def start():
	global _screen
	if not _screen:
		_screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0)
		curses.nonl()
		_screen.keypad(1)
		_screen.timeout(0)
		_screen.scrollok(False)
		curses.start_color()


def stop():
	global _screen
	if _screen:
		_screen.timeout(-1)
		_screen.keypad(0)
		_screen.scrollok(True)
		curses.nocbreak()
		curses.curs_set(1)
		curses.nl()
		curses.echo()
		curses.endwin()
		_screen = None

def get_input():
	global _screen, _keymap
	if _screen:
		c = _screen.getch()
		if c == 27: return "escape"
		elif c == 10 or c == 13: return "enter"
		elif c > 0 and c <= 256: return "%c"%c
		elif c in _keymap: return _keymap[c]
	return None

def draw(x, y, char, ventana):
	c = ord(char)
	h, w = _screen.getmaxyx()
	if x >= 0 and x < w and y >= 0 and y < h and (x,y)!=(w-1,h-1):
		ventana.addch(x, y, c)
		ventana.refresh()

def refresh():
	global _screen
	if _screen:
		curses.napms(20)

def clear():
	global _screen
	if _screen:
		_screen.erase()

class ventana:
	def __init__(self, x, y, pos_x = 0, pos_y = 0):
		self.win = curses.newwin(y, 2*x, pos_y, 2*pos_x)
	def addch(self, x, y, c):
		self.win.addch(y, 2*x, c)
	def refresh(self):
		self.win.refresh()

if __name__ == '__main__':
	try:
		start()
		win = ventana(20, 20)
		while 1:
			for i in range(19):
				for j in range(19):
					draw(i, j, '#', win)
			refresh()
			q = get_input()
			if q == 'q':
				break
		stop()
	except:
		stop()
		print (traceback.format_exc())
		sys.exit(-1)

