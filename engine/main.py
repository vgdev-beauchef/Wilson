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
import optionsUI
import UI
import Controller
import Screen
import time

if __name__ == '__main__':

    try:
        #musicPlayer.musicWrapper('resources/tracks/track_01.mid')
        Player.initPlayer('dummy')
        debug.debug = True
        start()

        #Initilization
        world = world.World()
        log = Log.Log()
        info = Info.Info()
        inventory = Inventory.Inventory()
        ope = optionsUI.optionsUI()
        intro = Screen.Screen()

        ui = UI.UI(world, log, info, inventory, ope)
        controller = Controller.Controller(world, log, info, inventory, ope)

        manzana = Item.Item('comida', 1, 'hola')
        cuchillo = Item.Item('cuchillo', 2, 'hola')
        ui.inventory.addItem(manzana)
        ui.inventory.addItem(manzana)
        ui.inventory.addItem(cuchillo)

        wait_time = 3
        intro.draw(1)
        intro.refresh()
        time.sleep(wait_time)
        intro.draw(2)
        intro.refresh()
        time.sleep(wait_time)
        while 1:
            intro.draw(3)
            intro.refresh()
            q = get_input()
            if q == 'enter':
                intro.clean()
                intro.refresh()
                intro.refresh()
                break

        while 1:
            ui.draw()

            # INPUT
            q = get_input()
            if q == 'q':
                break
            elif q == 'enter':
                debug.debug = not debug.debug
            controller.movement(q)
        stop()
    except:
        stop()
        print(traceback.format_exc())
        sys.exit(-1)
sys.exit(0)

