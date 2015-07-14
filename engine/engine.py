import curses
import gfx
import sys, traceback
class gameEngine(object):
	def __init__(self):
		self.world_window = curses.newwin(0, 0, 25, 25)
		self.log_window = curses.newwin(26, 0, 5, 25)
		self.

	def play(self):