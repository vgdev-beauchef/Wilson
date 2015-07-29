from Player import *
import gfx
import mapGen
import random
import math
import debug
from entities import *

_windowX = 25
_windowY = 25
_viewRadius = 4


class World(object):

    def __init__(self, width, height):
        self.grid = mapGen.mapGenerator3(width, height)
        self.vgrid = [[False for x in range(width)] for x in range(height)]
        self.memgrid = [[False for x in range(width)] for x in range(height)]
        self.window = gfx.Ventana(_windowX, _windowY)
        #self.player = Player('')

    def scrollingMapX(self):
        p = getPlayPos()[0]
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
        p = getPlayPos()[1]
        s = self.window.height
        hs = s / 2
        m = len(self.grid[0])

        if p < hs:
            return 0
        elif p > m - hs:
            return m - s
        else:
            return p - hs

    def fov(self):
        width = len(self.grid)
        height = len(self.grid[0])
        self.vgrid = [[False for x in range(width)] for x in range(height)]
        for i in range(360):
            x = math.cos(i * 0.01745)
            y = math.sin(i * 0.01745)
            self.doFov(x, y)

    def doFov(self, x, y):
        ox = getPlayPos()[0] + 0.5
        oy = getPlayPos()[1] + 0.5
        for i in range(_viewRadius):
            self.vgrid[int(ox)][int(oy)] = True
            if self.grid[int(ox)][int(oy)] == '#':
                return
            ox += x
            oy += y

    def drawMap(self):
        xCenter = getPlayPos()[0]
        yCenter = getPlayPos()[1]

        w = self.window.width
        h = self.window.height

        cameraX = self.scrollingMapX()
        cameraWidth = _windowX + cameraX
        cameraY = self.scrollingMapY()
        cameraHeight = _windowY + cameraY

        self.fov()

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

                if self.vgrid[x][y] and cha == '#':
                    self.memgrid[x][y] = True

                if self.vgrid[x][y] or debug.debug:
                    self.window.addch(i, j, cha, color)
                elif self.memgrid[x][y]:
                    self.window.addch(i, j, cha, 5)
                else:
                    self.window.addch(i, j, ' ')
        self.window.refresh()
