from gfx import *
import sys, traceback
import world, Player
class UI:
	def __init__(self):
		self.world = world.World(50, 50)
		self.log = Ventana(20, 5, 0, 21)
		self.info = Ventana(20, 40, 21, 0)

	def movement(self, ginput):
		if ginput == 'left':
			self.world.player.position[0] -= 1
		elif ginput == 'right':
			self.world.player.position[0] += 1
		elif ginput == 'up':
			self.world.player.position[1] -= 1
		elif ginput == 'down':
			self.world.player.position[1] += 1

if __name__ == '__main__':
	try:
		start()
		ui = UI()
		while 1:
			ui.world.drawMap()

			#LOG
			log = ['%'*20]*5
			for i in range(len(log[0])):
						for j in range(len(log)):
							draw(i, j, '%', ui.log)
			#INFO
			info = ['$'*20]*26
			for i in range(len(info[0])):
						for j in range(len(info)):
							draw(i, j, '$', ui.info)
			ui.log.refresh()
			ui.info.refresh()

			#INPUT
			q = get_input()
			if q == 'q': break
			ui.movement(q)
		stop()
	except:
		stop()
		print (traceback.format_exc())
		sys.exit(-1)