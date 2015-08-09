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

class Controller:

	def __init__(self, _world, _log, _info, _inventory, _ope, _mach, _intro, _ui):
		self.ui = _ui
		self.machine = _mach
		self.world = _world
		self.log = _log
		self.info = _info
		self.inventory = _inventory
		self.ope = _ope
		self.intro = _intro

		self.dayCount = 0
		self.stepCount = 0
		self.dayCountLimit = 30
		self.dayTime = 0
		self.flag = False

		self.hunger_flag_1 = False
		self.hunger_flag_2 = False
		self.hunger_flag_3 = False
		self.option_flag = dict()
		self.option_flag['A'] = False
		self.option_flag['J'] = False
		self.option_flag['W'] = False
		self.option_flag['O'] = False
		self.option_flag['X'] = False

		self.info.setTimeToDusk(self.dayCountLimit)

	def movement(self, ginput):
		px = Player.getPlayPos()[0]
		py = Player.getPlayPos()[1]

		left = self.world.grid[px - 1][py]
		right = self.world.grid[px + 1][py]
		up = self.world.grid[px][py - 1]
		down = self.world.grid[px][py + 1]

		if ginput == 'left' and ((left != '#' and\
								  left != 'T' and\
								  left != 'Y' and\
								  left != '~') or\
		                          debug.debug):
			Player.getPlayPos()[0] -= 1
		elif ginput == 'right' and ((right != '#' and\
								  right != 'T' and\
								  right != 'Y' and\
								  right != '~') or\
		                          debug.debug):
			Player.getPlayPos()[0] += 1
		elif ginput == 'up' and ((up != '#' and\
								  up != 'T' and\
								  up != 'Y' and\
								  up != '~') or\
		                          debug.debug):
			Player.getPlayPos()[1] -= 1
		elif ginput == 'down' and ((down != '#' and\
								  down != 'T' and\
								  down != 'Y' and\
								  down != '~') or\
		                          debug.debug):
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

	def manage_place(self):
		px = Player.getPlayPos()[0]
		py = Player.getPlayPos()[1]

		pos = self.world.grid[px][py]
		option = ""
		yes_answer = ""
		no_aswer = ""
		flag = False

		if pos=='A' and not self.option_flag['A']:
			self.log.add_event("Encontre una manzana")
			option = "que hacer con la manzana?"
			yes_answer = "guardarla"
			no_aswer = "comerla"
			self.option_flag['A'] = True
		elif pos=='J' and not self.option_flag['J']:
			self.log.add_event("Hay una cria de jabali alla... si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...? ")
			option = "que hacer?"
			yes_answer = "matarla"
			no_aswer = "dejarla huir"
			self.option_flag['J'] = True
		elif pos=='W' and not self.option_flag['W']:
			self.log.add_event("Oh! increiblemente he encontrado un cuchillo... se ve muy antiguo, quizas sea de algun pirata. Me podria servir asi que lo guardare.")
			self.option_flag['W'] = True
			return
		elif pos=='O' and not self.option_flag['O']:
			self.log.add_event("Oh, una cueva!! Se escuchan ruidos desde adentro...sera un algun animal?? un oso? Entro?")
			option = "que hacer?"
			yes_answer = "entrar"
			no_aswer = "ignorar"
			self.option_flag['O'] = True
		elif pos=='X' and not self.option_flag['X']:
			self.log.add_event("Me encuentro junto a una enorme palmera caida. No seria muy dificil usarla para construir una balsa...")
			option = "que hacer con la palmera?"
			yes_answer = "construir balsa"
			no_aswer = "ignorar balsa"
			self.option_flag['X'] = True

		if not option=="":
			self.ope.clearWindow()
			self.ope.setOption(option, yes_answer, no_aswer)

			while 1:
				self.ui.draw()
				q = get_input()
				if q =='y':
					if pos=='O' and not flag:
						self.log.add_event('Entre a la cueva')
						
					elif pos == 'X' and not flag:
						self.log.add_event('Decidi ocupar la palmera como balsa')

					elif pos == 'J' and not flag:
						self.log.add_event('Decidi matar al jabali')
						self.inventory.addItem(Item.item('comida',1,'0'))
						self.inventory.addItem(Item.item('comida',1,'0'))

					elif pos == 'A' and not flag:
						self.log.add_event('Guarde la manzana')
						self.inventory.addItem(Item.item('comida',1,'0'))
					flag = True
					break
				elif q == 'n':
					if pos =='O' and not flag:
						self.log.add_event('Decidi no entrar a la cueva')
					elif pos == 'X' and not flag:
						self.log.add_event('Deje la palmera en la playa')
					elif pos == 'J' and not flag:
						self.log.add_event('Deje a la cria tranquila')
					elif pos == 'A' and not flag:
						self.log.add_event('Comi la manzana')
						self.inventory.addItem(Item.item('comida',1,'0'))
						Player.useItem(Item.item('comida',1, '0'), self.inventory)
					flag = True	
					break
			self.ope.clearWindow()
			self.ope.setOption("", "", "")
			flag = False

	def manage(self, ginput):
		pxi = Player.getPlayPos()[0]
		pyi = Player.getPlayPos()[1]

		self.movement(ginput)
		self.manage_place()
		self.manage_log(ginput)

		pxf = Player.getPlayPos()[0]
		pyf = Player.getPlayPos()[1]

		if (ginput=='left' or ginput=='right' or ginput=='up' or ginput=='down') and (pxi!=pxf or pyi!=pyf) and not debug.debug:
			self.dayCount+=1
			self.stepCount+=1
			#self.log.add_event(ginput)
			self.info.setTime(self.dayCount)
			Player.modifyHunger(-1)
			if self.stepCount==46:
				self.log.add_event("Uf... La ultima vez que camine tanto fue ese dia que fuimos de campamento con mi esposa. Recuerdo lo mucho que se reia al verme cojear mientras ella corria por las cuestas.")
			if self.dayCount>self.dayCountLimit:
				self.dayCount=0
				self.log.increase_day()

				self.machine.changeState(self.log)
				self.flag = False
			elif self.dayCount>4*self.dayCountLimit/5 and not self.flag:
				self.machine.changeState(self.log)
				self.flag = True

		percentage = Player.getHunger()[0]
		if percentage <= 0 and not self.hunger_flag_1:
			
			self.hunger_flag_1 = True
			#time.sleep(3)
		elif percentage == 25 and not self.hunger_flag_2:
			self.hunger_flag_2 = True
			self.log.add_event("Me esta empezando a doler el estomago")

		elif percentage == 49 and not self.hunger_flag_3:
			self.hunger_flag_3 = True
			self.hunger_flag_2 = False
			self.log.add_event("Tengo un poco de hambre, deberia comer algo")

		elif percentage>=50:
			self.hunger_flag_3 = False
			self.hunger_flag_2 = False



	def deadCondition(self):
		if(Player.getHunger()[0]<=0):
			self.log.add_event("Creo que no me siento bien... *cae*")
			return True
		return False

