import curses
import traceback, sys

_screen = None
_keymap = {
    curses.KEY_DOWN: "down",
    curses.KEY_UP: "up",
    curses.KEY_LEFT: "left",
    curses.KEY_RIGHT: "right",
    curses.KEY_ENTER: "enter",
    -1: None
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
        if c == 27:
            return "escape"
        elif c == 10 or c == 13:
            return "enter"
        elif c > 0 and c <= 256:
            return "%c" % c
        elif c in _keymap:
            return _keymap[c]
    return None


def draw(x, y, char, ventana):
    c = ord(char)
    h, w = _screen.getmaxyx()
    if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w - 1, h - 1):
        ventana.addch(x, y, c)


def refresh():
    global _screen
    if _screen:
        curses.napms(20)


def clear():
    global _screen
    if _screen:
        _screen.erase()


class Ventana:
    def __init__(self, x, y, pos_x=0, pos_y=0):
        self.win = curses.newwin(y, 2 * x, pos_y, 2 * pos_x)
        self.width = x
        self.height = y

    def addch(self, x, y, c):
        self.win.addch(y, 2 * x, c)

    def refresh(self):
        self.win.refresh()


if __name__ == '__main__':
    try:
        start()
        win = Ventana(20, 20)
        myMap = ['.' * 20] * 20
        myPosition = [10, 10]
        while 1:
            for i in range(len(myMap[0])):
                for j in range(len(myMap)):
                    draw(i, j, '.', win)
            draw(myPosition[0], myPosition[1], '@', win)
            win.refresh()
            refresh()
            q = get_input()
            if q == 'q':
                break
            elif q == 'right':
                myPosition[0] += 1
            elif q == 'left':
                myPosition[0] -= 1
            elif q == 'up':
                myPosition[1] -= 1
            elif q == 'down':
                myPosition[1] += 1
        stop()
    except:
        stop()
        print (traceback.format_exc())
        sys.exit(-1)
