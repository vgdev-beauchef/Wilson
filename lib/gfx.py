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

def draw(x, y, char, window):
	c = ord(char)
	h, w = _screen.getmaxyx()
	if x >= 0 and x < w and y >= 0 and y < h and (x,y)!=(w-1,h-1):
		window.addch(y, x, c)

def refresh():
	global _screen
	if _screen:
		_screen.napms(20)

def clear():
	global _screen
	if _screen:
		_screen.erase()

if __name__ == '__main__':
	win = curses.newwin(10, 10, 10, 10)
	try:
		start()
		while 1:
			draw(5, 5, '@', win)
	except:
		stop()
		print (traceback.format_exc())
		sys.exit(-1)

