import pygame
from random import choice,randint
from time import sleep
import random

#screen size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
#grid size
GRID_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT =SCREEN_HEIGHT/GRID_SIZE
#color
BLACK = (0,0,0,)
WHITE = (220,220,220)
ORANGE = (250,150,0)
RED = (200,20,20)
GRAY = (100, 100, 100)
PURPLE = (100,100,200)
BLUE = (177,235,255)
GREEN = (153,255,69)
YELLOW = (255,242,62)
SC = WHITE
color = (YELLOW,GREEN,BLUE,PURPLE,WHITE)

def select(original,color):
    selected = random.choice(color)
    while original==selected:
        selected = random.choice(color)
    return selected

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
    def eat(self):
        self.length+=1
    def boom(self):
        sleep(1)
        self.length = 5
        self.create()
    def draw(self,screen):
        red,green,blue = 50/(self.length-1),150,150/(self.length-1)
        for i,p in enumerate(self.positions):
            color = (100+red*i,green,blue*i)
            rect = pygame.Rect((p[0],p[1]),(GRID_SIZE,GRID_SIZE))
            pygame.draw.rect(screen,color,rect)

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

class Boom():
    def __init__(self):
        self.position = (0,0)
        self.color = RED
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
        self.snake = Snake()
        self.feed = Feed()
        self.boom1 = Boom()
        self.boom2 = Boom()
        self.boom3 = Boom()
        self.boom4 = Boom()
        self.boom5 = Boom()
        self.boom6 = Boom()
        self.boom7 = Boom()
        self.boom8 = Boom()
        self.boom9 = Boom()
        self.boom0 = Boom()
        self.speed = 5
    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
                elif event.key == pygame.K_w:
                    self.snake.control(UP)
                elif event.key == pygame.K_s:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_a:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_d:
                    self.snake.control(RIGHT)
        return False
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake,self.feed,self.boom1,self.boom2,self.boom3,self.boom4,self.boom5,self.boom6,self.boom7,self.boom8,self.boom9,self.boom0)
        self.check_boom(self.snake,self.boom1)
        self.check_boom(self.snake,self.boom2)
        self.check_boom(self.snake,self.boom3)
        self.check_boom(self.snake,self.boom4)
        self.check_boom(self.snake,self.boom5)
        self.check_boom(self.snake,self.boom6)
        self.check_boom(self.snake,self.boom7)
        self.check_boom(self.snake,self.boom8)
        self.check_boom(self.snake,self.boom9)
        self.check_boom(self.snake,self.boom0)
        self.speed = (15 + self.snake.length) / 2
    def check_eat(self, snake,feed,boom1,boom2,boom3,boom4,boom5,boom6,boom7,boom8,boom9,boom0):
        global SC
        global color
        if snake.positions[0] == feed.position:
            SC = select(SC,color)
            snake.eat()
            feed.create()
            boom1.create()
            boom2.create()
            boom3.create()
            boom4.create()
            boom5.create()
            boom6.create()
            boom7.create()
            boom8.create()
            boom9.create()
            boom0.create()
    def check_boom(self,snake,boom):
        if snake.positions[0] == boom.position:
            snake.boom()
            boom.create()
    def draw_info(self,length,speed,screen):
        info = "length: "+str(length)+"       "+"speed: "+str(round(speed,2))
        font = pygame.font.SysFont('FixedSys',30,False,False)
        text_obj = font.render(info,True,BLACK)
        text_rect = text_obj.get_rect()
        text_rect = text_obj.get_rect()
        screen.blit(text_obj,text_rect)
    def display_frame(self,screen):
        screen.fill(SC)
        self.draw_info(self.snake.length,self.speed,screen)
        self.snake.draw(screen)
        self.boom1.draw(screen)
        self.boom2.draw(screen)
        self.boom3.draw(screen)
        self.boom4.draw(screen)
        self.boom5.draw(screen)
        self.boom6.draw(screen)
        self.boom7.draw(screen)
        self.boom8.draw(screen)
        self.boom9.draw(screen)
        self.boom0.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen,(0,0))

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
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