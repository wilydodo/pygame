import pygame
import random
from time import sleep
#screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#grid size
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT =SCREEN_HEIGHT/GRID_SIZE
#color
WHITE = (255,255,255)
ORANGE = (250,150,0)
GRAY = (100, 100, 100)
#move sight
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

class Snake():
    def __init__(self):
        self.create()
    def create(self):
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
    def control(self,xy):
        if (xy[0]*-1, xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
    def move(self):
        cur = self.positions[0]
        x,y =self.direction
        new = (cur[0]+(x*GRID_SIZE),(cur[1]+(y*GRID_SIZE)))
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or\
        new[1] < 0 or new[1] >= SCREEN_HEIGHT:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT))
    time = pygame.time.Clock()

    done = False

    while not done:
        screen.fill(WHITE)
        pygame.display.flip()
        time.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()