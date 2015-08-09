from gfx import *
import debug
import sys
import traceback
import world
import Player
import Log
import Inventory
import Item
import Info
import musicPlayer

_inveWindowWidth = 10
_inveWindowHeight = 10
_inveWindowXPos = 33
_inveWindowYPos = 10


class UI:

    def __init__(self):
        self.world = world.World()
        self.log = Log.Log()

        self.info = Info.Info()
        self.inventory = Inventory.Inventory()

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
        elif ginput == '[':
            Player.modifyHunger(-1)
        elif ginput == ']':
            Player.modifyHunger(1)


if __name__ == '__main__':
    try:
        musicPlayer.musicWrapper('resources/tracks/track_01.mid')
        Player.initPlayer('dummy')
        debug.debug = True
        start()
        ui = UI()

        manzana = Item.Item('comida', 1, 'hola')
        cuchillo = Item.Item('cuchillo', 2, 'hola')
        ui.inventory.addItem(manzana)
        ui.inventory.addItem(manzana)
        ui.inventory.addItem(cuchillo)

        while 1:
            ui.world.drawMap()

            # LOG
            ui.log.draw()

            # INFO
            ui.info.draw()


            #INVENTORY
            ui.inventory.draw()

            #OPERATIONS
            ope = ['O' * _opeWindowWidth] * _opeWindowHeight
            for i in range(len(ope[0])):
                for j in range(len(ope)):
                    draw(i, j, 'O', ui.operations, 8)

            ui.operations.refresh()
            ui.log.refresh()
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
