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
import time

import LinearStateMachine
import StoryStateMachine
import Story
import Events
import pygame.mixer as mixer
import InputMap

class Controller:

	def __init__(self, _world, _log, _info, _inventory, _ope, _mach, _intro, _ui, _keyMap):
		self.ui = _ui
		self.machine = _mach
		self.world = _world
		self.log = _log
		self.info = _info
		self.inventory = _inventory
		self.ope = _ope
		self.intro = _intro
		self.key_map = _keyMap


		self.dayCount = 0
		self.stepCount = 0
		self.dayCountLimit = 80
		self.nightTimeLimit = 40
		self.dayTime = 0

		self._killedByBear = False
		self.escape = False

		self.hunger_flag_0 = False
		self.hunger_flag_1 = False
		self.hunger_flag_2 = False
		self.hunger_flag_3 = False

		self.info.setTimeToDusk(self.dayCountLimit)
		self.hit_sound = mixer.Sound("resources/tracks/hit.wav")

		self.mapDisp = False

		#StateMachine for the Time Messages
		self.linearState = LinearStateMachine.LinearStateMachine(self.dayCountLimit)

		#Create the story
		self.events = Events.Events(self.world, self.inventory, self.dayCountLimit, self.log, self.info)

		self.story = Story.Story(self.world, self.inventory, self.dayCountLimit, self.log, self.events, self.info)


		#StateMachine for the story
		self.storyState = StoryStateMachine.StoryStateMachine(self.ui, self.log, self.ope,
															self.story.initStoryState)

		#StateMachine for the Events
		self.eventsState = StoryStateMachine.StoryStateMachine(self.ui, self.log, self.ope,
											self.events.getCurrentList())


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
		elif ginput == 'it_1':
			if not self.inventory.getItem(1) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(1), self.inventory))
		elif ginput == 'it_2':
			if not self.inventory.getItem(2) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(2), self.inventory))
		elif ginput == 'it_3':
			if not self.inventory.getItem(3) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(3), self.inventory))


	def manage_log(self, ginput):
		if ginput == 'log_up':
			self.log.scroll_up()
		elif ginput == 'log_down':
			self.log.scroll_down()
		elif ginput == 'log_left':
			self.log.prev_day()
		elif ginput == 'log_right':
			self.log.next_day()

	#def reset_place(self, x, y):


	def manage_place(self):
		px = Player.getPlayPos()[0]
		py = Player.getPlayPos()[1]

		pos = self.world.grid[px][py]
		option = ""
		yes_answer = ""
		no_aswer = ""
		flag = False

	def manage(self, ginput):
		pxi = Player.getPlayPos()[0]
		pyi = Player.getPlayPos()[1]

		self.movement(ginput)
		self.manage_place()
		self.manage_log(ginput)

		pxf = Player.getPlayPos()[0]
		pyf = Player.getPlayPos()[1]

		if self.escape:
			return

		if self.key_map.is_visible():
			#TODO
			if ginput == 'map':
				self.key_map.visibility(False)
			return

		if ginput == 'map':
			#TODO
			self.key_map.visibility(True)
			return

		if (ginput=='left' or ginput=='right' or ginput=='up' or ginput=='down') and (pxi!=pxf or pyi!=pyf) and not debug.debug:
			self.dayCount+=1
			self.stepCount+=1
			if self.dayCount < self.dayCountLimit/3:
				world._viewRadius = 13
			elif self.dayCount < self.dayCountLimit*2/3:
				world._viewRadius = 10
			else:
				world._viewRadius = 7
			if self.dayCount < self.dayCountLimit*2/3:
				world.tiles['rock']      = world.colors['gray']
				world.tiles['sand']      = world.colors['sand']
				world.tiles['deep']      = world.colors['deep-blue']
				world.tiles['grass']     = world.colors['grass']
				world.tiles['obj']       = world.colors['fucsia']
				world.tiles['cave']      = world.colors['dark']
				world.tiles['shallow']   = world.colors['shallow-blue']
				world.tiles['palm']      = world.colors['palm']
				world.tiles['tree']      = world.colors['tree']
			else:
				world.tiles['rock']      = world.colors['gray-night']
				world.tiles['sand']      = world.colors['sand-night']
				world.tiles['deep']      = world.colors['deep-blue-night']
				world.tiles['grass']     = world.colors['grass-night']
				world.tiles['obj']       = world.colors['fucsia-night']
				world.tiles['cave']      = world.colors['dark-night']
				world.tiles['shallow']   = world.colors['shallow-blue-night']
				world.tiles['palm']      = world.colors['palm-night']
				world.tiles['tree']      = world.colors['tree-night']
			#self.log.add_event(ginput)
			self.info.setTime(self.dayCount)
			Player.modifyHunger(-1)

			if self.dayCount>self.dayCountLimit:
				self.dayCount=0
				self.log.increase_day()

			self.linearState.changeState(self.stepCount, self.log)
			self.storyState.computeStoryState(self.dayCount, self.stepCount, pxf, pyf)
			self.eventsState.checkIndividualStates(self.dayCount, self.stepCount, pxf, pyf, self.events.getCurrentList())

		self.showHungerMessages()
		self.resetHungerFlags()


	def showHungerMessages(self):
		percentage = Player.getHunger()[0]
		if percentage <= 0 and not self.hunger_flag_1:
			self.hunger_flag_1 = True
			#time.sleep(3)
		if percentage ==5 and not self.hunger_flag_0:
			self.hunger_flag_0 = True
			self.log.add_event("No se cuanto mas me pueda mover... necesito comer algo")

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


	def killed(self):
		if self._killedByBear:
			self.log.add_event("Esto fue... demasiado para ... mi",197)
			#self.log.add_event("Presiona enter para continuar")
			self.info.gameOver()
		return self._killedByBear

	def deadCondition(self):
		if(Player.getHunger()[0]<=0):
			self.log.add_event("Creo que no me siento bien... *cae*",250)
			#self.log.add_event("Presiona enter para continuar")
			self.info.gameOver()
			return True
		return False
