from Player import Player
import gfx
import mapGen
import random
from entities import *

_windowX = 25
_windowY = 25


class World(object):

    def __init__(self, width, height):
        self.grid = mapGen.mapGenerator3(width, height)
        self.window = gfx.Ventana(_windowX, _windowY)
        self.player = Player('')

    def scrollingMapX(self):
        p = self.player.position[0]
        s = self.window.width
        hs = s / 2
        m = len(self.grid)

        if p < hs:
            return 0
        elif p > m - hs:
            return m - s
        else:
            return p - hs

    def scrollingMapY(self):
        p = self.player.position[1]
        s = self.window.height
        hs = s / 2
        m = len(self.grid[0])

        if p < hs:
            return 0
        elif p > m - hs:
            return m - s
        else:
            return p - hs

    def drawMap(self):
        xCenter = self.player.position[0]
        yCenter = self.player.position[1]

        w = self.window.width
        h = self.window.height

        cameraX = self.scrollingMapX()
        cameraWidth = _windowX + cameraX
        cameraY = self.scrollingMapY()
        cameraHeight = _windowY + cameraY

        for i in range(w):
            for j in range(h):

                x = i + cameraX
                y = j + cameraY

                try:
                    cha = self.grid[x][y]
                except:
                    pass

                if x == xCenter and y == yCenter:
                    cha = '@'

                if cha == '@':
                    color = 4
                elif cha == '#':
                    color = 7
                elif cha == '.':
                    color = 3
                elif cha == '~':
                    color = 6
                else:
                    color = 1
                self.window.addch(i, j, cha, color)
        self.window.refresh()
