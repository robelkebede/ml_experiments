
import time
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

class NewWorld():

    def __init__(self):


        self.goal_x = 3
        self.goal_y = 3

        self.size = 4

        self.done = False
        
        self.grid = []

        self.x = 0
        self.y = 0

        for i in range(self.size):
            self.grid.append([])
            for x in range(self.size):
                self.grid[i].append(0)

        self.grid = np.array(self.grid)

        self.grid[0][0] =1

        # init reward function 

        self.reward = np.ones_like(self.grid)
        self.reward[3][3] = 10
        self.reward[3][0] = -1
        #self.reward[2][2] = -1

        # init value function 
        
        self.value = []
        for i in range(self.size):
            self.value.append([])
            for x in range(self.size):
                self.value[i].append(1)

        self.value = np.array(self.value) 

        # transition probability 
        #           1  2    3     4
        # 4 moves [up down left right]

        # source https://github.com/dennybritz/...envs/gridworld.py     

        P = {}
        grid = self.grid
        it = np.nditer(grid,flags=['multi_index'])

        #it = np.nditer(grid)
        
        xy2i = lambda x,y:x*self.size+y
        
        while not it.finished: 

            s = it.iterindex
            #y, x = it.multi_index
            x, y = it.multi_index
        
            #           1  2   3   4
            # 4 moves [up down left right]

            P[s] = {a : [] for a in range(4)} 

            MAX_X = 3
            MAX_Y = 3
            MIN_X = 0
            MIN_Y = 0

            t_x = x
            t_y = y

            if self.done:
                P[s][0] = [(1.0, s, self.reward[x][y], True)]
                P[s][1] = [(1.0, s, self.reward[x][y], True)]
                P[s][2] = [(1.0, s, self.reward[x][y], True)]
                P[s][3] = [(1.0, s, self.reward[x][y], True)]

            else:
                
                ns_up = s if x == MIN_X else xy2i(x-1,y)
                ns_down = s if x == MAX_X else xy2i(x+1,y)

                ns_left = s if y == MIN_Y else xy2i(x,y-1) # this is brockn

                ns_right = s if y == MAX_Y else xy2i(x,y+1)

                is_done = lambda x:True if x ==15 else False

                P[s][0] = [(1.0, ns_up, self.reward[self.x][self.y], is_done(ns_up))]
                P[s][1] = [(1.0, ns_down, self.reward[self.x][self.y], is_done(ns_down))]
                P[s][2] = [(1.0, ns_left, self.reward[self.x][self.y], is_done(ns_left))]
                P[s][3] = [(1.0, ns_right, self.reward[self.x][self.y], is_done(ns_right))]  
        
            
            it.iternext()

        self.P = P
        self.state = np.ones(16)/16


    def render(self):
        clear_output(wait=True)  
        print(self.grid)
        time.sleep(1)

    def random_action(self):

        #           1  2   3   4
        # 4 moves [up down left right]
        move = np.random.randint(4)

        return move


    def reset(self):


        self.grid = []

        self.done = False

        self.x = 0
        self.y = 0

        for i in range(self.size):
            self.grid.append([])
            for x in range(self.size):
                self.grid[i].append(0)

        self.grid = np.array(self.grid)
        self.grid[0][0] = 1



    def step(self,x):
                  # 1  2   3   4
        # 4 moves [up down left right]
        if x==0: 
            self.move(x=-1,y=0)
        if x==1: 
            self.move(x=+1,y=0)
        if x==2: 
            self.move(x=0,y=-1)
        if x==3: 
            self.move(x=0,y=1)

        # return observation reward and done
        
        if self.x == self.goal_x and self.y == self.goal_y:
            self.done = True

        return [self.x,self.y],self.reward[self.x][self.y],self.done,{}

    def move(self,x,y):

        self.grid[self.x][self.y] = 0

        self.x += x
        self.y += y

        if self.x < 0:
            self.x = 0

        elif self.x > self.size-1:
            self.x = self.size-1

        if self.y < 0:
            self.y = 0

        elif self.y > self.size-1:
            self.y = self.size-1

        # if goal state return done

        self.grid[self.x][self.y] = 1



if __name__ == "__main__":

    new = NewWorld()
    #          1   2   3    4 
    # 4 moves [up down left right]

    for i in range(16):
        val = new.P[i]

        print("state ",i,val) 


    print(" #          1   2   3    4  \n# 4 moves [up down left right] ")




