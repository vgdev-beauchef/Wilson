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

def removeItem(world, itemName):
	px = Player.getPlayPos()[0]
	py = Player.getPlayPos()[1]
	replacement = Item.getReplacement(itemName, px, py)
	world.grid[px][py] = replacement

class Events:
	def __init__(self, world, inv, dayLimit, log):
		self.allEvents = dict()
		self.createEvents(world, inv, dayLimit, log)
		self.initEventState = self.initEvents()

	def initEvents(self):
		e = []
		e.append(self.allEvents['comida'])

		return e


	def createEvents(self, world, inv, dayLimit, log):

		############COMIDA################
		foodTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('comida'), world)
		foodLeyend = "Ohh... Una manzana!"
		foodOpt = ("Que hago con la manzana?", "Guardarla", "Comerla")

		def foodYes():
			log.add_event("Guarde el alimento para despues")
			c = Item.create('comida')
			inv.addItem(c)
			removeItem(world,'comida')
			
		def foodNo():
			log.add_event("Comi la manzana que encontre")
			c = Item.create('comida')
			inv.addItem(c)
			removeItem(world,'comida')	
			Player.useItem(c, inv)			

		yesFun1 = lambda: foodYes()
		noFun1 = lambda: foodNo()


		self.allEvents['comida']=StoryState.StoryState(foodLeyend, foodTrigger, foodOpt, yesFun1, noFun1, None, None)

		###################FUEGO

	def addEvent(name):
		return

	def removeEvent(name):
		return


