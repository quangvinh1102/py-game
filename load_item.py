import pygame
import time
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_UP, K_q, K_w, K_e, K_f

clock = pygame.time.Clock()
from random import randint
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
COLOR = (203,214,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)
YELLOW = (125, 1, 128)
TIM = (128, 0, 255)
XANH = (0, 255, 64)
XANH_NHAT = (163, 220, 172)
XAM = (192, 192, 192)

cao = 55
rong = 105

sl_map = 60
Tile = []
Tile_st = 'Tile_'
for i in range(sl_map):
    Tile_load = pygame.image.load(f'map/{Tile_st + str(i+1)}.png')
    Tile.append(Tile_load)


Item = []
sl_item = 5
for i in range(sl_item):
    Item_load = pygame.image.load(f'item/{str(i+1)}.png')
    Item_load = pygame.transform.scale(Item_load,(32, 32))
    Item.append(Item_load)

Coin = []
Coin_st = 'Coin'
sl_coin = 4
for i in range(sl_coin):
    Coin_load = pygame.image.load(f'img_item/{Coin_st + str(i+1)}.png')
    Coin_load = pygame.transform.scale(Coin_load, (25, 25))
    Coin.append(Coin_load)

Rune = []
Rune_st = 'Rune'
sl_rune = 4
for i in range(sl_rune):
    Rune_load = pygame.image.load(f'img_item/{Rune_st + str(i+1)}.png')
    Rune_load = pygame.transform.scale(Rune_load, (30, 30))
    Rune.append(Rune_load)

Key = []
Key_st = 'Key'
sl_key = 4
for i in range(sl_key):
    Key_load = pygame.image.load(f'img_item/{Key_st + str(i+1)}.png')
    Key_load = pygame.transform.scale(Key_load, (28, 21))
    Key.append(Key_load)

Chest = []
Chest_st = 'Chest'
sl_chest = 6
for i in range(sl_chest):
    Chest_load = pygame.image.load(f'img_item/{Chest_st + str(i+1)}.png')
    Chest.append(Chest_load)

Flag = []
Flag_st = 'Flag'
sl_flag = 4
for i in range(sl_flag):
    Flag_load = pygame.image.load(f'img_item/{Flag_st + str(i+1)}.png')
    Flag.append(Flag_load)

Br = []
sl_br = 54
for i in range(sl_br):
    Br_load = pygame.image.load(f'br/{str(i+1)}.png')
    if i > 17 and i < 37:
        x_q, y_q = Br_load.get_size()
        if i < 29:
            Br_load = pygame.transform.scale(Br_load, (x_q * 2, y_q))
        else:
            Br_load = pygame.transform.scale(Br_load, (x_q * 2, y_q + 5))
    Br.append(Br_load)

Br2 = []
sl_br2 = 21
for i in range(sl_br2):
    Br2_load = pygame.image.load(f'br2/{str(i+1)}.png')
    if i > 8 and i < 19:
        x_q, y_q = Br2_load.get_size()
        Br2_load = pygame.transform.scale(Br2_load, (x_q * 2, y_q))
    Br2.append(Br2_load)


file_icon = []
y = 440
x = -40
for i in range(sl_item + 1):
    x += 40
    if x > 799 :
        x = 0
        y += 40
    file_icon.append([i, x, y, 0])

y = 0
file_xy = []
for i in range(cao):
    x = 0
    rkt = []
    for t in range(rong):
        rkt.append([x, y])
        x += 32
    file_xy.append(rkt)
    y += 32

f_map = []
fi_map = []
file_map = []
file = open('file_map.txt')
for i in range(cao):
    map = file.readline().split()
    f_map.append(map)
for i in range(cao):
    fi_map = []
    for t in range(rong):
        k = int(f_map[i][t])
        fi_map.append(k)
    file_map.append(fi_map)  
file.close

f_item = []
fi_item = []
file_item = []
file1 = open('file_item.txt')
for i in range(cao):
    item = file1.readline().split()
    f_item.append(item)
for i in range(cao):
    fi_item = []
    for t in range(rong):
        k = int(f_item[i][t])
        fi_item.append(k)
    file_item.append(fi_item)  
file.close

f_br = []
fi_br = []
file_br = []
br1 = open('file_br.txt')
for i in range(cao):
    br33 = br1.readline().split()
    f_br.append(br33)
for i in range(cao):
    fi_br = []
    for t in range(rong):
        k = int(f_br[i][t])
        fi_br.append(k)
    file_br.append(fi_br)  
file.close

f_br2 = []
fi_br2 = []
file_br2 = []
br12 = open('file_br2.txt')
for i in range(cao):
    br22 = br12.readline().split()
    f_br2.append(br22)
for i in range(cao):
    fi_br2 = []
    for t in range(rong):
        k = int(f_br2[i][t])
        fi_br2.append(k)
    file_br2.append(fi_br2)  
file.close

k = -1
i_luu = 0
luu = False
br = 0
rb = 0
xac = True
xc = True
lock_luu = False
k_coin = 0.00001
k_rune = 0.00001
k_key = 0.00001
k_chest = 0.0001
k_flag = 0.00001

while running:
    screen.fill(XAM)
    x_mouse, y_mouse = pygame.mouse.get_pos()
    if lock_luu:
        for i in range(cao):
            for t in range(rong):
                x_map = file_xy[i][t][0] - br
                y_map = file_xy[i][t][1] - rb
                if x_mouse > x_map and y_mouse > y_map and x_mouse < x_map + 32 and y_mouse < y_map + 32 and y_mouse <= 416:
                    if file_map[i][t] < 0:
                        file_item[i][t] = k
    for i in range(13):
        pygame.draw.line(screen, TIM, (0, (i + 1) * 32), (800, (i + 1) * 32))
    for i in range(25):
        pygame.draw.line(screen, TIM, ((i + 1) * 32, 0), ((i + 1) * 32, 416))

    for i in range(5):
        pygame.draw.line(screen, TIM, (0, (i + 11) * 40), (800, (i + 11) * 40))
    for i in range(20):
        pygame.draw.line(screen, TIM, ((i + 1) * 40, 440), ((i + 1) * 40, 600))
        
    for i in range(cao):
        for t in range(rong):
            if file_br[i][t] > -1:
                a_map = file_br[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                if c_map - rb <= 410:
                    x_img, y_img = Br[a_map].get_size()
                    if y_img > 32:
                        y_xt = c_map - rb - (y_img - 32)
                    else:
                        y_xt = c_map - rb + (32 - y_img)
                    if x_img > 32:
                        x_xt = b_map - br + 16 - x_img / 2
                    else:
                        x_xt = b_map - br + (32 - x_img) / 2
                    screen.blit(Br[a_map], (x_xt, y_xt))
                    img_xt = pygame.transform.scale(Br[a_map],(32, 32))
                    if x_img > 32 and y_img > 32:
                        screen.blit(img_xt, (b_map - br, c_map - rb))
                    
    for i in range(cao):
        for t in range(rong):
            if file_map[i][t] > -1:
                a_map = file_map[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                if c_map - rb <= 410:
                    screen.blit(Tile[a_map], (b_map - br, c_map - rb))
    
    for i in range(cao):
        for t in range(rong):
            if file_item[i][t] > -1:
                a_map = file_item[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                if c_map - rb <= 410:
                    if a_map == 0:
                        screen.blit(Coin[int(k_coin)], (b_map - br, c_map - rb))
                    if a_map == 1:
                        screen.blit(Rune[int(k_rune)], (b_map - br, c_map - rb))
                    if a_map == 2:
                        screen.blit(Key[int(k_key)], (b_map - br, c_map - rb))
                    if a_map == 3:
                        screen.blit(Chest[int(k_chest)], (b_map - br, c_map - rb))
                    if a_map == 4:
                        screen.blit(Flag[int(k_flag)], (b_map - br - 6, c_map - rb - 17))

    for i in range(cao):
        for t in range(rong):
            if file_br2[i][t] > -1:
                a_map = file_br2[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                if c_map - rb <= 410:
                    x_img, y_img = Br2[a_map].get_size()
                    if y_img > 32:
                        y_xt = c_map - rb - (y_img - 32)
                    else:
                        y_xt = c_map - rb + (32 - y_img)
                    if x_img > 32:
                        x_xt = b_map - br + 16 - x_img / 2
                    else:
                        x_xt = b_map - br + (32 - x_img) / 2
                    screen.blit(Br2[a_map], (x_xt, y_xt))               
    k_coin += 0.08
    if k_coin > sl_coin:
        k_coin = 0

    k_rune += 0.08
    if k_rune > sl_rune:
        k_rune = 0

    k_key += 0.08
    if k_key > sl_key:
        k_key = 0

    k_flag += 0.08
    if k_flag > sl_flag:
        k_flag = 0
    
    k_chest += 0.08
    if k_chest > sl_chest:
        k_chest = 0



    for i in range(sl_item + 1):
        a_map = file_icon[i][0]
        b_map = file_icon[i][1]
        c_map = file_icon[i][2]
        d_map = file_icon[i][3]
        if d_map > 0:
            pygame.draw.rect(screen, RED, (b_map + 2, c_map + 2, 36, 36))
        pygame.draw.rect(screen, XAM, (b_map + 4, c_map + 4, 32, 32))
        if i < sl_item:
            screen.blit(Item[a_map], (b_map + 4, c_map + 4))


    if luu:
        file = open('file_item.txt','w')
        for i in range(cao):
            for t in range(rong):
                k_luu = file_item[i][t]
                file.write(str(k_luu) + ' ')
            file.write('\n')
        file.close()
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(sl_item + 1):
                    x_map = file_icon[i][1]
                    y_map = file_icon[i][2]
                    if x_mouse > x_map and y_mouse > y_map and x_mouse < x_map + 40 and y_mouse < y_map + 40:
                        k = file_icon[i][0]
                        if k == sl_item:
                            k = -1
                        file_icon[i_luu][3] = 0
                        i_luu = i
                        file_icon[i][3] = 1
                for i in range(cao):
                    for t in range(rong):
                        x_map = file_xy[i][t][0] - br
                        y_map = file_xy[i][t][1] - rb
                        if x_mouse > x_map and y_mouse > y_map and x_mouse < x_map + 32 and y_mouse < y_map + 32 and y_mouse <= 416:
                            if file_map[i][t] < 0:
                                file_item[i][t] = k
        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
               lock_luu = True
            if event.key == K_f:
               k = -1
               file_icon[i_luu][3] = 0
               i_luu = i
               file_icon[i][3] = 1
            if event.key == K_q:
                luu = True
            if event.key == K_RIGHT or event.key == K_d:
                if br < 2000:
                    br += 320
                if br > 2000 and xac:
                    br += 160
                    xac = False
            if event.key == K_LEFT or event.key == K_a:
                if xac == False:
                    br -= 160
                    xac = True
                else:
                    if br > 0:
                        br -= 320
            if event.key == K_DOWN or event.key == K_s:
                if rb < 1100:
                    rb += 160
                if rb > 1110 and xc:
                    rb += 128
                    xc = False
            if event.key == K_UP or event.key == K_w:
                if not xc:
                    rb -= 128
                    xc = True
                else:
                    if rb > 0:
                        rb -= 160
        if event.type == pygame.KEYUP:
            if event.key == K_e:
               lock_luu = False

    pygame.display.flip()
pygame.quit()