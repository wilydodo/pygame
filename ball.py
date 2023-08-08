import pygame

#양수+1,음수+1
def ad1(num=int,add=int):
    """'num'이 양수면 'add'를 더합니다
       'num'이 음수면 add를 뺍니다"""
    if num == abs(num):
        return num+add
    else:
        return num-add

#창의 크기
SCREEN_WIDTH = 600 #가로
SCREEN_HEIGHT = 500#세로

#색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 96, 240)

#초기화
pygame.init()

#창의 이름
pygame.display.set_caption("Ball")

#창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#게임 화면 없데이트 속도
clock = pygame.time.Clock()
# 초기화
ball_x = int(SCREEN_WIDTH/2)
ball_y = int(SCREEN_HEIGHT/2)
ball_dx = 2
ball_dy = 2
ball_size = max(SCREEN_WIDTH,SCREEN_HEIGHT)/10

#게임종료여부
done = False

#게임 반복 구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    #게임로직 구간
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x <= ball_size or ball_x >= SCREEN_WIDTH-ball_size:
        ball_dx*=-1
#        ball_dx = ad1(ball_dx,1)
    if ball_y <= ball_size or ball_y >= SCREEN_HEIGHT-ball_size:
        ball_dy*=-1
#        ball_dy = ad1(ball_dy,1)

    #화면삭제구간
    #스크린 채우기
    screen.fill(WHITE)
    #화면 그리기 구간
    pygame.draw.circle(screen,PURPLE,[ball_x,ball_y],ball_size,0)
    #화면 없데이트
    pygame.display.flip()
    #초당 60 프레임으로 없데이트
    clock.tick(120)
pygame.quit()