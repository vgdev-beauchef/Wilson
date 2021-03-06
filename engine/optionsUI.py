from Log import parser
from gfx import *

_opeWindowWidth = 10
_opeWindowHeight = 10
_opeWindowXPos = 33
_openWindowYPos = 20

class optionsUI(object):
	def __init__(self):
		self.window = Ventana(_opeWindowWidth, _opeWindowHeight,
							  _opeWindowXPos, _openWindowYPos)
		self.intro = ''
		self.yesOption = ''
		self.noOption = ''


	def draw(self):

		header = parser(self.intro, 20)
		line = 0

		for string in header:
			write(0, line, string, self.window, 0)
			line += 1

		line += 1

		if not self.yesOption=="":
			self.updateOption('(y)'+ self.yesOption, line)
			self.updateOption('(n)' + self.noOption, line + 2)

		self.window.refresh()

	def updateOption(self, string, pos):
		write(0, pos, string, self.window, 0)

	def setOption(self, a, b, c):
		self.intro = a
		self.yesOption = b
		self.noOption = c

	def clearWindow(self):
		clean_string = " " * 19
		for i in range(10):
			write(0,i,clean_string,self.window,0)
