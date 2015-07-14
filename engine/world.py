from Player import Player
import gfx, mapGen
import random
class World(object):
	def __init__(self, width, height):
		self.grid = mapGen.mapGenerator(width, height)
		self.window = gfx.Ventana(20, 20)
		self.player = Player('')

	def drawMap(self):
		xCenter = self.player.position[0]
		yCenter = self.player.position[1]

		w = self.window.width
		h = self.window.height

		iniX = xCenter - w/2

		for i in range(w):
			iniY = yCenter - w/2
			for j in range(h):
				if iniX >= 0 and iniY >= 0 and\
				   iniX <= self.window.width and iniY <= self.window.height:
					cha = self.grid[iniX][iniY]
				else:
					cha = 'X'

				if i == w/2 and j == h/2:
					cha = '@'

				self.window.addch(i, j, cha)
				iniY += 1
			iniX += 1
		self.window.refresh()
