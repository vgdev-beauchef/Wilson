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
from pygame.locals import *
import StateMachine
import KeyMap
import InputMap

if __name__ == '__main__':

    try:
        debug.debug = sys.argv[1] == "-d"
    except:
        debug.debug = False

    os.environ["TERM"] = "xterm-256color"


    try:
        pygame.init()
        pygame.mixer.music.load('resources/tracks/mainloop.wav')
        pygame.mixer.music.play(-1, 0.0)

        Player.initPlayer('dummy')
        start()

        #Initilization
        machine = StateMachine.StateMachine()
        world = world.World()
        log = Log.Log()
        info = Info.Info()
        inventory = Inventory.Inventory()
        ope = optionsUI.optionsUI()
        intro = Screen.Screen()
        key_map = KeyMap.KeyMap(42, 18)

        escape = False


        ui = UI.UI(world, log, info, inventory, ope, machine, key_map)
        machine.changeState(log, ui)
        controller = Controller.Controller(world, log, info, inventory, ope, machine, intro, ui, key_map)


        #manzana = Item.Item('comida', 1, 'hola')
        #cuchillo = Item.Item('cuchillo', 2, 'hola')
        #ui.inventory.addItem(manzana)
        #ui.inventory.addItem(manzana)
        #ui.inventory.addItem(cuchillo)
        wait_time = 3

        if not debug.debug:
            intro.draw(1)
            intro.refresh()
            time.sleep(wait_time)
            intro.draw(2)
            intro.refresh()
            time.sleep(wait_time)
        while 1:
            if not debug.debug:
                intro.draw(3)
                intro.refresh()
                q = InputMap.key(get_input())
                if q == 'enter':
                    break
            else: break
        while 1:
            if not debug.debug:
                intro.draw(6)
                intro.refresh()
                q = InputMap.key(get_input())
                if q == 'enter':
                    intro.clean()
                    intro.refresh()
                    break
            else: break


        while not controller.deadCondition() and not controller.killedByBear():
            ui.draw()

            # INPUT
            q = InputMap.key(get_input())
            if q == 'quit':
                stop()
                sys.exit(0)

            elif q == 'enter':
                debug.debug = not debug.debug
            controller.manage(q)
            escape = controller.escape
            if escape:
                break
        while 1:
            ui.draw()

            q = InputMap.key(get_input())
            if q == 'enter':
                break
            controller.manage_log(q)

        intro.clean()
        intro.refresh()
        if not escape:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('resources/tracks/end.wav')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(1, 0.0)
        while 1 :
            if escape:
                intro.win_screen()
            else:
                intro.game_over_screen()
                time.sleep(2)
                break
            q = InputMap.key(get_input())
            if q == 'enter':
                break
        intro.clean()
        intro.refresh()
        intro.show_credits()
        stop()
    except:
        stop()
        print(traceback.format_exc())
        sys.exit(-1)

stop()
pygame.mixer.music.stop()
sys.exit(0)
