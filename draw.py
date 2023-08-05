import pygame

#창의 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 800 #세로

#색 정의
BLACk = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 96, 240)

#초기화
pygame.init()

#창의 이름
pygame.display.set_caption("그림 그리기")

#창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))

#게임 화면 없데이트 속도
clock = pygame.time.Clock()

#게임종료여부
done = False

#게임 반복 구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    #게임로직 구간
    #화면삭제구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    pygame.draw.rect(screen, BLUE, [50,50,500,500],3)
    pygame.draw.line(screen, PURPLE, [50, 300],[549,300],5)
    pygame.draw.line(screen, PURPLE, [300, 50],[300,549],5)
    pygame.draw.circle(screen, GREEN, [300,300],50,3)
    pygame.draw.polygon(screen, PURPLE, [[400,200],[200,400],[600,400]],4)
    pygame.draw.ellipse(screen,BLUE,[250,400,200,100],1)
    font = pygame.font.SysFont('Wingdings', 40, True, False)
    text = font.render("hello, world!",True, BLACk)
    screen.blit(text, [400,400])
    #화면 없데이트
    pygame.display.flip()
    #초당 60 프레임으로 없데이트
    clock.tick(60)
pygame.quit()