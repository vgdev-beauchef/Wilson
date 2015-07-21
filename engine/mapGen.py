import random
import noise
import time


def mapGenerator(width, height):
    grid = []
    for i in range(width):
        fila = []
        for j in range(height):
            n = random.randint(1, 100)
            if n <= 30:
                fila.append('#')
            else:
                fila.append('.')
        grid.append(fila)
    return grid


def mapGenerator2(width, height):
    grid = []
    for i in range(width):
        fila = []
        for j in range(height):
            x = (i*1.0)/width
            y = (j*1.0)/height

            seed = random.random()
            seed2 = random.randint(10, 250)

            n = noise.pnoise2(
                seed2*x+10, 10*y, 1, 0.5, 0.2, 1024, 1024, 0)*1.5+0.6

            # if n == 0.0:
            #     fila.append('/')

            if n < 0.15:
                fila.append('~')
            elif n >= 0.15 and n < 0.6:
                fila.append('.')
            elif n >= 0.75:
                fila.append('#')

        grid.append(fila)
    return grid