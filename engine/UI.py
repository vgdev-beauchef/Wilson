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

    def __init__(self, _world, _log, _info, _inventory, _ope):
        self.world = _world
        self.log = _log

        self.info = _info
        self.inventory = _inventory
        self.ope = _ope


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
