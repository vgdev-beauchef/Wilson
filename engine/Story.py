import StoryState
import world
import Player
import Log
import Inventory
import Item
import Events

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



class Story:
	def __init__(self, world, inv, dayLimit, log, events):
		self.initStoryState = self.createStory(world, inv, dayLimit, log, events)

	def createStory(self, world, inv, dayLimit, log, events):

		#######JABALI##############
		jabaliT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('b_jabali'), world)
		jabaliL = "Una cria de Jabali, si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...?"
		jabaliO = ("Que hacer?","Matarla","Dejarla Huir")

		def jabaliFunY():
			log.add_event("Su alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			inv.addItem(c)
			inv.addItem(c)
			removeItem(world, 'b_jabali')

		def jabaliFunN():
			log.add_event("Esta criatura no me ha hecho nada, nada le hare yo")		
			#events.addEvent('fuego')
			addItem(world, 'fuego')
			addItem(world, 'banana')
			#events.addEvent('banana')
			removeItem(world, 'b_jabali')

		jabaliY = lambda: jabaliFunY()
		jabaliN = lambda: jabaliFunN()
		jabaliS = StoryState.StoryState(jabaliL, jabaliT, jabaliO, jabaliY, jabaliN, None, None)


		##########CUEVA##########
		cuevaT = lambda day, step, x, y: posTrigger(x,y, "O", world)
		cuevaL = "Una cria de Jabali, si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...?"
		cuevaO = ("Que hacer?","Matarla","Dejarla Huir")

		def jabaliFunY():
			log.add_event("Su alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			inv.addItem(c)
			inv.addItem(c)



		cuevaY = lambda: jabaliFunY()
		cuevaN = lambda: log.add_event("Esta criatura no me ha hecho nada, nada le hare yo")		
		cuevaS = StoryState.StoryState(cuevaL, cuevaT, cuevaO, cuevaY, cuevaN, None, None)


		return jabaliS
