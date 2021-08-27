
import numpy as np
import pygame 

"""
    input : name of the game 
    

    render : pygame blit 

    output : observation -> numpy grid of the states
           : reward -> scalar reward value 
           : done -> bool output
           : info -> other outputs

"""
"""
    if event.scancode == 82:
        print("up")
    elif event.scancode == 81:
        print("down")
    elif event.scancode == 80:
        print("left")
    elif event.scancode == 79:
        print("right") 
"""

class GridWorld():
    def __init__(self):

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED   = (255, 0, 0)
     
        pygame.init()
        self.font = pygame.font.SysFont("Courier New", 24)
        self.size = (500, 500)
        self.screen = pygame.display.set_mode(self.size)
        
        # init agent 

        self.agent = [0,0]
        
        # init state

        self.grid = []
        
        for row in range(10):
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)
        
        self.grid[0][0] = 1 # init pos
        pygame.display.set_caption("Grid World")
        self.done = False
        self.clock = pygame.time.Clock()
        
    def ren(self):
        grid = []
        for row in range(10):
            grid.append([])
            for column in range(10):
                grid[row].append(0)
    
        return grid

    
    def observation(self):

        return np.array(self.grid)

    def act(self,action):

        # is it up down left right  
        # represent the agent with green 
        # starting pos == [0,0]
        # [1,2,3,4] up,down,left,right

        # how to get the reward


        reward = 0
        
        if action == 1:
            self.agent[0] -= 1
        
        elif action == 2:
            self.agent[0] += 1

        elif action == 3:
            self.agent[1] -= 1

        elif action == 4:
            self.agent[1] += 1
        
        
        x,y = self.agent[0],self.agent[1] # agents pos

        self.grid = self.ren()
        self.grid[x][y] = 1


        return self.observation(),reward,self.done


    def render(self):

        # if render is true show the graphics 

        self.MARGIN = 3
        self.column = 10
        self.row = 10
        self.WIDTH = 45
        self.HEIGHT = 45

        
        while not self.done:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    column = pos[0] // (self.WIDTH + self.MARGIN)
                    row = pos[1] // (self.HEIGHT + self.MARGIN)
                    
                    self.grid[row][column] +=1
                elif event.type == pygame.KEYDOWN:

                    if event.scancode == 82:
                        self.act(1)
                    elif event.scancode == 81:
                        self.act(2)
                    elif event.scancode == 80:
                        self.act(3)
                    elif event.scancode == 79:
                        self.act(4)

            
            print(self.observation())            

            self.screen.fill(self.BLACK)

            for row in range(10):
                for column in range(10):
                    color = self.WHITE

                    rect = pygame.Rect([(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                      (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                      self.WIDTH,
                                      self.HEIGHT])

                    pygame.draw.rect(self.screen,
                                     color,
                                     rect)




                    text = self.font.render(str(self.grid[row][column]), True,self.RED)
                    self.screen.blit(text, (rect.right-35, rect.top+10))
             
            
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == "__main__":
    game = GridWorld()
    pygame.quit()










