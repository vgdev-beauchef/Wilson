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

def modifyHunger(n):
    global _player
    if _player:
        if _player.hunger + n <= _player.maxHunger and\
           _player.hunger + n >= 0:
           _player.hunger += n

def useItem(item):
    if(item.name=="Comida"):
        modifyHunger(20)
        return "Comi Algo"
    else:
        return "Miro mi arma, podria ser util"


class Player(Entity):
    def __init__(self, name):
        character = '@'
        color = 2
        passable = True
        self.name = name
        self.position = [random.randint(0, 199), random.randint(0, 199)]
        self.maxHunger = 100
        self.hunger = 50
        self.sanity = 10
