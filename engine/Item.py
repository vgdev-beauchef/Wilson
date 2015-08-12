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
    'comida'  : ['a', 1, [[93, 139, '/'], [], [] ]],
    'cuchillo': ['w', 2, [[105, 123, '.']]],
    'balsa'   : ['X', 3, [[89, 101, '.']]],
    'fuego'   : ['&', 4, [[92, 90, '.']]],
    'banana'  : ['B', 5, [[68, 161, '/']]],
    'madera'  : ['M', 6, [[89,], [160]]],
    'cuerda'  : ['|', 7, [[89, 139, '/']]],
    'b_jabali': ['j', 9, [[80, 170, '.'], [78, 154, '/']]],
    'm_jabali': ['J', 10, [[81, 164, '/']]],

}