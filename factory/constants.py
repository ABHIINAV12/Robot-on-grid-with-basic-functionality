import pygame
WIDTH, HEIGHT = 800,800
ROWS,COLS = 80,80
SQUARE_SIZE	= WIDTH//COLS


RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY=(128,128,128)


MACHINE= pygame.transform.scale(pygame.image.load('assets/machine.png'),(10,10))
ROBOT= pygame.transform.scale(pygame.image.load('assets/robot.png'),(10,10))