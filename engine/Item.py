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