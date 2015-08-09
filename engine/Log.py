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
        self.diary.append("banana")
        self.diary.append("???")

        self.diary.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")
        self.diary.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")



    def draw(self):

        write(1, 0, "<Dia "+str(self.day)+">", self.window, 0)
        i = 0
        index = 10
        while i < 10:
            color = 3
            if i >= len(self.diary) or index < 1:
                break
            line = ">"+self.diary[i]
            lines = parser(line)

            rows = row_number(line)

            index -= rows
            if index < 1:
                break
            if i == 0:
                color = 4

            for sub_index in range(0, rows):
                write(1, index, lines[sub_index], self.window, color)
                index += 1

            index -= rows

            i += 1
            index -= 1


    def refresh(self):
        self.window.refresh()

    def add_event(self, string):
        self.diary.insert(string, 0)

    def increase_day(self):
        self.day += 1

def row_number(line):
        n = int(len(line) // 62)+1
        return n

def parser(line):

    size = len(line)
    len_size = 62

    return_list = [line[i:i+len_size] for i in range(0, size, len_size)]

    return return_list

