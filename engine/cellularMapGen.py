import random
_chanceToStartAlive = 0.4
deathLimit = 3
birthLimit = 4
numberOfSteps = 4


def initialiseMap(grid):
    width = len(grid)
    height = len(grid[0])

    for i in range(0, width):
        for j in range(0, height):
            if random.random() < _chanceToStartAlive:
                grid[i][j] = True

    return grid


def doSimulationStep(oldGrid):
    width = len(oldGrid)
    height = len(oldGrid[0])

    newGrid = [[0 for x in range(width)] for x in range(height)]

    for x in range(width):
        for y in range(height):
            nbs = countAliveNeighbours(oldGrid, x, y)
            if oldGrid[x][y]:
                if nbs < deathLimit:
                    newGrid[x][y] = False
                else:
                    newGrid[x][y] = True
            else:
                if nbs > birthLimit:
                    newGrid[x][y] = True
                else:
                    newGrid[x][y] = False
    return newGrid


def countAliveNeighbours(grid, x, y):
    width = len(grid)
    height = len(grid[0])

    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbour_x = x + i
            neighbour_y = y + j
            if i == 0 and j == 0:
                pass
            elif neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= width or neighbour_y >= height:
                count += 1
            elif grid[neighbour_x][neighbour_y]:
                count += 1
    return count


def generateMap(width, height):
    gridMap = [[0 for x in range(width)] for x in range(height)]
    gridMap = initialiseMap(gridMap)
    for i in range(0, numberOfSteps):
        gridMap = doSimulationStep(gridMap)
    for x in range(0, width):
        for y in range(0, height):
            if gridMap[x][y]:
                gridMap[x][y] = '.'
            else:
                gridMap[x][y] = '#'
    return gridMap
