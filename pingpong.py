import pygame
import os
import random

WHITE = (255,255,255)
BLACK = (0,0,0,)
BLUE =(20,60,120)
ORANGE = (250,170,70,)
RED=(250,0,0)

FPS = 60

SCREEN_W = 480
SCREEN_H = 640

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,"assets")

class Ball():
    def __init__(self,bounce_sound):
        self.rect = pygame.Rect(SCREEN_W//2,SCREEN_H//2,12,12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0:
            self.dx *=-1
            self.rect.left = 0
            self.bounce_sound.play()
        if self.rect.right > SCREEN_W:
            self.dx*= -1
            self.rect.right = SCREEN_W
            self.bounce_sound.play()
    def reset(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.dx= random.randint(-3,3)
        self.dy = 5
    def draw(self,screen):
        pygame.draw.rect(screen,ORANGE,self.rect,0)
        pygame.draw.circle(screen,ORANGE,self.rect.center,6,0)

class Player1():
    def __init__(self,ping_sound):
        self.rect = pygame.Rect(SCREEN_W//2,SCREEN_H-40,50,15)#player1 길이 조절
        self.ping_sound = ping_sound
        self.dx = 0
    def update(self,ball):
        if self.rect.left <= 0 and self.dx <0:
            self.dx = 0
        elif self.rect.right >= SCREEN_W and self.dx>0:
            self.dx = 0
        
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5,5)#ball의 방향
            ball.dy *=-1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()
            
        self.rect.x+= self.dx
            
    def draw(self,screen):
        pygame.draw.rect(screen,RED,self.rect,0)

class Player2():
    def __init__(self,pong_sound):
        self.rect = pygame.Rect(SCREEN_W//2,40,50,15)#player2 길이 조절
        self.pong_sound = pong_sound
        self.dx = 0
    def update(self,ball):
        if self.rect.left <= 0 and self.dx <0:
            self.dx = 0
        elif self.rect.right >= SCREEN_W and self.dx>0:
            self.dx = 0
        
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5,5)#ball의 방향
            ball.dy *=-1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()
            
        self.rect.x+= self.dx
            
    def draw(self,screen):
        pygame.draw.rect(screen,RED,self.rect,0)

class Game():
    def __init__(self) :
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path,"bounce.wav"))
        ping_sound = pygame.mixer.Sound(os.path.join(assets_path,"ping.wav"))
        pong_sound = pygame.mixer.Sound(os.path.join(assets_path,"pong.wav"))
        self.font =pygame.font.SysFont("Comic Sans ms", 50,False,False)#폰트지정
        self.ball = Ball(bounce_sound)
        self.player1 = Player1(ping_sound)
        self.player2 = Player2(pong_sound)
        self.player1_score = 0
        self.player2_score = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player1.dx = -5
                elif event.key == pygame.K_RIGHT:
                    self.player1.dx = 5
                elif event.key == pygame.K_a:
                    self.player2.dx == -5
                elif event.key == pygame.K_d:
                    self.player2.dx == 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player1.dx = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player2.dx = 0

        return True
    
    def run_logic(self):
        self.ball.update()
        self.player1.update(self.ball)
#        self.player2.update(self.ball)
    #공이 나갔을때
        #위쪽
        if self.ball.rect.top<0:
            self.player2_score+=1
            self.ball.reset(self.player1.rect.centerx,self.player1.rect.centery)
        #아래쪽
        if self.ball.rect.bottom>SCREEN_H:
            self.player1_score+=1
            self.ball.reset(self.player2.rect.centerx,self.player2.rect.centery)

    def display_message(self,screen,message,color):
        label = self.font.render(message,True,color)
        width = label.get_width()
        height = label.get_height()
        pos_x = (SCREEN_W//2) - (width//2)
        pos_y = int(SCREEN_H//2)-(height//2)
        screen.blit(label,(pos_x,pos_y))
        pygame.display.update()

    def display_flame(self,screen):
        screen.fill(BLUE)
        if self.player2_score == 10:
            self.display_message(screen,"Player A Win!",WHITE)#승리 매세지
            self.player1_score = 0
            self.player2_score = 0
            pygame.time.wait(2000)
        elif self.player1_score == 10:
            self.display_message (screen,"Player B Win!",WHITE)#패배 매세지
            self.player1_score = 0
            self.player2_score = 0
            pygame.time.wait(2000)
        else: 
            self.ball.draw(screen)
            self.player1.draw(screen)
            self.player2.draw(screen)

            for x in range(0,SCREEN_W, 24):
                pygame.draw.rect(screen,WHITE,[x,int(SCREEN_H/2),10,10])
            #적 점수
            enemy_score_label = self.font.render(str(self.player1_score),True,WHITE)
            screen.blit(enemy_score_label,(10,250))
            #내 점수
            player_score_label = self.font.render(str(self.player2_score),True,WHITE)
            screen.blit(player_score_label,(10,330))
        

def main():
    pygame.init()
    pygame.display.set_caption("PINGPONG")
    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    clock = pygame.time.Clock()
    game = Game()

    running=True

    while running:
        running = game.process_events()
        game.run_logic()
        game.display_flame(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit
if __name__ == "__main__":
    main()