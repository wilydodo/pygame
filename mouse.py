import pygame
import os
#창의 크기
SCREEN_WIDTH = 800 #가로 
SCREEN_HEIGHT = 600#세로

WHITE = (255,255,255)

pygame.init()

pygame.display.set_caption("Mouse")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path,"assets")
mouse_image=pygame.image.load(os.path.join(assets_path,"mouse.png"))
mouse_x = int(SCREEN_WIDTH/2)
mouse_y = int(SCREEN_HEIGHT/2)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)
    screen.blit(mouse_image,[mouse_x,mouse_y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()