__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from gfx import *
import codecs
import time

class Screen:

    def __init__(self):
        self.read_ascii_art("resources/ascii_images/full.txt")
        self.width = 44
        self.height = 30
        self.xPos = 0
        self.yPos = 0
        self.window = Ventana(self.width, self.height, self.xPos, self.yPos)

    def read_ascii_art(self,filename):
        self.ascii_art = {}
        current = ""
        for line in codecs.open(filename, 'r', "utf-8"):
            if line.startswith("# "):
                current = line[2:-1]
                self.ascii_art[current] = []
                continue
            self.ascii_art[current].append(line)

    def draw(self, view):
        if view == 1:
            self.draw_array(self.ascii_art["vg_dev"])
        elif view == 2:
            self.draw_array(self.ascii_art["vgew"])
        elif view == 3:
            self.draw_array(self.ascii_art["wilson"])
        elif view == 4:
            self.draw_array(self.ascii_art["game_over"])
        elif view == 5:
            self.draw_array(self.ascii_art["credits"])
        elif view == 6:
            self.draw_array(self.ascii_art["prologo"])
        elif view == 7:
            self.draw_array(self.ascii_art["epilogo"])

    def draw_array(self, array):
        for i in range(0, len(array)):
            try:
               write(0, i, array[i], self.window, 0)
            except curses.error:
                pass

    def game_over_screen(self):
        self.draw(4)
        self.refresh()

    def win_screen(self, ending):
        if(ending==1):
            self.draw(7)
        elif(ending==2):
            pass
        else:
            pass
        self.refresh()


    def show_credits(self):
        self.draw(5)
        self.refresh()
        time.sleep(5)

    def refresh(self):
        self.window.refresh()

    def clean(self):
        for i in range(0, self.height):
            empty_string = " "*(2*self.width-1)
            write(0, i, empty_string, self.window, 0)
