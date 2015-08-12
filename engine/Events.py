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

def removeItem(gridPosX,gridPosY, world, replacement):
	world.grid[gridPosX][gridPosY] = replacement

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
		foodTrigger = lambda day, step, x, y: posTrigger(x,y, "a", world)
		foodLeyend = "Ohh... Una manzana!"
		foodOpt = ("Que hago con la manzana?", "Guardarla", "Comerla")

		def foodYes():
			log.add_event("Guarde el alimento para despues")
			c = Item.Item('comida',1,'0')
			inv.addItem(c)
			removeItem(80,170,world,'.')
			
		def foodNo():
			log.add_event("Comi la manzana que encontre")
			c = Item.Item('comida',1,'0')
			inv.addItem(c)
			removeItem(80,170,world,'.')		
			Player.useItem(c, inv)			

		yesFun1 = lambda: foodYes()
		noFun1 = lambda: foodNo()


		self.allEvents['comida']=StoryState.StoryState(foodLeyend, foodTrigger, foodOpt, yesFun1, noFun1, None, None)

		###################FUEGO



