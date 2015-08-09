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

class Controller:

	def __init__(self, _world, _log, _info, _inventory, _ope):
		self.world = _world
		self.log = _log
		self.info = _info
		self.inventory = _inventory
		self.ope = _ope
		self.dayCount = 0
		self.dayCountLimit = 30
		self.dayTime = 0

		self.info.setTimeToDusk(self.dayCountLimit)

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

		if ginput=='left' or ginput=='right' or ginput=='up' or ginput=='down':
			self.dayCount+=1
			#self.log.add_event(ginput)
			self.info.setTime(self.dayCount)
			Player.modifyHunger(-1)
			if self.dayCount>self.dayCountLimit:
				self.dayCount=0
				self.log.increase_day()

