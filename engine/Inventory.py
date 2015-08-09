__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx import *

class Inventory:

    def __init__(self):
        self.width = 10
        self.height = 10
        self.xPos = 33
        self.yPos = 10
        self.window = Ventana(self.width, self.height, self.xPos, self.yPos)

        self.items = []
        self.used = 0
        self.max = 5

    def draw(self):

        inv = ['I' * self.width] * self.height
        for i in range(len(inv[0])):
            for j in range(len(inv)):
                draw(i, j, 'I', self.window, 7)

        write(1, 0, '<Inventario>', self.window, 0)

    def refresh(self):
        self.window.refresh()