import pygame
import time
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
clock = pygame.time.Clock()
from random import randint
pygame.init()
screen = pygame.display.set_mode((500,200))
COLOR = (203,214,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)
YELLOW = (125, 1, 128)
TIM = (128, 0, 255)
XANH = (0, 255, 64)
XANH_NHAT = (163, 220, 172)
XAM = (192, 192, 192)
a1 = pygame.image.load('map/Tile_8.png')
a2 = pygame.image.load('map/Tile_33.png')
running = True
x = 50
y = 50
k=0
while running:
    screen.fill(XAM)
    p_rect = pygame.draw.rect(screen,BLACK,(x,y,1,1))
    p_img = screen.blit(a1, (100, 100))
    if p_rect.colliderect(p_img):
        print(k)
        k+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                y += 5
            if event.key == K_UP:
                y -= 5
            if event.key == K_RIGHT:
                x += 5
            if event.key == K_LEFT:
                x -= 5
    pygame.display.flip()
pygame.quit()