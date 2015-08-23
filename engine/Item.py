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
        return self.id == other.id

def create(name):
    index = items[name][1]
    return Item(name, index, '0')

def getAscii(name):
    return items[name][0]  

def getReplacement(name, x, y):
    l = items[name][2]
    elem = None
    for coords in l:
        if coords[0]==x and coords[1]==y:
            elem = coords[2]
    if elem == None:
        elem = '.'
    return elem

def getItemPos(name):
    l = items[name][2]
    for coords in l:
        return (coords[0], coords[1])

def getItemId(name):
    return items[name][1]

def addItem(name, x, y, before):
    l = items[name][2]
    l.append([x, y, before])

def removeItem(name):
    items[name][2] = []

def addNextFood(world):
    if(len(next_items)==0):
        return False

    i = next_items[0]

    x = i[3]
    y = i[4]

    before = world.grid[x][y]
    addItem(i[0], x, y, before)

    world.grid[x][y] = i[1]

    del next_items[0]

    return True


items = {
    'comida'  : ['a', 1, [[93, 139, '/']]],
    'cuchillo': ['w', 2, [[105, 123, '.']]],
    'balsa'   : ['X', 3, [[89, 101, '.']]],
    'fuego'   : ['&', 4, [[92, 90, '.']]],
    'banana'  : ['B', 5, [[68, 161, '/']]],
    'madera'  : ['M', 6, [[89, 160, '.']]],
    'cuerda'  : ['|', 7, [[89, 139, '/']]],
    'b_jabali': ['j', 9, [[80, 170, '.']]],
    'm_jabali': ['J', 10, [[65, 148, '/']]],
    'dead_man': ['1', 11, [[60, 176, '.']]],
    'radio'   : ['R', 12, [[112, 100, '.']]],
    'palmera' : ['F', 13, [[34, 107, '-']]],
    'cueva'   : ['O', 14, [[117, 112, 'O']]]
}

next_items = [
    ['comida', 'a', 1, 60, 145],
    ['comida', 'a', 1, 75, 132],
    ['comida', 'a', 1, 54, 170],
    ['comida', 'a', 1, 94, 117],
    ['comida', 'a', 1, 96, 102],
    ['comida', 'a', 1, 80, 122],
    ['comida', 'a', 1, 37,  122],
    ['comida', 'a', 1, 100, 112],
    ['comida', 'a', 1, 109, 133],
    ['comida', 'a', 1, 31, 149]
]