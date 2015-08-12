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



class Story:
	def __init__(self, world, inv, dayLimit, log):
		self.initStoryState = self.createStory(world, inv, dayLimit, log)
		self.initEventState = self.createEvents(world, inv, dayLimit, log)

	def createStory(self, world, inv, dayLimit, log):
		trigger1 = lambda day, step, x, y: posTrigger(x,y, "-", world)
		leyend1 = "La orilla... se ve calmada"
		op1 = ("Seguir en el agua?","Claro","Obvio que no")

		yesFun1 = lambda: log.add_event("Decidi seguir en el agua")
		noFun1 = lambda: log.add_event("Corre!!!")
		state1 = StoryState.StoryState(leyend1, trigger1, op1, yesFun1, noFun1, None, None)

		return state1

	def createEvents(self, world, inv, dayLimit, log):
		foodTrigger = lambda day, step, x, y: posTrigger(x,y, "a", world)
		foodLeyend = "Ohh... Una manzana!"
		foodOpt = ("Que hago con la manzana?", "Guardarla", "Comerla")

		def common(text):
			log.add_event(text)
			c = Item.Item('comida',1,'0')
			inv.addItem(c)
			removeItem(80,170,world,'.')

		def yes():
			common('Guarde la manzana')
			
		def no():
			common('Comi la manzana')			
			Player.useItem(c, inv)			

		yesFun1 = lambda: yes()
		noFun1 = lambda: no()

		state1 = StoryState.StoryState(foodLeyend, foodTrigger, foodOpt, yesFun1, noFun1, None, None)
		states = []
		states.append(state1)
		return states