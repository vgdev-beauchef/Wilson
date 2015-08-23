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
        self.max = 10

    def draw(self):
        #inv = ['I' * self.width] * self.height
        # for i in range(len(inv[0])):
        #     for j in range(len(inv)):
        #         draw(i, j, 'I', self.window, 7)

        write(1, 0, '<Inventario>', self.window, 0)

        newlist = sorted(self.items.keys(), key=lambda x: x.id)
        k = 1
        i = 1
        for key in newlist:
            string = "[" + str(key.id) + "] " +key.name +" : "+ str(self.items[key])
            f = self.width-len(string)
            string = string + '  '
            write(1, k, string, self.window, 0)
            k = k+2
            i += 1

    def refresh(self):
        self.window.refresh()

    def clean(self):        
        clean_string = ' ' * self.width
        for i in range(self.height):
            write(0,i,clean_string,self.window,0)

    def getItem(self, id):
        for key in self.items.keys():
            if (key.id==id):
                return key;
        return None

    def addItem(self, item):
        self.clean()
        if(len(self.items)<self.max):
            if(item in self.items):
                self.items[item]=self.items[item]+1
            else:
                self.items[item]=1

    def deleteItem(self, item):
        self.items[item] = self.items[item]-1

    def getQuantity(self, item):
        return self.items[item]
