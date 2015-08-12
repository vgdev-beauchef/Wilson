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

items = {
    'comida'  : ['a', 1, [[80, 170, '.'], [], [] ]],
    'cuchillo': ['w', 2, [[105, 123, '.']]],
    'balsa'   : ['X', 3, [[89, 101, '.']]],
    'fuego'   : ['&', 4, [[], []]],
    'banana'  : ['B', 5, [[], []]],
    'madera'  : ['M', 6, [[], []]],
    'cuerda'  : ['|', 7, [[], []]],
    'radio'   : ['R', 8, [[], []]],
    'b_jabali': ['j', 9, [[93, 139, '/'], []]],
    'm_jabali': ['J', 10, [[], []]],

}