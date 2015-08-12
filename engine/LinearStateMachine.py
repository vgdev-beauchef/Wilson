__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"

class LinearStateMachine:

    class LinearState:
        def __init__(self, trigger, message, next_stage):
            self.trigger = trigger
            self.message = message
            self.next_stage = next_stage

    def __init__(self, dayLimit):

        messages= ["Miro el mar desde la orilla de la playa. Su olor es penetrante y deja un sabor amargo en mi boca reseca.",
            "Comienza la manana, acaba de amanecer y debo aprovechar la luz del dia para encontrar algo de comida...",
            "No he encontrado ningun refugio... es mejor pasar la noche despierto.",
            "Me sorprende la cantidad de estrellas que se pueden ver desde aqui. Recuerdo la granja del abuelo, sus animales, sus vacas... sus cerdos... La sonrisa de la abuela al verme llegar, y su limonada. Como desearia poder tomar un poco de su limonada. Nunca aprendi a prepararla y me he arrepentido de ello desde el ultimo dia que la vi.",
            "Jamas habia visto salir el sol por el mar. Es mas, no puedo recordar la ultima vez que vi salir el sol. Quizas fue cuando mi hijo era bebe y debia levantarme a darle su leche; quizas incluso antes.",
            "Seguire explorando la isla.",
            "Otro dia mas...He perdido la cuenta.",
            "El sol golpea mi curtida espalda."]

        limits = [1, 5, dayLimit-10, dayLimit-6, dayLimit+1, dayLimit+5,  (dayLimit*2)-10, (dayLimit*2)-6]

        states = []
        states.append(self.LinearState(lambda x: self.timeTrigger(x, limits[len(limits)-1]), messages[len(messages)-1], None))
        for i in range(1, len(messages)):
            k = limits[len(limits)-1-i]
            states.append(self.LinearState(lambda x, k=k: self.timeTrigger(x, k), messages[len(messages)-1-i], states[len(states)-1]))

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
