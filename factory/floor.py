import pygame
from .constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK, BLUE, GREY, ROWS, COLS
from .piece import Piece


class Floor:
	def __init__(self):
		self.floor=[]
		self.starting_row,self.ending_row=21,60
		self.starting_col1,self.ending_col1=11,30
		self.starting_col2,self.ending_col2=51,70
		self.create_floor()
		

	def draw_floor(self,win):
		win.fill(BLACK)
		for row in range (ROWS):
			for col in range(row%2,ROWS,2):
				pygame.draw.rect(win,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
		for row in range (ROWS):
			for col in range(COLS):
				if(row>=self.starting_row and row<=self.ending_row) and((col>=self.starting_col1 and col<=self.ending_col1) or (col>=self.starting_col2 and col<=self.ending_col2)):
					pygame.draw.rect(win,BLUE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

	def create_floor(self):
		for row in range (ROWS):
			self.floor.append([])
			for col in range(COLS):
				if(row==0 and col==0):
					self.floor[row].append(Piece(row,col,"ROBOT"))
				elif(row>=self.starting_row and row<=self.ending_row) and((col>=self.starting_col1 and col<=self.ending_col1) or (col>=self.starting_col2 and col<=self.ending_col2)):
					self.floor[row].append(1)	
				else:
					self.floor[row].append(0)

	def draw(self,win):
		self.draw_floor(win)
		for row in range (ROWS):
			for col in range(COLS):
				piece=self.floor[row][col]
				if (piece!=0 and piece!=1):
					piece.draw(win)

	def get_robo_cor(self):
		for row in range (ROWS):
			for col in range(COLS):
				if(self.floor[row][col]!=0 and self.floor[row][col]!=1):
					return [row,col]
		return [0,0]
	
	def inplace(self,col,row):
		if(row>=0 and row<ROWS and col>=0 and col<COLS):
			if(row>=self.starting_row and row<=self.ending_row) and((col>=self.starting_col1 and col<=self.ending_col1) or (col>=self.starting_col2 and col<=self.ending_col2)):
				return False
			return True
		return False

	def move_from_to(self,row,col,new_row,new_col):
		self.floor[row][col]=0
		#print(row,col,new_row,new_col)
		self.floor[new_row][new_col]=Piece(new_row,new_col,"ROBOT")
				
	
	
	
	
	