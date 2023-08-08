import pygame
import os
import random

SCREEN_W = 900
SCREEN_H = 700

WHITE = (255,255,255)
SEA = (80,180,220)
GROUND = (140,120,40)
DARK_GROUND = (70,60,20)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,"assets")

FPS = 60

class Fish():
    def __init__(self) -> None:
        self.image = pygame.image.load(os.path.join(assets_path,"fish.png"))
        self.sound = pygame.mixer.Sound(os.path.join(assets_path,"swim.wav"))
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.heiht = self.image.get_rect().height
        self.reset()
    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0
    def swim(self):
        self.dy = -10
        self.sound.play()
    def update(self):
        self.dy += 0.5
        self.rect.y += self.dy
        #화면위 걸리기
        if self.rect.y <= 0:
            self.rect.y = 0
        #화면아래 걸리기
        if self.rect.y >= (SCREEN_H-self.rect.height):
            self.rect.y = (SCREEN_H-self.rect.height)
            self.dy = 0
        if self.dy >20:
            self.dy = 20#속도제한
    def draw(self,screen):
        screen.blit(self.image,self.rect)

def main():
    pygame.init()#init후 파이게임 실행!!
    screen =pygame.display.set_mode((SCREEN_W,SCREEN_H))
    pygame.display.set_caption("fish game")
    clock = pygame.time.Clock()

    fish = Fish()
    fish.reset()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fish.swim()

        screen.fill(SEA)
        fish.update()
        fish.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()