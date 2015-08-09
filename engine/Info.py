import gfx
import Player
import Controller
import math

_infoWindowWidth = 10
_infoWindowHeight = 10
_infoWindowXPos = 33
_infoWindowYPos = 0


class Info(object):

    def __init__(self):
        self.window = gfx.Ventana(
            _infoWindowWidth, _infoWindowHeight,
            _infoWindowXPos, _infoWindowYPos)
        self.time=0
        self.timeToDusk = 10

    def draw(self):
        self.clearWindow()
        sc = 'Saciedad ' + str(Player.getHunger()[0]) + '/' + str(Player.getHunger()[1])
        gfx.write(0, 0, sc, self.window)
        h = Player.getHunger()[0]
        hungerColor = 41
        if h <= 25:
            hungerColor = 197
        elif h <= 50:
            hungerColor = 209
        gfx.write(0, 1, hungerBar(), self.window, hungerColor)
        gfx.write(0, 2, 'Hora', self.window)
        gfx.write(0, 3, self.timeBar(), self.window, 4)
        self.window.refresh()

    def clearWindow(self):
		clean_string = " " * 19
		for i in range(10):
			gfx.write(0,i,clean_string,self.window,0)

    def timeBar(self):
        percentage = 100 * self.time / self.timeToDusk
        bar = 'D'
        star = math.floor(percentage * 18 / 100)
        for i in range(18):
            if i == star:
                 bar += '*'
            else:
                bar += '.'
        return bar + 'N'

    def setTime(self, _time):
        self.time = _time

    def setTimeToDusk(self, _time):
        self.timeToDusk = _time

def hungerBar():
    h = Player.getHunger()[0]
    H = Player.getHunger()[1]
    percentage = 100 * h / H
    bar = ''
    for i in range(20):
        if i * 5 < percentage:
            bar += '='
        else:
            bar += '-'
    return bar
