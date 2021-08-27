
import numpy as np
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
font = pygame.font.SysFont("Courier New", 24)
size = (100, 100)
screen = pygame.display.set_mode(size)

grid = []
    # Loop for each row
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)


pygame.display.set_caption("Grid World")
done = False
clock = pygame.time.Clock()


MARGIN = 1
#column = 10
#row = 10
WIDTH = 4
HEIGHT = 4


while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill(BLACK) # this is the background

    #for row in range(4):
    #for column in range(4):
    color = WHITE

    """
    rect = pygame.Rect([(MARGIN + WIDTH) * column + MARGIN,
                      (MARGIN + HEIGHT) * row + MARGIN,
                      WIDTH,
                      HEIGHT]) """
    #column = pos[0] // (WIDTH + MARGIN)
    #row = pos[1] // (HEIGHT + MARGIN)


    for row in range(10):
        for col in range(10):
            

            rect = pygame.Rect([(MARGIN + WIDTH) * (col + MARGIN),
                                (MARGIN + HEIGHT) * (row + MARGIN),WIDTH,HEIGHT]) 
            
            pygame.draw.rect(screen,color,rect)


    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()




