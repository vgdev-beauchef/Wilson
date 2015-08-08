from gfx import *
import debug
import sys
import traceback
import world
import Player
import Log

_infoWindowWidth = 10
_infoWindowHeight = 10
_infoWindowXPos = 33
_infoWindowYPos = 0

_inveWindowWidth = 10
_inveWindowHeight = 10
_inveWindowXPos = 33
_inveWindowYPos = 10

_opeWindowWidth = 10
_opeWindowHeight = 10
_opeWindowXPos = 33
_openWindowYPos = 20


class UI:

    def __init__(self):
        self.world = world.World(200, 200)
        self.log = Log.Log()
        self.info = Ventana(
            _infoWindowWidth, _infoWindowHeight,
            _infoWindowXPos, _infoWindowYPos)
        self.inventory = Ventana(
            _inveWindowWidth, _inveWindowHeight,
            _inveWindowXPos, _inveWindowYPos)
        self.operations = Ventana(
            _opeWindowWidth, _opeWindowHeight,
            _opeWindowXPos, _openWindowYPos)

    def movement(self, ginput):
        px = Player.getPlayPos()[0]
        py = Player.getPlayPos()[1]
        if ginput == 'left' and (self.world.grid[px - 1][py] != '#' or debug.debug):
            Player.getPlayPos()[0] -= 1
        elif ginput == 'right' and (self.world.grid[px + 1][py] != '#' or debug.debug):
            Player.getPlayPos()[0] += 1
        elif ginput == 'up' and (self.world.grid[px][py - 1] != '#' or debug.debug):
            Player.getPlayPos()[1] -= 1
        elif ginput == 'down' and (self.world.grid[px][py + 1] != '#' or debug.debug):
            Player.getPlayPos()[1] += 1


if __name__ == '__main__':
    try:
        Player.initPlayer('dummy')
        debug.debug = True
        start()
        ui = UI()
        while 1:
            ui.world.drawMap()

            # LOG
            ui.log.draw()

            # INFO
            info = ['$' * _infoWindowWidth] * _infoWindowHeight
            for i in range(len(info[0])):
                for j in range(len(info)):
                    draw(i, j, '$', ui.info, 6)


            #INVENTORY
            inv = ['I' * _inveWindowWidth] * _inveWindowHeight
            for i in range(len(inv[0])):
                for j in range(len(inv)):
                    draw(i, j, 'I', ui.inventory, 7)

            #OPERATIONS
            ope = ['O' * _opeWindowWidth] * _opeWindowHeight
            for i in range(len(ope[0])):
                for j in range(len(ope)):
                    draw(i, j, 'O', ui.operations, 8)

            ui.operations.refresh()
            ui.log.refresh()
            ui.info.refresh()
            ui.inventory.refresh()

            # INPUT
            q = get_input()
            if q == 'q':
                break
            elif q == 'enter':
                debug.debug = not debug.debug
            ui.movement(q)
        stop()
    except:
        stop()
        print(traceback.format_exc())
        sys.exit(-1)
sys.exit(0)
