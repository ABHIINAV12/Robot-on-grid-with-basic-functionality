import pygame
from factory.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK, BLUE, GREY, ROWS, COLS
from factory.floor import Floor
from factory.act import Act


FPS=60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Factory')

def get_row_col_from_mouse(pos):
	x,y=pos
	row=y// SQUARE_SIZE
	col=x//SQUARE_SIZE
	return row,col


def main(): 
	run=True
	clock=pygame.time.Clock()
	floor=Act(WIN)

	while run:
		clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos=pygame.mouse.get_pos()
				row,col=get_row_col_from_mouse(pos)
				floor.teleport(row,col)

			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
				move = [0,0,0,0]
				dx = [0,0,-1,1]
				dy = [-1,1,0,0]
	
				for key in keys:
					if keys[pygame.K_LEFT]:
						move[0]=1
					elif keys[pygame.K_RIGHT]:
						move[1]=1
					elif keys[pygame.K_UP]:
						move[2]=1
					elif keys[pygame.K_DOWN]:
						move[3]=1
				for i in range (0,4):
					if(move[i]==1):
						print(dx[i],dy[i])
						floor.move_robot(dx[i],dy[i])
				
		floor.update()

	pygame.quit() 

main()  

	