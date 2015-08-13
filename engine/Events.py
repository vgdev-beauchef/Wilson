import StoryState
import world
import Player
import Log
import Inventory
import Item
import Story

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
    def __init__(self, world, inv, dayLimit, log, info):
        self.info = info
        self.world = world
        self.allEvents = dict()
        self.createEvents(world, inv, dayLimit, log)
        self.currentEvents = dict()
        self.initEvents()

    def initEvents(self):
        self.addEvent('comida')
        self.addEvent('cueva')


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
        fireTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('fuego'), world)
        fireLeyend = "Eso es... Fuego?"
        fireOpt = ("Que deberia hacer?", "Tomarlo", "Apagarlo")

        def fireYes():
            log.add_event("Esto me sera muy util")
            c = Item.create('fuego')
            inv.addItem(c)
            removeItem(world,'fuego')

        def fireNo():
            log.add_event("Esto podria generar problemas...")
            removeItem(world,'fuego')

        yesFun2 = lambda: fireYes()
        noFun2 = lambda: fireNo()
        self.allEvents['fuego']=StoryState.StoryState(fireLeyend, fireTrigger, fireOpt, yesFun2, noFun2, None, None)

        ###################BANANA
        bananaTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('banana'), world)
        bananaLeyend = "Mira! Un ramo de bananas"
        bananaOpt = ("Que deberia hacer?", "Guardarla", "Comerla")

        def bananaYes():
            log.add_event("Guarde la banana para despues")
            c = Item.create('comida')
            inv.addItem(c)
            removeItem(world,'banana')

        def bananaNo():
            log.add_event("Comi la banana que encontre")
            c = Item.create('comida')
            inv.addItem(c)
            removeItem(world,'banana')
            Player.useItem(c, inv)

        yesFun3 = lambda: bananaYes()
        noFun3 = lambda: bananaNo()
        self.allEvents['banana']=StoryState.StoryState(bananaLeyend, bananaTrigger, bananaOpt, yesFun3, noFun3, None, None)

        ###################boar
        boarTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('m_jabali'), world)
        boarLeyend = "Otra vez la madre!"
        boarOpt = ("Que deberia hacer?", "Atacarla", "Huir")

        def boarYes():
            if inv.getItem(Item.getItemId('cuchillo')) is None:
                #TODO Killed
                log.add_event("Esto fue demasiado para mi....", 197)
                self.info.gameOver()
            else:
                log.add_event("Por fin murio...")
                c = Item.create('comida')
                inv.addItem(c)
                inv.addItem(c)
                inv.addItem(c)
                removeItem(world,'m_jabali')

        def boarNo():
            log.add_event("Sera mejor que huya")

        yesFun4 = lambda: boarYes()
        noFun4 = lambda: boarNo()
        self.allEvents['m_jabali']=StoryState.StoryState(boarLeyend, boarTrigger, boarOpt, yesFun4, noFun4, None, None)

        ###################deadman
        dmTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('dead_man'), world)
        dmLeyend = "Es un cadaver...?"
        dmOpt = ("Que deberia hacer?", "Acercarme", "Dejarlo en paz")

        def dmYes():
            log.add_event("Hey! Tiene un cuchillo")
            c = Item.create('cuchillo')
            inv.addItem(c)
            removeItem(world,'dead_man')

        def dmNo():
            log.add_event("Espero no terminar asi...")
            removeItem(world,'dead_man')

        yesFun5 = lambda: dmYes()
        noFun5 = lambda: dmNo()
        self.allEvents['dead_man']=StoryState.StoryState(dmLeyend, dmTrigger, dmOpt, yesFun5, noFun5, None, None)

        ###################wood
        woodTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('madera'), world)
        woodLeyend = "Encontre madera!"
        woodOpt = ("Que deberia hacer?", "Tomarla", "Dejarla ahi")

        def woodYes():
            log.add_event("Esto me servira para muchas cosas...")
            c = Item.create('madera')
            inv.addItem(c)
            removeItem(world,'madera')

        def woodNo():
            log.add_event("Solo haria vulto...")
            removeItem(world,'madera')

        yesFun6 = lambda: woodYes()
        noFun6 = lambda: woodNo()
        self.allEvents['madera']=StoryState.StoryState(woodLeyend, woodTrigger, woodOpt, yesFun6, noFun6, None, None)

        ###################rope
        ropeTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('cuerda'), world)
        ropeLeyend = "Es una serpiente...?"
        ropeOpt = ("Que deberia hacer?", "Acercarse", "Alejarse")

        def ropeYes():
            log.add_event("Es una cuerda! Que suerte tengo")
            c = Item.create('cuerda')
            inv.addItem(c)
            removeItem(world,'cuerda')

        def ropeNo():
            log.add_event("Asi estare mas asalvo")
            removeItem(world,'cuerda')

        yesFun7 = lambda: ropeYes()
        noFun7 = lambda: ropeNo()
        self.allEvents['cuerda']=StoryState.StoryState(ropeLeyend, ropeTrigger, ropeOpt, yesFun7, noFun7, None, None)

        ###################cave
        caveTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('cueva'), world)
        caveLeyend = "Una cueva."
        caveOpt = ("Que deberia hacer?", "Mirare dentro", "Alejarse")

        def caveYes():
            log.add_event("No hay nada interesante aqui...")

        def caveNo():
            log.add_event("Vere si hay algo mas interesante en otro lado..")

        yesFun8 = lambda: caveYes()
        noFun8 = lambda: caveNo()
        self.allEvents['cueva']=StoryState.StoryState(caveLeyend, caveTrigger, caveOpt, yesFun8, noFun8, None, None)

        ###################radio
        radioTrigger = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('radio'), world)
        radioLeyend = "Aquello no es la pieza que necesito?"
        radioOpt = ("Que deberia hacer?", "Entrar por ella", "Debo estar loco...")

        def radioYes():
            log.add_event("Si! Esto me sacara de aqui!")
            c = Item.create('radio')
            inv.addItem(c)
            removeItem(world,'radio')
        def radioNo():
            log.add_event("Me pregunto si habra otra forma de arreglar ese aparato...")
            removeItem(world,'radio')

        yesFun9 = lambda: radioYes()
        noFun9 = lambda: radioNo()
        self.allEvents['radio']=StoryState.StoryState(radioLeyend, radioTrigger, radioOpt, yesFun9, noFun9, None, None)

    def addEvent(self, name):
        self.currentEvents[name]=self.allEvents[name]

    def removeEvent(self, name):
        del self.currentEvents[name]

    def getCurrentList(self):
        return self.currentEvents.values()


