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
        self.day_displayed = 0
        self.diary_index = 0
        self.diary = list()
        # Day zero
        self.diary.append(list())
        self.page = self.diary[0]
        self.page.append("banana")
        self.page.append("???")

        self.page.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")
        self.page.append("Lorem ipsum ad his scripta blandit partiendo, eum fastidii accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis reformidans eu, legimus senserit definiebas an eos.")

    def clean(self):
        for i in range(0, 11):
            empty_string = " "*63
            write(0, i, empty_string, self.window, 0)

    def draw(self):

        self.clean()
        write(1, 0, "<Dia "+str(self.day_displayed+1)+">", self.window, 0)
        i = self.diary_index
        index = 10
        while i < self.diary_index+10:
            color = 3
            if i >= len(self.page) or index < 1:
                break
            line = ">"+self.page[i]
            lines = parser(line, 62)

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
        self.page.insert(0, string)

    def increase_day(self):
        self.day += 1
        self.diary.append(list())
        self.page = self.diary[len(self.diary)-1]
        self.day_displayed = self.day

    def scroll_up(self):
        if (self.diary_index + 1) >= len(self.page):
            return
        else:
            self.diary_index += 1

    def scroll_down(self):
        if (self.diary_index - 1) < 0:
            return
        else:
            self.diary_index -= 1

    def next_day(self):
        day_index = self.day_displayed + 1
        if day_index >= len(self.diary):
            return
        else:
            self.page = self.diary[day_index]
            self.diary_index = 0
            self.day_displayed += 1

    def prev_day(self):
        day_index = self.day_displayed - 1
        if day_index < 0:
            return
        else:
            self.page = self.diary[day_index]
            self.diary_index = 0
            self.day_displayed -= 1

    def to_file(self):
        log_file = open("Wilson_log.txt", "w")
        for i in range(0, len(self.diary)):
            log_file.write("Day :"+str(i+1)+"\n")

            day = '\n'.join(map(str, self.diary[i]))

            log_file.write(day)
            log_file.write("\n\n")
        log_file.close()

def row_number(line):
        n = int(len(line) // 62)+1
        return n

def parser(line, line_size):

    size = len(line)
    len_size = line_size

    return_list = [line[i:i+len_size] for i in range(0, size, len_size)]

    return return_list

