import StoryState
import world
import Player
import Log
import Inventory
import Item
import Story

survive_time = None
radio_time = None
survive_count = 0

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
            if not (inv.getItem(Item.getItemId('cuerda')) is None):
                Story.addItem(self.world, 'balsa')

        def woodNo():
            log.add_event("Solo haria bulto...")
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
            if not (inv.getItem(Item.getItemId('madera')) is None):
                Story.addItem(self.world, 'balsa')

        def ropeNo():
            log.add_event("Asi estare mas a salvo")
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

        ##################CONSTRUIR BALSA
        balsaCT = lambda day, step, x, y: posTrigger(x,y, Item.getAscii('balsa'), world)
        balsaCL = "Aun puedo construir la balsa con lo que tengo..."
        balsaCO = ("Que deberia hacer?","Construir","Reservar recursos")

        def balsaCFunY():
            log.add_event("No tengo nada mejor que hacer con estos recursos, mejor los uso")
            inv.deleteItem(Item.create('madera'))
            inv.deleteItem(Item.create('cuerda'))
            inv.addItem(Item.create('balsa'))
            self.add_event('final_balsa')

        def balsaCFunN():
            log.add_event("Puede que guardar estos recursos sea util despues...")

        balsaCY = lambda: balsaCFunY()
        balsaCN = lambda: balsaCFunN()
        self.allEvents['construir_balsa'] = StoryState.StoryState(balsaCL, balsaCT, balsaCO, balsaCY, balsaCN, None, None)

        ##################Balsa Final (acercarse a la orilla)

        balsaT = lambda day, step, x, y: posTrigger(x,y, '-', world)
        balsaL = "Podria usar la balsa para tratar de salir de aqui"
        balsaO = ("Que deberia hacer?","Zarpar","Quedarse")

        def balsaFunY():
            log.add_event("Me ire de aqui, estoy seguro de que encontrare a alguien. Ojala alguien mas pueda leer este diario algun dia...")
            self.info.gameFinal1()
            self.info.gameOver()

        def balsaFunN():
            log.add_event("Puede que sea sensato darme otra vuelta a ver si encuentro mas opciones")

        balsaY = lambda: balsaFunY()
        balsaN = lambda: balsaFunN()
        self.allEvents['final_balsa'] = StoryState.StoryState(balsaL, balsaT, balsaO, balsaY, balsaN, None, None)

        ###################fire_palm
        def fireTrigger(day, step, x, y):
            return posTrigger(x,y, Item.getAscii('palmera'), world) and (not inv.getItem(Item.getItemId('fuego')) is None)

        fire_palmTrigger = lambda day, step, x, y: fireTrigger(day, step, x, y)
        fire_palmLeyend = "Podria usar esta palmera como senyal de humo..."
        fire_palmOpt = ("Que deberia hacer?", "Prenderle fuego", "No hacerlo")

        def fire_palmYes():
            log.add_event("Con esto deberian lograr verme!!")
            self.info.gameOver()
            self.info.gameFinal2()
        def fire_palmNo():
            log.add_event("Es muy peligroso, buscare otras formas...")

        yesFun10 = lambda: fire_palmYes()
        noFun10 = lambda: fire_palmNo()
        self.allEvents['palmera']=StoryState.StoryState(fire_palmLeyend, fire_palmTrigger, fire_palmOpt, yesFun10, noFun10, None, None)

        ######Survive
        def survive(step):
            time = 20
            global survive_time
            if(survive_time is None):
                survive_time = step
                return False
            else:
                return survive_time+time == step

        surviveTrigger = lambda day, step, x, y: survive(step)
        surviveLeyend = "He sobrevivido mucho tiempo solo... creo que es momentos de tomar una decision"
        surviveOpt = ("Que deberia hacer?", "Usar lo obtenido", "Explorar")

        def surviveYes():
            log.add_event("Creo haber visto algo que puede servirme...")
            self.addEvent('palmera')
            Story.addItem(self.world, 'palmera')
            Story.addNewItem(self.world, 'comida', 70, 125)
            Story.addNewItem(self.world, 'comida', 100, 112)

        def surviveNo():
            global survive_count
            if(survive_count>1):
                log.add_event("A pesar de todos mis esfuerzos, nunca encontre nada en esta isla que me ayudase")
                self.info.gameOver()
            else:
                survive_count += 1
                log.add_event("Seguir explorando es lo mejor, aun me queda isla por recorrer")
                global survive_time
                survive_time = None

        yesFun11 = lambda: surviveYes()
        noFun11 = lambda: surviveNo()
        self.allEvents['sobrevivir']=StoryState.StoryState(surviveLeyend, surviveTrigger, surviveOpt, yesFun11, noFun11, None, None)

        ######Radio Survive
        def surviveR(step):
            time = 30
            global radio_time
            if(radio_time is None):
                radio_time = step
                return False
            else:
                if radio_time+(time/4)==step:
                    log.add_event("Esta radio esta sonando...")
                elif radio_time+(time/2)==step:
                    log.add_event("No se si mi mente aguante mucho mas... esta radio...")
                elif radio_time+(time*3/4)==step:
                    log.add_event("Me estoy volviendo loco!!")
                return radio_time+time == step

        surviveRTrigger = lambda day, step, x, y: surviveR(step)
        surviveRLeyend = "No aguanto mas!! debo hacer algo con esta radio!"
        surviveROpt = ("Que deberia hacer?", "Seguir", "Lanzarla")

        def surviveRYes():
            log.add_event("Debo seguir y encontrar una forma de recuperar mi sanidad, algo de calor deberia servir")
            self.addEvent('fuego')
            self.addEvent('palmera')
            Story.addItem(self.world, 'fuego')
            Story.addItem(self.world, 'palmera')
            Story.addNewItem(self.world, 'comida', 70, 125)

        def surviveRNo():
            log.add_event("A pesar de mis esfuerzos, no puedo mas...")
            self.info.gameOver()

        yesFun12 = lambda: surviveRYes()
        noFun12 = lambda: surviveRNo()
        self.allEvents['radio_survive']=StoryState.StoryState(surviveRLeyend, surviveRTrigger, surviveROpt, yesFun12, noFun12, None, None)

    def addEvent(self, name):
        self.currentEvents[name]=self.allEvents[name]

    def removeEvent(self, name):
        del self.currentEvents[name]

    def getCurrentList(self):
        return self.currentEvents.values()


