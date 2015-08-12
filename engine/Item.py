__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx import *

class Item:

    def __init__(self, _name, _id, _action):
        self.name=_name
        self.id=_id
        self.action=_action

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

def create(name):
    index = items[name][1]
    return Item(name,index, '0')

def getAscii(name):
    return items[name][0]  

def getReplacement(name, x, y):
    l = items[name][2]
    for coords in l:
        if coords[0]==x and coords[1]==y:
            return coords[2]

def getItemPos(name):
    l = items[name][2]
    for coords in l:
        return (coords[0], coords[1])

def addItem(name, x, y, before):
    l = items[name][2]
    l.append([x, y, before])

def removeItem(name):
    items[name][2] = []

items = {
    'comida'  : ['a', 1, [[93, 139, '/']]],
    'cuchillo': ['w', 2, [[105, 123, '.']]],
    'balsa'   : ['X', 3, [[89, 101, '.']]],
    'fuego'   : ['&', 4, [[92, 90, '.']]],
    #'fuego'   : ['&', 4, [[83, 165, '.']]],
    'banana'  : ['B', 5, [[68, 161, '/']]],
    'madera'  : ['M', 6, [[89,], [160]]],
    'cuerda'  : ['|', 7, [[89, 139, '/']]],
    'b_jabali': ['j', 9, [[80, 170, '.']]],
    'm_jabali': ['J', 10, [[81, 164, '/']]],
    'dead_man': ['1', 11, [[82, 162, '/']]]

}