from gfx2 import *
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

    def __init__(self, _world, _log, _info, _inventory, _ope, _mach, _keyMap):
        self.world = _world
        self.log = _log
        self.machine = _mach
        self.key_map = _keyMap

        self.info = _info
        self.inventory = _inventory
        self.ope = _ope

    def draw(self):
        #Key Map
        if self.key_map.is_visible():
            self.key_map.draw()
            self.key_map.refresh()
            return

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
