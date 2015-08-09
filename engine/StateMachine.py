__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"
from gfx import *
from Item import *
import time

class StateMachine:

    def __init__(self):
    	self.current_state = 0
        self.machine = dict()
        self.machine[0] = [1, ["Miro el mar desde la orilla de la playa. El olor del mar es penetrante y deja un sabor amargo en mi boca reseca.",
        					"Comienza la manana, acaba de amanecer y debo aprovechar la luz del dia para encontrar algo de comida..."]]
        self.machine[1] = [2, ["No he encontrado ningun refugio... es mejor pasar la noche despierto.",
        					"Me sorprende la cantidad de estrellas que se pueden ver desde aqui.",
        					"Recuerdo la granja del abuelo, sus animales, sus vacas... sus cerdos... La primera manana en que mi abuelo me entrego ese oxidado azadon y me llevo a cosechar con el, el sudor de mi frente y la sonrisa de la abuela al verme regresar lleno de tierra. Como desearia poder tomar un poco de su limonada. Nunca aprendi a prepararla y me he arrepentido de ello desde el ultimo dia que la vi."]]
        self.machine[2] = [3, ["Jamas habia visto salir el sol por el mar. Es mas, no puedo recordar la ultima vez que vi salir el sol. Quizas fue cuando mi hijo era bebe y debia levantarme a darle su leche; quizas incluso antes.",
        "Seguire explorando la isla."]]
        self.machine[3] = [4, ["El olor de la cueva me recuerda a los enormes perros que cuidaban las ovejas de mi abuelo y como yo dormia abrazado a ellos. Casi puedo sentir su agradable calor."]]
        self.machine[4] = [5, ["Otro dia mas...He perdido la cuenta.", "El sol golpea mi curtida espalda."]]
        self.machine[5] = [-1, ["He vuelto a la costa con mi balsa. Me ire de aqui porque estoy seguro de que encontrare a alguien. Ojala alguien mas que yo pueda leer este diario algun dia..."]]

    def changeState(self, log):
    	if not self.current_state==-1:
            texts = self.machine[self.current_state][1]
            for text in texts:
                log.add_event(text)

            self.current_state = self.machine[self.current_state][0]