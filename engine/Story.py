import StoryState
import world
import Player
import Log
import Inventory
import Item
import Events
import time

def posTrigger(px, py, target, world):
	pos=world.grid[px][py]
	return pos==target

def gotItemTrigger(itemPos, inv):
	return inv.getItem(itemPos) != None

def removeItem(world, itemName):
	px = Player.getPlayPos()[0]
	py = Player.getPlayPos()[1]
	replacement = Item.getReplacement(itemName, px, py)
	world.grid[px][py] = replacement

def addItem(world, itemName):
	pos = Item.getItemPos(itemName)
	replacement = Item.getAscii(itemName)
	world.grid[pos[0]][pos[1]] = replacement

def addNewItem(world, itemName, x, y):
	replacement = Item.getAscii(itemName)
	Item.addItem(itemName, x, y, world.grid[x][y])
	world.grid[x][y] = replacement



class Story:
	def __init__(self, world, inv, dayLimit, log, events, info):
		self.initStoryState = self.createStory(world, inv, dayLimit, log, events, info)

	def createStory(self, world, inv, dayLimit, log, events, info):

		#######JABALI##############
		jabaliT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('b_jabali'), world)
		jabaliL = "Una cria de Jabali, si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...?"
		jabaliO = ("Que hacer?","Matarla","Dejarla Huir")

		def jabaliFunY():
			log.add_event("Su alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			inv.addItem(c)
			inv.addItem(c)
			inv.clean()

			removeItem(world, 'b_jabali')
			Item.removeItem('b_jabali')
			Item.addItem('b_jabali', 78, 154, '/')
			addItem(world, 'b_jabali')

		def jabaliFunN():
			log.add_event("Esta criatura no me ha hecho nada, nada le hare yo")		
			events.addEvent('fuego')
			addItem(world, 'fuego')
			addItem(world, 'banana')
			events.addEvent('banana')
			removeItem(world, 'b_jabali')

		jabaliY = lambda: jabaliFunY()
		jabaliN = lambda: jabaliFunN()
		jabaliS = StoryState.StoryState(jabaliL, jabaliT, jabaliO, jabaliY, jabaliN, None, None)

		##########SEGUNDA CRIA JABALI############

		jabali2T = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('b_jabali'), world)
		jabali2L = "Otra cria de Jabali, seguire con mi desicion anterior?"
		jabali2O = ("Que hacer?","Matarla","Dejarla Huir")

		def jabali2FunY():
			log.add_event("Mas alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			inv.addItem(c)
			inv.addItem(c)
			inv.clean()
			events.addEvent('dead_man')
			addItem(world, 'dead_man')
			addItem(world, 'm_jabali')
			removeItem(world, 'b_jabali')
			Item.removeItem('b_jabali')

		def jabali2FunN():
			log.add_event("No soy capaz, no puedo hacerlo de nuevo")		
			events.addEvent('fuego')
			addItem(world, 'fuego')
			removeItem(world, 'b_jabali')
			Item.removeItem('b_jabali')
			Item.addNextFood(world)
			Item.addNextFood(world)

		jabali2Y = lambda: jabali2FunY()
		jabali2N = lambda: jabali2FunN()
		jabali2S = StoryState.StoryState(jabali2L, jabali2T, jabali2O, jabali2Y, jabali2N, None, None)

		########MAMA JABALI############

		jabaliMT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('m_jabali'), world)
		jabaliML = "La madre de las crias! sabe lo que hice... mis manos llenas de sangre me delatan!"
		jabaliMO = ("Que hacer?","Atacarla","Huir")

		def jabaliMFunY():
			if(inv.getItem(Item.getItemId('cuchillo')) is None):
				log.add_event("Esto fue demasiado para mi....", 197)
				info.gameOver()

			else:
				log.add_event("Eso fue facil... creo")
				c = Item.create('comida')
				inv.addItem(c)
				inv.addItem(c)
				inv.clean()

			removeItem(world, 'm_jabali')
			Item.removeItem('m_jabali')

		def jabaliMFunN():
			log.add_event("No quiero enfrentarme contra ella ahora, pero si necesito alimento se donde encontrarlo")		
			events.addEvent('m_jabali')
			Item.addNextFood(world)

		jabaliMY = lambda: jabaliMFunY()
		jabaliMN = lambda: jabaliMFunN()
		jabaliMS = StoryState.StoryState(jabaliML, jabaliMT, jabaliMO, jabaliMY, jabaliMN, None, None)


		##########CUEVA ENTRADA##########
		cuevaT = lambda day, step, x, y: posTrigger(x,y, "o", world)
		cuevaL = "Oh, una cueva!! Se escuchan ruidos desde adentro...sera algun animal??"
		cuevaO = ("Que deberia hacer?","Entrar","Huir")

		def cuevaFunY():
			log.add_event('Es mejor entrar, puede ser una buena oportunidad')
			events.removeEvent('cueva')

		def huirCueva():
			events.addEvent('cuerda')
			addItem(world, 'cuerda')
			events.addEvent('madera')
			addItem(world, 'madera')
			Item.addNextFood(world)
			Item.addNextFood(world)
			

		def cuevaFunN():
			log.add_event("No puedo arriesgarme... Es mejor que no siga")
			huirCueva()

		cuevaY = lambda: cuevaFunY()
		cuevaN = lambda: cuevaFunN()
		cuevaS = StoryState.StoryState(cuevaL, cuevaT, cuevaO, cuevaY, cuevaN, None, None)

		#############CUEVA INTERIOR#############

		cuevaIT = lambda day, step, x, y: posTrigger(x,y, "O", world)
		cuevaIL = "Entre a la cueva... Aparece un oso salvaje!"
		cuevaIO = ("Que deberia hacer?","Atacarlo","Huir")

		def cuevaIFunY():
			if(not inv.getItem(Item.getItemId('cuchillo')) is None):
				log.add_event("Logre matar a la bestia... al menos tendre comida")
				c = Item.create('comida')
				inv.addItem(c)
				inv.clean()
				addItem(world, 'radio')
				events.addEvent('radio_survive')
				Item.addNextFood(world)
				Item.addNextFood(world)
			elif(not inv.getItem(Item.getItemId('fuego')) is None):
				log.add_event("Logre ahuyentar al oso con el fuego")
				log.add_event("Y encontre comida para mi!")
				c = Item.create('comida')
				Item.addNextFood(world)
				Item.addNextFood(world)
				inv.addItem(c)
				inv.addItem(c)
				inv.clean()
				events.addEvent('sobrevivir')
			else:
				log.add_event("Esto fue demasiado para mi....", 197)
				info.gameOver()
			

		def cuevaIFunN():
			log.add_event("No me siento capaz de pelear contra una bestia como esa")
			huirCueva()

		cuevaIY = lambda: cuevaIFunY()
		cuevaIN = lambda: cuevaIFunN()
		cuevaIS = StoryState.StoryState(cuevaIL, cuevaIT, cuevaIO, cuevaIY, cuevaIN, None, None)

		###########CONSTRUIR BALSA

		balsaT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('balsa'), world)
		balsaL = "Ohh, con estos materiales mas la cuerda y madera que llevo podria construir una balsa"
		balsaO = ("Que deberia hacer?","Construir","Reservar")

		def balsaFunY():
			log.add_event("No tengo nada mejor que hacer con estos recursos, mejor los uso")
			events.addEvent('final_balsa')
			c = Item.create('balsa')
			inv.addItem(c)
			inv.deleteItem(Item.create('madera'))
			inv.deleteItem(Item.create('cuerda'))
			inv.clean()
			removeItem(world, 'balsa')


		def balsaFunN():
			log.add_event("Puede que guardar estos recursos sea util despues")
			events.addEvent('construir_balsa')

		balsaY = lambda: balsaFunY()
		balsaN = lambda: balsaFunN()
		balsaS = StoryState.StoryState(balsaL, balsaT, balsaO, balsaY, balsaN, None, None)

		###############RADIO

		radioT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('radio'), world)
		radioL = "Otra cueva, puede que no tenga tanta suerte como antes..."
		radioO = ("Que deberia hacer?","Entrar","Huir")

		def radioFunY():
			log.add_event("Increible, quien diria que encontraria respuestos para la radio")
			log.add_event("... ... .. Alo? ... ...")
			log.refresh()
			#time.sleep(1)
			log.add_event("... ...")
			log.refresh()
			#time.sleep(1)
			log.add_event("Si! Alo!? Vengan a recatarme!")
			info.gameOver()
			info.gameFinal3()


		def radioFunN():
			log.add_event("No creo correr tanta suerte dos veces")
			#log.add_event("Lo siento... No logre encontrar una salida...")
			#self.info.gameOver()
			#Because, because yes

		radioY = lambda: radioFunY()
		radioN = lambda: radioFunN()
		radioS = StoryState.StoryState(radioL, radioT, radioO, radioY, radioN, None, None)







		jabaliS.next_no_state=cuevaS
		jabaliS.next_yes_state=jabali2S

		jabali2S.next_no_state=cuevaS
		jabali2S.next_yes_state=jabaliMS

		jabaliMS.next_yes_state=cuevaS
		jabaliMS.next_no_state=cuevaS

		cuevaS.next_yes_state=cuevaIS
		cuevaS.next_no_state=balsaS

		cuevaIS.next_no_state=balsaS
		cuevaIS.next_yes_state=radioS

		return jabaliS
