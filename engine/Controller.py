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
import musicPlayer
import optionsUI
import StateMachine
import time
import pygame.mixer as mixer

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
		self.flag = False
		self._killedByBear = False

		self.hunger_flag_0 = False
		self.hunger_flag_1 = False
		self.hunger_flag_2 = False
		self.hunger_flag_3 = False
		self.option_flag = dict()
		self.option_flag['A'] = False
		self.option_flag['J'] = False
		self.option_flag['W'] = False
		self.option_flag['O'] = False
		self.option_flag['X'] = False
		self.cueva = False
		self.escape = False

		self.info.setTimeToDusk(self.dayCountLimit)
		self.hit_sound = mixer.Sound("resources/tracks/hit.wav")

		self.mapDisp = False

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
			if not self.inventory.getItem(1) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(1), self.inventory))
		elif ginput == '2':
			if not self.inventory.getItem(2) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(2), self.inventory))
		elif ginput == '3':
			if not self.inventory.getItem(3) is None:
				self.log.add_event(Player.useItem(self.inventory.getItem(3), self.inventory))


	def manage_log(self, ginput):
		if ginput == 'i':
			self.log.scroll_up()
		elif ginput == 'k':
			self.log.scroll_down()
		elif ginput == 'j':
			self.log.prev_day()
		elif ginput == 'l':
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

		if pos=='-' and self.inventory.getItem(3) != None :
			self.log.add_event('He vuelto a la costa con mi balsa. Me ire de aqui porque estoy seguro de que encontrare a alguien. Ojala alguien mas que yo pueda leer este diario algun dia...')
			#self.ui.draw()
			#time.sleep(0.5)
			#self.log.add_event("Presione enter para continuar")
			self.info.gameOver()
			self.escape = True
			return

		if pos!='O':
			self.cueva = False

		if pos=='a' and not self.option_flag['A']:
			self.log.add_event("Encontre una manzana")
			option = "Que hacer con la manzana?"
			yes_answer = "Guardarla"
			no_aswer = "Comerla"
			self.option_flag['A'] = True
			self.world.grid[80][170]  = '.'
		elif pos=='j' and not self.option_flag['J']:
			self.log.add_event("Hay una cria de jabali alla... si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...? ")
			option = "Que hacer?"
			yes_answer = "Matarla"
			no_aswer = "Dejarla huir"
			self.option_flag['J'] = True
			self.world.grid[93][139] = '/'
		elif pos=='w' and not self.option_flag['W']:
			self.log.add_event("Oh! increiblemente he encontrado un cuchillo... se ve muy antiguo, quizas sea de algun pirata. Me podria servir asi que lo guardare.")
			c = Item.Item("cuchillo",2,'0')
			self.inventory.addItem(c)
			self.option_flag['W'] = True
			self.world.grid[105][123] = '.'
			return
		elif pos=='O' and not self.option_flag['O'] and not self.cueva:
			self.log.add_event("Oh, una cueva!! Se escuchan ruidos desde adentro...sera un algun animal?? Un oso? Entro?")
			option = "Que hacer?"
			yes_answer = "Entrar"
			no_aswer = "Ignorar"
			self.option_flag['O'] = True
			self.cueva = True
		elif pos=='X' and not self.option_flag['X']:
			self.log.add_event("Me encuentro junto a una enorme palmera caida. No seria muy dificil usarla para construir una balsa...")
			option = "Que hacer con la palmera?"
			yes_answer = "Construir balsa"
			no_aswer = "Ignorar balsa"
			self.option_flag['X'] = True
			self.world.grid[89][101] = '.'


		if not option=="":
			self.ope.clearWindow()
			self.ope.setOption(option, yes_answer, no_aswer)
			oso = False

			while 1:
				self.ui.draw()
				q = get_input()
				if oso:
					if q == 'y':
						if self.inventory.getItem(2) is None:
							self._killedByBear = True
						else:
							self.log.add_event('Logre matarlo !! La cueva me servira de refugio. Ademas podre utilizar su piel como abrigo. Creo que esta noche podre dormir tranquilo. Descansare pues ha sido un dia muy agitado.')
							self.ui.draw()
							time.sleep(1)
							c = Item.Item('comida',1,'0')
							self.inventory.addItem(c)
							self.inventory.addItem(c)
							self.inventory.addItem(c)
							self.log.add_event('El olor de la cueva me recuerda a los enormes perros que cuidaban las ovejas de mi abuelo y como yo dormia abrazado a ellos. Casi puedo sentir su agradable calor.')
							self.ope.setOption("","","")
							self.ui.draw()
							time.sleep(5)
							self.dayCount = self.dayCountLimit
						break
					elif q == 'n':
						self.log.add_event('No puedo pelear contra ese oso. Es mejor que huya')
						self.option_flag['O']=False
						oso = False
						break

				if q =='y':
					if pos=='O' and not flag:
						self.log.add_event('Entre a la cueva')
						self.log.add_event('Aparece un oso salvaje!!!')
						self.ope.clearWindow()
						self.ope.setOption('Que hacer?', 'Atacar', 'Huir')
						oso = True
						continue
					elif pos == 'X' and not flag:
						self.log.add_event('Decidi ocupar la palmera para construir una balsa')
						c = Item.Item('balsa',3,'0')
						self.inventory.addItem(c)
						break

					elif pos == 'j' and not flag:
						self.log.add_event('Decidi matar al jabali')
						c = Item.Item('comida',1,'0')
						self.inventory.addItem(c)
						self.inventory.addItem(c)
						break

					elif pos == 'a' and not flag:
						self.log.add_event('Guarde la manzana')
						c = Item.Item('comida',1,'0')
						self.inventory.addItem(c)
						break
					flag = True

				elif q == 'n':
					if pos =='O' and not flag:
						self.log.add_event('Decidi no entrar a la cueva')
						self.option_flag['O']=False
					elif pos == 'X' and not flag:
						self.log.add_event('Deje la palmera en la playa')
					elif pos == 'j' and not flag:
						self.log.add_event('Deje a la cria tranquila')
					elif pos == 'a' and not flag:
						self.log.add_event('Comi la manzana')
						c = Item.Item('comida',1,'0')
						self.inventory.addItem(c)
						Player.useItem(c, self.inventory)
					flag = True
					break
				q=''
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

		if self.escape:
			return

		if self.key_map.is_visible():
			#TODO
			if ginput=='m':
				self.key_map.visibility(False)
			return

		if ginput=='m':
			#TODO
			self.key_map.visibility(True)
			return

		if (ginput=='left' or ginput=='right' or ginput=='up' or ginput=='down') and (pxi!=pxf or pyi!=pyf) and not debug.debug:
			self.dayCount+=1
			if self.dayCount < self.dayCountLimit/3:
				world._viewRadius = 13
			elif self.dayCount < self.dayCountLimit*2/3:
				world._viewRadius = 10
			else:
				world._viewRadius = 7
			if self.dayCount < self.dayCountLimit*2/3:
				world.tiles['rock']      = world.colors['grey']
				world.tiles['sand']      = world.colors['sand']
				world.tiles['deep']      = world.colors['deep-blue']
				world.tiles['grass']     = world.colors['grass']
				world.tiles['obj']       = world.colors['fuchsia']
				world.tiles['cave']      = world.colors['dark']
				world.tiles['shallow']   = world.colors['shallow-blue']
				world.tiles['palm']      = world.colors['palm']
				world.tiles['tree']      = world.colors['tree']
			else:
				world.tiles['rock']      = world.colors['grey-night']
				world.tiles['sand']      = world.colors['sand-night']
				world.tiles['deep']      = world.colors['deep-blue-night']
				world.tiles['grass']     = world.colors['grass-night']
				world.tiles['obj']       = world.colors['fuchsia-night']
				world.tiles['cave']      = world.colors['dark-night']
				world.tiles['shallow']   = world.colors['shallow-blue-night']
				world.tiles['palm']      = world.colors['palm-night']
				world.tiles['tree']      = world.colors['tree-night']
			self.stepCount+=1
			#self.log.add_event(ginput)
			self.info.setTime(self.dayCount)
			Player.modifyHunger(-1)
			if self.stepCount==46:
				self.log.add_event("Uf... la ultima vez que camine tanto fue ese dia que fuimos de campamento con mi esposa. Recuerdo lo mucho que se reia al verme cojear mientras ella corria por las cuestas.")

			if self.dayCount>self.nightTimeLimit:
				pass

			if self.dayCount>self.dayCountLimit:
				self.dayCount=0
				self.log.increase_day()

				self.machine.changeState(self.log, self.ui)
				self.flag = False
			elif self.dayCount>4*self.dayCountLimit/5 and not self.flag:
				self.machine.changeState(self.log, self.ui)
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


	def killedByBear(self):
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
