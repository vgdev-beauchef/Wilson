__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"

class LinearStateMachine:

    class LinearState:
        def __init__(self, trigger, message, next_stage):
            self.trigger = trigger
            self.message = message
            self.next_stage = next_stage

    def __init__(self, dayLimit):
        self.dayLimit = dayLimit
        secondState = self.LinearState(lambda x: self.timeTrigger(x, 20), "Hola, la maquina funciona de nuevo", None) 
        firstState = self.LinearState(lambda x: self.timeTrigger(x, 10), "Hola, la maquina funciona", secondState)
        self.state = firstState

    def timeTrigger(self, currentTime, triggerTime):
        return currentTime==triggerTime

    def changeState(self, step, log):
        if(not self.state==None and self.state.trigger(step)):
            log.add_event(self.state.message)
            self.state = self.state.next_stage