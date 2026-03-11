import pygame
import random

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

# Player
player_width = 50
player_height = 40
player_x = WIDTH//2
player_y = HEIGHT-60
player_speed = 7

# Bullets
bullets = []

# Enemies
enemies = []

# Score
score = 0
font = pygame.font.SysFont(None,36)

clock = pygame.time.Clock()

running = True

def draw_player():
    pygame.draw.rect(screen,WHITE,(player_x,player_y,player_width,player_height))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen,WHITE,bullet)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen,RED,enemy)

def spawn_enemy():
    x = random.randint(0, WIDTH-40)
    enemies.append(pygame.Rect(x, -40, 40, 40))

spawn_timer = 0

while running:

    clock.tick(60)
    screen.fill(BLACK)

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player_x+20, player_y, 5, 15))

    # MOVEMENT
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH-player_width:
        player_x += player_speed

    # BULLET MOVEMENT
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    # ENEMY SPAWN
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_enemy()
        spawn_timer = 0

    # ENEMY MOVEMENT
    for enemy in enemies[:]:
        enemy.y += 4

        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # COLLISION
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    # DRAW
    draw_player()
    draw_bullets()
    draw_enemies()

    score_text = font.render(f"Score: {score}",True,WHITE)
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()