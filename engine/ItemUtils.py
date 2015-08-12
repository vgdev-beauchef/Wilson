__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx2 import *
from Item import *

class ItemUtils:

    def __init__(self):
        self.items = dict();
        comida = Item.Item("comida", 1, '0')
        self.items['Manzana'] = comida
        self.items['Platano'] = comida
        self.items['Arma'] = Item.Item("cuchillo",2,'0')

    def get_item(self, string):
    	return self.items[string]
