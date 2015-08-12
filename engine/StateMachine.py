__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx2 import *
from Item import *
import time

class StateMachine:

    def __init__(self):
    	self.current_state = 0
        self.machine = dict()
        self.machine[0] = [1, ["Miro el mar desde la orilla de la playa. El olor del mar es penetrante y deja un sabor amargo en mi boca reseca.",
        					"Comienza la manana, acaba de amanecer y debo aprovechar la luz del dia para encontrar algo de comida..."]]
        self.machine[1] = [2, ["No he encontrado ningun refugio... es mejor pasar la noche despierto.",
        					"Me sorprende la cantidad de estrellas que se pueden ver desde aqui. Recuerdo la granja del abuelo, sus animales, sus vacas... sus cerdos... La sonrisa de la abuela al verme llegar, y su limonada. Como desearia poder tomar un poco de su limonada. Nunca aprendi a prepararla y me he arrepentido de ello desde el ultimo dia que la vi."]]
        self.machine[2] = [3, ["Jamas habia visto salir el sol por el mar. Es mas, no puedo recordar la ultima vez que vi salir el sol. Quizas fue cuando mi hijo era bebe y debia levantarme a darle su leche; quizas incluso antes.",
        "Seguire explorando la isla."]]
        self.machine[3] = [-1, ["Otro dia mas...He perdido la cuenta.", "El sol golpea mi curtida espalda."]]

    def changeState(self, log, ui):
    	if not self.current_state==-1:
            texts = self.machine[self.current_state][1]
            for text in texts:
                log.add_event(text)
                #ui.draw()
                #time.sleep(0.3)

            self.current_state = self.machine[self.current_state][0]
