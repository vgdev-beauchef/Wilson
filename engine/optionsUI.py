from gfx import *

_opeWindowWidth = 10
_opeWindowHeight = 10
_opeWindowXPos = 33
_openWindowYPos = 20

class optionsUI(object):
	def __init__(self):
		self.window = Ventana(_opeWindowWidth,_opeWindowHeight,_opeWindowXPos,_openWindowYPos)


	def writeOptions(intro,y_string,n_string):

		header = parser(intro, 20)
		line = 0

		for str in header
			write(0,line,str,self.window,0)
			line += 1

		line += 1
		setOption('(Y)'+ y_string,line)
		setOption('(N)' + n_string,line+2)

	def setOption(string, pos):
		write(0,pos,string,self.window,0)



	def clearWindow():
		clean_string = " " * 20
		for i in range(10):
			write(0,i,clean_string,self.window,0)