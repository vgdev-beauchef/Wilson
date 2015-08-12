from Player import *
import gfx
import mapGen
import random
import math
import debug
import matrix
from entities import *

_windowX = 32
_windowY = 18
_viewRadius = 13

colors = {
    'black'         : 0,
    'red'           : 1,
    'green'         : 2,
    'yellow'        : 3,
    'blue'          : 4,
    'magenta'       : 5,
    'cyan'          : 6,
    'white'         : 7,
    'pink'          : 226,
    'gray'          : 95,
    'sand'          : 227,
    'deep-blue'     : 21,
    'grass'         : 83,
    'fucsia'        : 129,
    'dark'          : 246,
    'shallow-blue'  : 124,
    'palm'          : 41,
    'tree'          : 29,
    'gray-night'    : 236,
    'sand-night'    : 71,
    'deep-blue-night':18,
    'grass-night'   : 30,
    'fucsia-night'  : 197,
    'dark-night'    : 254,
    'shallow-blue-night': 28,
    'palm-night'    : 29,
    'tree-night'    : 23,
    'apple'         : 197,
    'fallen_palm'   : 162,
    'boar'          : 167,
    'metal'         : 248
}

tiles = {
    'person' : colors['pink'],
    'rock' : colors['gray'],
    'sand' : colors['sand'],
    'deep' : colors['deep-blue'],
    'grass' : colors['grass'],
    'obj' : colors['fucsia'],
    'cave' : colors['dark'],
    'shallow' : colors['shallow-blue'],
    'palm' : colors['palm'],
    'tree' : colors['tree']
}

asciiToUnicode = {
    '#' :   u'\u2588',
    '~' :   u'\u2248',
    '/' :   u'\u0e45',
    'O' :   u'\u22d2',
    '-' :   '~',
    'Y' :   u'\u1f33',
    'T' :   u'\u1f34'
}




class World(object):

    def __init__(self):
        self.grid = matrix.maptoMatrix('mapa4.txt')

        self.grid[80][170]  = 'j'
        self.grid[93][139]  = 'a'
        self.grid[105][123] = 'w'
        self.grid[115][112] = 'O'
        self.grid[89][101]  = 'X'

        height = len(self.grid[0])
        width = len(self.grid)
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
            pos = self.grid[int(ox)][int(oy)]
            if pos == '#' or\
               pos == 'T' or\
               pos == 'Y':
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

                if cha == '@':          #Personaje
                    color = tiles['person']
                elif cha == '#':        #Roca
                    color = tiles['rock']
                    cha = u'\u2588'
                elif cha == '.':        #Arena
                    color = tiles['sand']
                elif cha == '~':        #Agua profunda
                    color = tiles['deep']
                    cha = u'\u2248'
                elif cha == '/':        #Pasto
                    color = tiles['grass']
                    cha = u'\u0e45'
                elif cha == '*':        #Objeto
                    color = tiles['obj']
                elif cha == 'O':        #Cueva
                    color = tiles['cave']
                    cha = u'\u22d2'
                elif cha == '-':        #agua no profunda
                    color = tiles['shallow']
                    cha = '~'
                elif cha == 'Y':        #palmera
                    color = tiles['palm']
                    cha = u'\u1f33'
                elif cha == 'T':        #arbol
                    color = tiles['tree']
                    cha = u'\u1f34'
                elif cha == 'a':        #manzana
                    color = colors['apple']
                elif cha == 'X':        #evento interesante
                    color = colors['fallen_palm']
                elif cha == 'j':        #jabali
                    color = colors['boar']
                elif cha == 'w':        #cuchillo
                    color = colors['metal']
                elif cha == '&':
                    color = colors['apple']
                elif cha == 'B':
                    color = colors['yellow']
                else:
                    color = 1

                if self.vgrid[x][y]:
                    self.memgrid[x][y] = True

                if self.vgrid[x][y] or debug.debug:
                    self.window.addch(i, j, cha, color)
                elif self.memgrid[x][y]:
                    self.window.addch(i, j, cha, 5)
                else:
                    self.window.addch(i, j, ' ')
        self.window.refresh()
