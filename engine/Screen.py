__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from gfx import *
import codecs
import time


class Screen:

    def __init__(self):
        intro_source = "resources/ascii_images/intro.txt"
        go_source = "resources/ascii_images/game_over.txt"
        credits_source = "resources/ascii_images/credits.txt"
        with codecs.open(intro_source, 'r', "utf-8") as text:
            array = []
            index = -1
            current = []
            for line in text:
                if len(line) > 0 and line[0] == '#':
                    index += 1
                    array.append(list())
                    current = array[index]
                else:
                    current.append(line)

            self.vg_dev = array[0]
            self.vgew = array[1]
            self.wilson = array[2]

            self.width = 44
            self.height = 30
            self.xPos = 0
            self.yPos = 0
            self.window = Ventana(self.width, self.height, self.xPos, self.yPos)
        with codecs.open(go_source, 'r', "utf-8") as text:
            self.game_over = []
            for line in text:
                self.game_over.append(line)

        with codecs.open(credits_source, 'r', "utf-8") as text:
            self.credits = []
            for line in text:
                self.credits.append(line)

    def draw(self, view):
        if view == 1:
            self.draw_array(self.vg_dev)
        elif view == 2:
            self.draw_array(self.vgew)
        elif view == 3:
            self.draw_array(self.wilson)
        elif view == 4:
            self.draw_array(self.game_over)
        elif view == 5:
            self.draw_array(self.credits)

    def draw_array(self, array):
        for i in range(0, len(array)):
            try:
               write(0, i, array[i], self.window, 0)
            except curses.error:
                pass

    def game_over_screen(self):
        self.clean()
        self.refresh()
        self.draw(4)
        self.refresh()
        time.sleep(2)
        self.clean()
        self.refresh()
        self.draw(5)
        self.refresh()


    def refresh(self):
        self.window.refresh()

    def clean(self):
        for i in range(0, self.height):
            empty_string = " "*(2*self.width-1)
            write(0, i, empty_string, self.window, 0)