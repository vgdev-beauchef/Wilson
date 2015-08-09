import random
from entities import Entity

_player = None


def initPlayer(name):
    global _player
    if not _player:
        _player = Player(name)


def getPlayPos():
    global _player
    if _player:
        return _player.position

def getHunger():
    global _player
    if _player:
        return (_player.hunger, _player.maxHunger)

def modifyHunger(n): #Se le esta sumando a la cantidad de comida
    global _player
    if _player:
        if _player.hunger + n <= _player.maxHunger and\
           _player.hunger + n >= 0:
           _player.hunger += n

def useItem(item, inventory):
    
    if(item.name.lower()=="comida"):
        if(inventory.getQuantity(item)>0):
            inventory.deleteItem(item)
            modifyHunger(20)
            return "Comi Algo"
        return "No me queda que comer"
    else:
        return "Miro mi arma, podria ser util"


class Player(Entity):
    def __init__(self, name):
        character = '@'
        color = 2
        passable = True
        self.name = name
        self.position = [77, 173]
        self.maxHunger = 100
        self.hunger = 50
        self.sanity = 10
