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
import StateMachine
import time
import pygame.mixer as mixer

class Controller:

	def __init__(self, _world, _log, _info, _inventory, _ope, _mach, _intro):
		self.machine = _mach
		self.world = _world
		self.log = _log
		self.info = _info
		self.inventory = _inventory
		self.ope = _ope
		self.intro = _intro

		self.dayCount = 0
		self.stepCount = 0
		self.dayCountLimit = 60
		self.nightTimeLimit = 30
		self.dayTime = 0
		self.flag = False

		self.hunger_flag_0 = False
		self.hunger_flag_1 = False
		self.hunger_flag_2 = False
		self.hunger_flag_3 = False

		self.info.setTimeToDusk(self.dayCountLimit)
		self.hit_sound = mixer.Sound("resources/tracks/hit.wav")

	def movement(self, ginput):
		px = Player.getPlayPos()[0]
		py = Player.getPlayPos()[1]

		left = self.world.grid[px - 1][py]
		right = self.world.grid[px + 1][py]
		up = self.world.grid[px][py - 1]
		down = self.world.grid[px][py + 1]

		def check(key):
			if not ((key != '#' and key != 'T' and key != 'Y' and key != '~') or debug.debug):
				self.hit_sound.play()
				return False
			return True

		if ginput == 'left' and check(left):
			Player.getPlayPos()[0] -= 1
		elif ginput == 'right' and check(right):
			Player.getPlayPos()[0] += 1
		elif ginput == 'up' and check(up):
			Player.getPlayPos()[1] -= 1
		elif ginput == 'down' and check(down):
			Player.getPlayPos()[1] += 1
		elif ginput == '[':
			Player.modifyHunger(-1)
		elif ginput == ']':
			Player.modifyHunger(1)
		elif ginput == '1':
			self.log.add_event(Player.useItem(self.inventory.getItem(1), self.inventory))
		elif ginput == '2':
			self.log.add_event(Player.useItem(self.inventory.getItem(2), self.inventory))


	def manage_log(self, ginput):
		if ginput == 'i':
			self.log.scroll_up()
		elif ginput == 'k':
			self.log.scroll_down()
		elif ginput == 'j':
			self.log.prev_day()
		elif ginput == 'l':
			self.log.next_day()

	def manage(self, ginput):
		pxi = Player.getPlayPos()[0]
		pyi = Player.getPlayPos()[1]

		self.movement(ginput)
		self.manage_log(ginput)

		pxf = Player.getPlayPos()[0]
		pyf = Player.getPlayPos()[1]

		if (ginput=='left' or ginput=='right' or ginput=='up' or ginput=='down') and (pxi!=pxf or pyi!=pyf) and not debug.debug:
			self.dayCount+=1
			if self.dayCount < self.dayCountLimit/3:
				world._viewRadius = 13
			elif self.dayCount < self.dayCountLimit*2/3:
				world._viewRadius = 10
			else:
				world._viewRadius = 7
			self.stepCount+=1
			#self.log.add_event(ginput)
			self.info.setTime(self.dayCount)
			Player.modifyHunger(-1)
			if self.stepCount==46:
				self.log.add_event("Uf... La ultima vez que camine tanto fue ese dia que fuimos de campamento con mi esposa. Recuerdo lo mucho que se reia al verme cojear mientras ella corria por las cuestas.")

			if self.dayCount>self.nightTimeLimit:
				pass

			if self.dayCount>self.dayCountLimit:
				self.dayCount=0
				self.log.increase_day()

				self.machine.changeState(self.log)
				self.flag = False
			elif self.dayCount>4*self.dayCountLimit/5 and not self.flag:
				self.machine.changeState(self.log)
				self.flag = True

		self.showHungerMessages()
		self.resetHungerFlags()


	def showHungerMessages(self):
		percentage = Player.getHunger()[0]
		if percentage <= 0 and not self.hunger_flag_1:
			self.hunger_flag_1 = True
			#time.sleep(3)
		if percentage ==5 and not self.hunger_flag_0:
			self.hunger_flag_0 = True
			self.log.add_event("No se cuanto mas me pueda mover... Necesito comer algo")

		elif percentage == 25 and not self.hunger_flag_2:
			self.hunger_flag_2 = True
			self.log.add_event("Me esta empezando a doler el estomago")

		elif percentage == 49 and not self.hunger_flag_3:
			self.hunger_flag_3 = True
			self.log.add_event("Tengo un poco de hambre, deberia comer algo")

	def resetHungerFlags(self):
		percentage = Player.getHunger()[0]
		if percentage>=6 and self.hunger_flag_0:
			self.hunger_flag_0 = False
		if percentage>=26 and self.hunger_flag_2:
			self.hunger_flag_2 = False
		if percentage>=50 and self.hunger_flag_3:
			self.hunger_flag_3 = False


	def deadCondition(self):
		if(Player.getHunger()[0]<=0):
			self.log.add_event("Creo que no me siento bien... *cae*")
			return True
		return False
