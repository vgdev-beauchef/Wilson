import StoryState
import world
import Player
import Log
import Inventory
import Item

def posTrigger(px, py, target, world):
	pos=world.grid[px][py]
	return pos==target

def gotItemTrigger(itemPos, inv):
	return inv.getItem(itemPos) != None



class Story:
	def __init__(self, world, inv, dayLimit, log):
		self.initStoryState = self.createStory(world, inv, dayLimit, log)

	def createStory(self, world, inv, dayLimit, log):

		#######JABALI##############
		jabaliT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('b_jabali'), world)
		jabaliL = "Una cria de Jabali, si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...?"
		jabaliO = ("Que hacer?","Matarla","Dejarla Huir")

		def jabaliFunY():
			log.add_event("Su alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			self.inv.addItem(c)
			self.inv.addItem(c)


		jabaliY = lambda: jabaliFunY()
		jabaliN = lambda: log.add_event("Esta criatura no me ha hecho nada, nada le hare yo")		
		jabaliS = StoryState.StoryState(jabaliL, jabaliT, jabaliO, jabaliY, jabaliN, None, None)


		##########CUEVA##########
		cuevaT = lambda day, step, x, y: posTrigger(x,y, "O", world)
		cuevaL = "Una cria de Jabali, si la mato ahora tengo alimento facil, pero es tan solo un pequena criatura... como podria yo...?"
		cuevaO = ("Que hacer?","Matarla","Dejarla Huir")

		def jabaliFunY():
			log.add_event("Su alimento me ayudara a sobrevivir")
			c = Item.create('comida')
			self.inv.addItem(c)
			self.inv.addItem(c)


		cuevaY = lambda: jabaliFunY()
		cuevaN = lambda: log.add_event("Esta criatura no me ha hecho nada, nada le hare yo")		
		cuevaS = StoryState.StoryState(cuevaL, cuevaT, cuevaO, cuevaY, cuevaN, None, None)


		return jabaliS
