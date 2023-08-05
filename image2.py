import pygame
import os

#창의 크기
SCREEN_WIDTH = 640   #가로
SCREEN_HEIGHT = 320  #세로

#색 정의
land = (160,120,40)

#초기화
pygame.init()

#창의 이름
pygame.display.set_caption("image2")

#창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#게임 화면 없데이트 속도
clock = pygame.time.Clock()

#이미지 랜더
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
background_image = pygame.image.load(os.path.join(assets_path,"terrain.png"))

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
    screen.fill(land)
    #화면 그리기 구간
    screen.blit(background_image,background_image.get_rect())
    #화면 없데이트
    pygame.display.flip()
    clock.tick(60)#60틱
pygame.quit()