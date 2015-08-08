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

class Player(Entity):
    def __init__(self, name):
        character = '@'
        color = 2
        passable = True
        self.name = name
        self.position = [random.randint(0, 50), random.randint(0, 50)]
        self.hunger = 10
        self.sanity = 10
