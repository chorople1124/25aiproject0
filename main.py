import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 300))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# 공룡, 장애물
dino = pygame.Rect(50, 250, 40, 40)
obstacle = pygame.Rect(800, 250, 20, 40)
jump = False
jump_speed = 10
gravity = 1
velocity = 0
score = 0

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not jump:
            if event.key == pygame.K_SPACE:
                jump = True
                velocity = -jump_speed

    # 점프 처리
    if jump:
        dino.y += velocity
        velocity += gravity
        if dino.y >= 250:
            dino.y = 250
            jump = False

    # 장애물 이동
    obstacle.x -= 5
    if obstacle.x < -20:
        obstacle.x = 800
        score += 1

    # 충돌 검사
    if dino.colliderect(obstacle):
        screen.blit(font.render("💥 Game Over", True, RED), (320, 120))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    # 화면 그리기
    pygame.draw.rect(screen, GREEN, dino)
    pygame.draw.rect(screen, RED, obstacle)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
