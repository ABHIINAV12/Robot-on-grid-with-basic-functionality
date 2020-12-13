import pygame
from factory.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK, BLUE, GREY, MACHINE, ROBOT, ROWS, COLS



class Piece:
	def __init__(self,row,col,obj):
		self.row=row
		self.col=col
		self.obj=obj
		self.x=0
		self.y=0
		self.calc_pos()

	def calc_pos(self):
		self.x=SQUARE_SIZE*self.col + SQUARE_SIZE//2
		self.y=SQUARE_SIZE*self.row + SQUARE_SIZE//2

	
	def draw(self,win):
		self.calc_pos()
		if self.obj=="ROBOT":
			win.blit(ROBOT,(self.x-ROBOT.get_width()//2, self.y-ROBOT.get_height()//2))
		else:
			win.blit(MACHINE,(self.x-MACHINE.get_width()//2, self.y-MACHINE.get_height()//2))

	def __repr__(self):
		return str(self.color)
 