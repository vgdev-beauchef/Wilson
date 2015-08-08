__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from gfx import *

class Log:

    def __init__(self):
        self.width = 32
        self.height = 11
        self.xPos = 0
        self.yPos = 19
        self.window = Ventana(self.width, self.height, self.xPos, self.yPos)

    def draw(self):
        log = ['%' * self.width] * self.height
        for i in range(len(log[0])):
            for j in range(len(log)):
                draw(i, j, '%', self.window, 5)

    def refresh(self):
        self.window.refresh()