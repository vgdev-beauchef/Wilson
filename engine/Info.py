import gfx
import Player
import Controller
import math
import debug

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
        self._gameOver = False

        self.final1 = False
        self.final2 = False
        self.final3 = False
        self.pos=[-1,-1]

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
        if(not debug.debug):
            gfx.write(0, 4, " " * 19, self.window, 4)
        else:
            gfx.write(0, 4, str(self.pos[0])+','+str(self.pos[1]), self.window, 4)
        if self._gameOver:
            gfx.write(0, 5, 'Presione enter para continuar', self.window)
        self.window.refresh()

    def gameOver(self):
        self._gameOver = True

    def gameFinal1(self):
        self.final1 = True

    def gameFinal2(self):
        self.final2 = True

    def gameFinal3(self):
        self.final3 = True

    def clearWindow(self):
		clean_string = " " * 19
		for i in range(10):
			gfx.write(0,i,clean_string,self.window,0)

    def setPos(self, pxf, pyf):
        self.pos[0]=pxf
        self.pos[1]=pyf

    def timeBar(self):
        percentage = 100 * self.time / self.timeToDusk
        bar = u'\u2600'
        star = math.floor(percentage * 18 / 100)
        for i in range(18):
            if i == star:
                 bar += '*'
            else:
                bar += '.'
        return bar + u'\u263d'

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
