import curses
import traceback, sys

_screen = curses.initscr()
_keypad = {
	curses.KEY_DOWN : 'down',
	curses.KEY_UP   : 'up',
	curses.KEY_LEFT : 'left',
	curses.KEY_RIGHT: 'right',
	curses.KEY_ENTER: 'enter'
}

def start():
	global _screen
	curses.noecho()
	curses.cbreak()
	_screen.keypad(1)
	curses.curs_set(0)


def stop():
	global _screen
	curses.nocbreak()
	_screen.keypad(0)
	curses.echo()
	curses.curs_set(1)
	curses.endwin()

def draw(x, y, char, window):
	c = ord(char)
	window.addch(y, x, c)
	window.refresh()

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

