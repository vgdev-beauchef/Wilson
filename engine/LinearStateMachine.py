__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"

class LinearStateMachine:

    class LinearState:
        def __init__(self, trigger, message, next_stage):
            self.trigger = trigger
            self.message = message
            self.next_stage = next_stage


    def __init__(self, dayLimit):

        tuples = [("Miro el mar desde la orilla de la playa. Su olor es penetrante y deja un sabor amargo en mi boca reseca.", 1),
            ("Comienza la manana, acaba de amanecer y debo aprovechar la luz del dia para encontrar algo de comida...", 5),
            ("No he encontrado ningun refugio... es mejor pasar la noche despierto.", dayLimit-10),
            ("Me sorprende la cantidad de estrellas que se pueden ver desde aqui. Recuerdo la granja del abuelo, sus animales, sus vacas... sus cerdos... La sonrisa de la abuela al verme llegar, y su limonada. Como desearia poder tomar un poco de su limonada. Nunca aprendi a prepararla y me he arrepentido de ello desde el ultimo dia que la vi.", dayLimit-6), 
            ("Jamas habia visto salir el sol por el mar. Es mas, no puedo recordar la ultima vez que vi salir el sol. Quizas fue cuando mi hijo era bebe y debia levantarme a darle su leche; quizas incluso antes.", dayLimit+1),
            ("Seguire explorando la isla.", dayLimit+5), 
            ("Otro dia mas...He perdido la cuenta.", (dayLimit*2)-10), 
            ("El sol golpea mi curtida espalda.", (dayLimit*2)-6),
            ("Uf... la ultima vez que camine tanto fue ese dia que fuimos de campamento con mi esposa. Recuerdo lo mucho que se reia al verme cojear mientras ella corria por las cuestas.", 46)]

        tuples.sort(key=lambda tup: tup[1])

        states = []
        states.append(self.LinearState(lambda x: self.timeTrigger(x, tuples[len(tuples)-1][1]), tuples[len(tuples)-1][0], None))
        for i in range(1, len(tuples)):
            k = tuples[len(tuples)-1-i][1]
            states.append(self.LinearState(lambda x, k=k: self.timeTrigger(x, k), tuples[len(tuples)-1-i][0], states[len(states)-1]))

        #secondState = self.LinearState(lambda x: self.timeTrigger(x, 20), "Hola, la maquina funciona de nuevo", None) 
        #firstState = self.LinearState(lambda x: self.timeTrigger(x, 10), "Hola, la maquina funciona", secondState)
        self.state = states[len(states)-1]

    def timeTrigger(self, currentTime, triggerTime):
        return currentTime==triggerTime

    def changeState(self, step, log):
        if(not self.state==None and self.state.trigger(step)):
            log.add_event(self.state.message)
            self.state = self.state.next_stage
        #if(not self.state == None):
            #log.add_event(self.state.message)
