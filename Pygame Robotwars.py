import pygame
import sys

pygame.init()
background = pygame.image.load("Grafiken/Hintergrund.jpg")
screen = pygame.display.set_mode([1200,800])
clock = pygame.time.Clock()
pygame.display.set_caption("Robotwars")

x=300
y=300
player_speed=6
width=40
height=80
clock = pygame.time.Clock()
pygame.display.set_caption("Robotwars")

left_wall = pygame.draw.rect(screen,(0,0,0),(-2,0,2,600),0)
right_wall = pygame.draw.rect(screen,(0,0,0),(1201,0,2,600),0)
play_field = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player_rectangle = pygame.Rect(x,y,40,80)
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        y -= player_speed
    if pressed_keys[pygame.K_LEFT] and not player_rectangle.colliderect(left_wall):
        x -= player_speed
    if pressed_keys[pygame.K_RIGHT] and not player_rectangle.colliderect(left_wall):
        x += player_speed
    if pressed_keys[pygame.K_DOWN]:
        y += player_speed

    screen.blit(background,(0,0))
    pygame.draw.rect(screen,(255,255,0),(x,y,width,height))
    pygame.display.update()
    clock.tick(60)