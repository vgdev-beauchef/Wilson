import gfx
import Player

_infoWindowWidth = 10
_infoWindowHeight = 10
_infoWindowXPos = 33
_infoWindowYPos = 0


class Info(object):

    def __init__(self):
        self.window = gfx.Ventana(
            _infoWindowWidth, _infoWindowHeight,
            _infoWindowXPos, _infoWindowYPos)

    def draw(self):
        gfx.write(0, 0, 'Hambre', self.window)
        gfx.write(0, 1, hungerBar(), self.window, 2)
        self.window.refresh()

def hungerBar():
    h = Player.getHunger()[0]
    H = Player.getHunger()[1]
    porcentage = 100 * h / H
    bar = ''
    for i in range(20):
        if i * 5 < porcentage:
            bar += '='
        else:
            bar += '-'
    return bar
