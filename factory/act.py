import pygame
from .constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK, BLUE, GREY, ROWS, COLS
from .floor import Floor
from collections import defaultdict

class Act:
	def __init__(self,win):
		self.win=win
		self._init()
		
	def update(self):
		self.floor.draw(self.win)
		self.draw_valid_moves(self.valid_moves)
		pygame.display.update()

	def _init(self):	
		self.selected=None
		self.floor=Floor()
		self.valid_moves={}
		self.update()
		
	def reset(self):
		self._init()

	
	def draw_valid_moves(self,moves):
		for move in moves:
			row,col=move
			pygame.draw.circle(self.win,BLUE,(col*SQUARE_SIZE + SQUARE_SIZE//2,row*SQUARE_SIZE + SQUARE_SIZE//2),2)


	def get_floor(self):
		return self.floor

	def move_robot(self,dx,dy):
		cor=self.floor.get_robo_cor()
		new_row=cor[0]+dx
		new_col=cor[1]+dy
		print(cor[0],cor[1],new_row,new_col)
		if(self.floor.inplace(new_row,new_col)):
			self.floor.move_from_to(cor[0],cor[1],new_row,new_col)
		self.update()

	def teleport(self,row,col):
		if(self.floor.inplace(row,col)):
			cor=self.floor.get_robo_cor()
			vis=[]
			for row1 in range (ROWS):
				temp=[]
				for col1 in range (COLS):
					temp.append(False)
				vis.append(temp)
			par=[]
			for row1 in range (ROWS):
				tmp=[]
				for col1 in range (COLS):
					tmp.append([-1,-1])
				par.append(tmp)
			dx = [0,0,-1,1]
			dy = [-1,1,0,0]
			sx,sy=cor[0],cor[1]
			stack=[]
			vis[sx][sy]=True
			stack.append([sx,sy])
			while (len(stack)):
				fp=stack[0]
				stack.pop(0)
				for i in range (0,4):
					tmpx=fp[0]+dx[i]
					tmpy=fp[1]+dy[i]
					if(self.floor.inplace(tmpx,tmpy) and vis[tmpx][tmpy]==False):
						vis[tmpx][tmpy]=True
						stack.append([tmpx,tmpy])
						par[tmpx][tmpy]=[fp[0],fp[1]]
			#for row1 in range (ROWS):
			#	for col1 in range (COLS):
			#		print(par[row1][col1][0],par[row1][col1][1],end=" ")
			#	print("")
			if(par[row][col]==[-1,-1]):
				print("NOT REACHABLE")
			else:
				path=[]
				while(row!=sx and col!=sy):
					path.append([row,col])
					[row,col]=par[row][col]
				path.reverse()
				for [row1,col1] in path:
					self.floor.move_from_to(sx,sy,row1,col1)
					sx=row1
					sy=col1
					self.update()
					pygame.time.delay(20)



			
			"""vis=[]
			for row1 in range (ROWS):
				temp=[]
				for col1 in range (COLS):
					temp.append(False)
				vis.append(temp)
			dx = [0,0,-1,1]
			dy = [-1,1,0,0]
			sx,sy=cor[0],cor[1]
			stack=[]
			vis[sx][sy]=True
			stack.append([sx,sy])
			while (len(stack)):
				fp=stack[-1]
				stack.pop()
				if (fp[0]==row and fp[1]==col):
					stack.append(fp)
					stack.pop(0)
					while(len(stack)):
						lp=stack[0]
						stack.pop(0)
						pygame.time.delay(500)
						self.floor.move_from_to(sx,sy,lp[0],lp[1])
						sx,sy=lp[0],lp[1]
						self.update()
					break
				for i in range (0,4):
					tmpx=fp[0]+dx[i]
					tmpy=fp[1]+dy[i]
					if(self.floor.inplace(tmpx,tmpy) and vis[tmpx][tmpy]==False):
						vis[tmpx][tmpy]=True
						stack.append([tmpx,tmpy])
			"""
			


	

		
		



	
