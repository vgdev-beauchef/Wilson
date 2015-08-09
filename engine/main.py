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
import os
import time
import pygame

if __name__ == '__main__':
    if os.environ["COLORTERM"] ==  "gnome-terminal":
        os.environ["TERM"] = "xterm-256color"


    try:
        #musicPlayer.musicWrapper('resources/tracks/track_01.mid')
        pygame.init()
        pygame.mixer.music.load('resources/tracks/mainloop.wav')
        pygame.mixer.music.play(-1, 0.0)

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
        controller = Controller.Controller(world, log, info, inventory, ope, intro)

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

        while not controller.deadCondition():
            ui.draw()

            # INPUT
            q = get_input()
            if q == 'q':
                break
            elif q == 'd':
                intro.game_over_screen()
                time.sleep(5)
                break

            elif q == 'enter':
                debug.debug = not debug.debug
            controller.manage(q)
        stop()
    except:
        stop()
        print(traceback.format_exc())
        sys.exit(-1)
pygame.mixer.music.stop()
sys.exit(0)
