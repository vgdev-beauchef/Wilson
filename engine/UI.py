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
#import musicPlayer
import optionsUI

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
        self.ope = optionsUI.optionsUI()

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
        elif ginput == '1':
	        self.log.add_event(Player.useItem(self.inventory.getItem(1), self.inventory))
        elif ginput == '2':
            self.log.add_event(Player.useItem(self.inventory.getItem(2), self.inventory))
        elif ginput == 'i':
            self.log.scroll_up()
        elif ginput == 'k':
            self.log.scroll_down()
        elif ginput == 'j':
            self.log.prev_day()
        elif ginput == 'l':
            self.log.next_day()

        elif ginput == '1':
            self.log.increase_day()
        elif ginput == '2':
            self.log.add_event("Elephant")

    def draw(self):
        self.world.drawMap()

        # LOG
        self.log.draw()

        # INFO
        self.info.draw()

        #INVENTORY
        self.inventory.draw()

        #OPERATIONS
        self.ope.draw()

        self.log.refresh()
        self.inventory.refresh()
