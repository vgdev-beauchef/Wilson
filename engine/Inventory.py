__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx import *
import Item

class Inventory:

    def __init__(self):
        self.width = 10
        self.height = 10
        self.xPos = 33
        self.yPos = 10
        self.window = Ventana(self.width, self.height, self.xPos, self.yPos)

        self.items = dict()
        self.max = 5

    def draw(self):
        #inv = ['I' * self.width] * self.height
        # for i in range(len(inv[0])):
        #     for j in range(len(inv)):
        #         draw(i, j, 'I', self.window, 7)

        write(1, 0, '<Inventario>', self.window, 0)

        newlist = sorted(self.items.keys(), key=lambda x: x.id)
        k = 1
        for key in newlist:
            string = "[" + str(k) + "] " +key.name +" : "+ str(self.items[key])
            write(1, k, string, self.window, 0)
            k = k+2

    def refresh(self):
        self.window.refresh()

    def getItem(self, id):
	for key in self.items.keys():
	    if (key.id==id):
		return key;

    def addItem(self, item):
        if(len(self.items)<self.max):
            if(item in self.items):
                self.items[item]=self.items[item]+1
            else:
                self.items[item]=1

    def deleteItem(self, item):
        self.items[item] = self.items[item]-1

    def getQuantity(self, item):
        return self.items[item]
