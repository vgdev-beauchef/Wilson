__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from gfx import *

class Log:

    def __init__(self):
        self.width = 32
        self.height = 11
        self.xPos = 0
        self.yPos = 19
        self.window = Ventana(self.width, self.height, self.xPos, self.yPos)
        self.day = 0
        self.diary = list()
        self.diary.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")
        self.diary.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")
        self.diary.append("banana")
        self.diary.append("???")
        self.diary.append("???")


    def draw(self):
        log = ['%' * self.width] * self.height
        for i in range(len(log[0])):
            for j in range(len(log)):
                draw(i, j, '%', self.window, 5)
        write(1,0, "<Dia "+str(self.day)+">", self.window, 0)
        i = 0
        index = 10
        color = 3
        while i < 10:
            if i >= len(self.diary) or index < 1:
                break;
            line = self.diary[i]
            rows = self.row_number(line)
            index -= rows
            if index < 1:
                break;
            if i == 0:
                write(1, index, line, self.window, 4)
            else:
                write(1, index, line, self.window, color)
            i += 1
            index -= 1


    def refresh(self):
        self.window.refresh()

    def add_event(self, string):
        self.diary.insert(string, 0)

    def row_number(self, line):
        n = int(len(line) // 62)
        return n

    def increase_day(self):
        self.day += 1

