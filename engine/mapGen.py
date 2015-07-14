import random


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
