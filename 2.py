import pygame
import random
#창의 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 600#세로

#색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
r = (255, 0 ,0)
g = (0, 255, 0)
b = (0, 0, 255)
COLOR=BLACK
sel=((255, 0 ,0),(0, 255, 0),(0, 0, 255))
#초기화
pygame.init()

#창의 이름
pygame.display.set_caption("PYGAME")

#창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#게임 화면 없데이트 속도
clock = pygame.time.Clock()

#게임종료여부
done = False

#게임 반복 구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if COLOR == (255, 0 ,0):
                    COLOR = (0, 255, 0)
                elif COLOR == (0, 255, 0):
                    COLOR = (0, 0, 255)
                elif COLOR == (0, 0, 255):
                    COLOR = (255, 0 ,0)
                else:
                    COLOR = (255, 0 ,0)
            elif event.key == pygame.K_r:
                COLOR = random.choice(sel)
    #게임로직 구간
    #화면삭제구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    rect= pygame.Rect(0,0,100,100)
    rect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
    pygame.draw.rect(screen,COLOR,rect,0)
    #화면 없데이트
    pygame.display.flip()
    #초당 60 프레임으로 없데이트
    clock.tick(60)
pygame.quit()