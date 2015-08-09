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
        gfx.write(0, 2, 'Hora', self.window)
        gfx.write(0, 3, timeBar(), self.window, 4)
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

def timeBar():
    #Hay que hacer una variable global de tiempo!
    time = 5
    timeToDusk = 10
    porcentage = 100 * time / timeToDusk
    bar = 'D'
    for i in range(18):
        if i * 5 == porcentage:
             bar += '*'
        else:
            bar += '.'
    return bar + 'N'
