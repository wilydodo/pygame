import pygame
from random import choice,randint
from time import sleep
import random

#screen size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
#grid size
GRID_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT =SCREEN_HEIGHT/GRID_SIZE
#color
BLACK = (0,0,0,)
WHITE = (255,255,255)
ORANGE = (250,150,0)
RED = (255,0,0)
GRAY = (100, 100, 100)
#move sight
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

class Snake():
    def __init__(self):
        self.create(self)
    def create(self,type):
        self.length = 2
        if type == 1:
            self.positions = [(int(SCREEN_WIDTH/4),int(SCREEN_HEIGHT/2))]
            self.direction = choice([UP,DOWN,LEFT,RIGHT])
        else:
            self.positions = [(SCREEN_WIDTH-int(SCREEN_WIDTH/4),int(SCREEN_HEIGHT/2))]
            self.direction = choice([UP,DOWN,LEFT,RIGHT])
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
            self.create(me)
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
    def eat(self):
        self.length+=1
    def draw(self,screen,type):
        if type == 1:
            col=(0,255,0)
        else:
            col=(0,0,255)
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, col, rect)

class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = ORANGE
        self.create()
    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0, GRID_HEIGHT-1)
        self.position = x * GRID_SIZE, y * GRID_SIZE
    def draw(self,screen):
        rect = pygame.Rect((self.position[0],self.position[1]),(GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,self.color,rect)
            
class Game():
    def __init__(self):
        self.snake1 = Snake()
        self.snake2 = Snake()
        self.feed = Feed()
        self.speed = 5
    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake1.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake1.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake1.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake1.control(RIGHT)
                elif event.key == pygame.K_w:
                    self.snake2.control(UP)
                elif event.key == pygame.K_s:
                    self.snake2.control(DOWN)
                elif event.key == pygame.K_a:
                    self.snake2.control(LEFT)
                elif event.key == pygame.K_d:
                    self.snake2.control(RIGHT)

        return False
    def run_logic(self):
        self.snake1.move()
        self.snake2.move()
        self.check_eat1(self.snake1,self.feed)
        self.check_eat2(self.snake2,self.feed)
        self.speed = (25 + self.snake1.length) / 2
    def check_eat1(self, snake,feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    def check_eat2(self, snake,feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    def draw_info(self,length,speed,screen):
        info = "length"+str(length)+"       "+"speed: "+str(round(speed,2))
        font = pygame.font.SysFont('FixedSys',30,False,False)
        text_obj = font.render(info,True,BLACK)
        text_rect = text_obj.get_rect()
        text_rect = text_obj.get_rect()
        screen.blit(text_obj,text_rect)
    def display_frame(self,screen):
        screen.fill(WHITE)
        self.draw_info(self.snake1.length,self.speed,screen)
        self.draw_info(self.snake2.length,self.speed,screen)
        self.snake1.draw(screen,1)
        self.snake2.draw(screen,2)
        self.feed.draw(screen)
        screen.blit(screen,(0,0))

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode(((SCREEN_WIDTH,SCREEN_HEIGHT)))
    time = pygame.time.Clock()
    game=Game()
    done = False

    while not done:
        done = game.process_event()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        time.tick(game.speed)

    pygame.quit()

if __name__ == "__main__":
    main()

#gg!    