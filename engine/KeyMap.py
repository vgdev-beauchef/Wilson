__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
from gfx import *


class KeyMap:
    def __init__(self, win_width, win_height):
        self.width = win_width / 2
        self.height = win_height / 2
        self.window = Ventana(self.width, self.height, self.width / 2, self.height)
        self.visible = False

    def draw(self):
        border_sides = "||" + " " * (2 * (self.width) - 5) + "||"
        for i in range(0, self.height):
            write(0, i, border_sides, self.window, 0)
        border = "[]" + "=" * (2 * (self.width) - 5) + "[]"
        write(0, 0, border, self.window, 0)
        write(0, self.height - 1, border, self.window, 0)

        # first column

        write(3, 2, "@ Personaje", self.window, 226)
        write(3, 3, u"\u2588 Roca", self.window, 95)
        write(3, 4, ". Arena", self.window, 227)
        write(3, 5, u"\u2248 Agua prof", self.window, 21)
        write(3, 6, u"\u0e45 Pasto", self.window, 83)

        # second column

        write(16, 2, "* Objeto", self.window, 129)
        write(16, 3, u"\u22d2 Cueva", self.window, 246)
        write(16, 4, "~ Agua", self.window, 124)
        write(16, 5, u"\u1f33 Palmera", self.window, 41)
        write(16, 6, u"\u1f34 Arbol", self.window, 29)

        # third column

        write(27, 2, "A Manzana", self.window, 197)
        write(27, 3, "J Jabali", self.window, 167)
        write(27, 4, "W Cuchillo", self.window, 248)
        write(27, 5, "X Relev. Obj", self.window, 162)

        return

    def refresh(self):
        self.window.refresh()

    def is_visible(self):
        return self.visible

    def visibility(self, state):
        if state:
            self.visible = True
        else:
            self.visible = False
