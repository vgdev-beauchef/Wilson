class Entity(object):
    character = ''
    color = 0
    passable = False

class Wall(Entity):
    def __init__(self):
        character = '#'
        color = 3
        passable = False

class Ground(Entity):
    def __init__(self):
        character = '.'
        color = 4
        passable = True

class Water(Entity):
    def __init__(self):
        character = '~'
        color = 6
        passable = True

class OutOfBounds(Entity):
    character = 'X'
    color = 1
    passable = False
