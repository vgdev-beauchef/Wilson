import gfx
import Player

_infoWindowWidth = 15
_infoWindowHeight = 30
_infoWindowXPos = 26
_infoWindowYPos = 0


class Info(object):

    def __init__(self):
        self.window = gfx.Ventana(
            _infoWindowWidth, _infoWindowHeight, _infoWindowXPos, _infoWindowYPos)
