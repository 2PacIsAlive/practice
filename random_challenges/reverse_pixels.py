from pyprocessing import *

class iterationControl():
	def __init__(self):
		self.front = None
		self.back = None
	def setControls(self,front,back):
		self.front = front
		self.back = back
	def getControls(self):
		return self.front, self.back

def setup():
	#global frontIndex
	#global backIndex
	#backIndex = None
	global init
	init = True
	global pic
	pic = loadImage("assets/pixels_small.jpg")
	size(pic.width,pic.height)	
	global iterCtrl
	iterCtrl = iterationControl()
	global dir
	dir = 0

def draw():
	global init
	if init == True:
		global pic
		image(pic,0,0)
		loadPixels()
		global iterCtrl
		iterCtrl.setControls(0,(len(screen.pixels)-1))
		init = False
	else:
		global iterCtrl
		frontIndex, backIndex = iterCtrl.getControls()
		tmp = screen.pixels[frontIndex]
		screen.pixels[frontIndex] = screen.pixels[backIndex]
		screen.pixels[backIndex] = tmp
		global iterCtrl
		frontIndex, backIndex = iterCtrl.getControls()
		global dir
		if dir == 0:
			if frontIndex < (len(screen.pixels)-1)/2:
				frontIndex += 1
				backIndex -= 1
			else:
				frontIndex -= 1 
				backIndex += 1
				global dir
				dir = 1
		else:
			if frontIndex > 0:
				frontIndex -= 1
				backIndex += 1
			else:
				frontIndex += 1
				backIndex -= 1
				global dir
				dir = 0
		global iterCtrl
		iterCtrl.setControls(frontIndex,backIndex)
		updatePixels()

if __name__=="__main__":		
	run()
