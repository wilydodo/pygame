import pygame

#창의 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 600#세로

#색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#초기화
pygame.init()

#창의 이름
pygame.display.set_caption("PYGAME")

#창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#게임 화면 없데이트 속도
clock = pygame.time.Clock()

#게임종료여부
running = True

#게임 반복 구간
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #게임로직 구간
    #화면삭제구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    #화면 없데이트
    pygame.display.flip()
    #초당 60 프레임으로 없데이트
    clock.tick(60)
pygame.quit()