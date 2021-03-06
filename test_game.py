# from load_map import XANH_NHAT
import pygame
import time

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_F1, K_F2, K_F3, K_F7, K_F8, K_F9, K_F10, K_F11, K_F12, K_a,  K_d,  K_s, K_w, K_g, K_k
clock = pygame.time.Clock()
from random import randint
pygame.init()
x_y = 800, 416
screen = pygame.display.set_mode(x_y)
running = True
COLOR = (203,214,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)
YELLOW = (255, 255, 0)
DO = ( 255, 0, 128)
TIM = (128, 0, 255)
XANH = (0, 255, 64)
XAM = (192, 192, 192)
XANH_NHAT = (163, 220, 172)
CAM = (255, 128, 0)
THAM = (0, 0, 64)

walk_st = 'walk'
walk_attack_st = 'walk_attack'
jump_st = 'jump'
hight_jump_st = 'high_jump'
idle_st = 'idle'
run_st = 'run'
run_attack_st = 'run_attack'
attack_st = 'attack'
fire_st = 'fire'
attack_extra_st = 'attack_extra'
fire_extra_st = 'fire_extra'
death_st = 'death'
hurt_st = 'hurt'
push_st = 'push'
climb_st = 'climb'
Tile_st = 'Tile_'
wh = 100, 100

ve = False
ve1 = False
sleep_const = 3
sleep_k = 0.15

lock_map = True
mage_run = False
doi_nv = False
# load sl
sl_atr = 5
sl_atr_e = 8
sl_id = 12
nguon = 'anh1'
# load image
walk = []
for i in range(6):
    walk_load = pygame.image.load(f'{nguon}/{walk_st + str(i+1)}.png')
    walk.append(walk_load)
walk_attack = []
for i in range(6):
    walk_attack_load = pygame.image.load(f'{nguon}/{walk_attack_st + str(i+1)}.png')
    walk_attack.append(walk_attack_load)
jump = []
for i in range(7):
    jump_load = pygame.image.load(f'{nguon}/{jump_st + str(i+1)}.png')
    jump.append(jump_load)
hight_jump_up = []
for i in range(5):
    hight_load = pygame.image.load(f'{nguon}/{hight_jump_st + str(i+6)}.png')
    hight_jump_up.append(hight_load)
idle = []
for i in range(sl_id):
    idle_load = pygame.image.load(f'{nguon}/{idle_st + str(i+1)}.png')
    idle.append(idle_load)
run = []
for i in range(8):
    run_load = pygame.image.load(f'{nguon}/{run_st + str(i+1)}.png')
    run.append(run_load)
run_attack = []
for i in range(8):
    run_attack_load = pygame.image.load(f'{nguon}/{run_attack_st + str(i+1)}.png')
    run_attack.append(run_attack_load)
attack = []
for i in range(sl_atr):
    attack_load = pygame.image.load(f'{nguon}/{attack_st + str(i+1)}.png')  
    attack.append(attack_load)
if mage_run:
    fire = []
    for i in range(9):
        fire_load = pygame.image.load(f'{nguon}/{fire_st + str(i+1)}.png')
        fire.append(fire_load)
attack_extra = []
for i in range(sl_atr_e):
    attack_extra_load = pygame.image.load(f'{nguon}/{attack_extra_st + str(i+1)}.png')
    attack_extra.append(attack_extra_load)
if mage_run:
    fire_extra = []
    for i in range(9):
        fire_extra_load = pygame.image.load(f'{nguon}/{fire_extra_st + str(i+1)}.png')
        fire_extra.append(fire_extra_load)
death = []
for i in range(10):
    death_load = pygame.image.load(f'{nguon}/{death_st + str(i+1)}.png')
    death.append(death_load)
hurt = []
for i in range(4):
    hurt_load = pygame.image.load(f'{nguon}/{hurt_st + str (i+1)}.png')
    hurt.append(hurt_load)
push = []
for i in range(4):
    push_load = pygame.image.load(f'{nguon}/{push_st + str (i+1)}.png')
    push.append(push_load)
climb = []
for i in range(4):
    climb_load = pygame.image.load(f'{nguon}/{climb_st + str (i+1)}.png')
    climb.append(climb_load)

Tile = []
sl_map = 60
for i in range(sl_map):
    Tile_load = pygame.image.load(f'map/{Tile_st + str(i+1)}.png')
    Tile.append(Tile_load)

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

BG_1 = pygame.image.load(f'{nguon}/Background.png')
BG_1 = pygame.transform.scale(BG_1,x_y)
mage = pygame.image.load(f'{nguon}/mage.png')

font = pygame.font.SysFont('sans',15)
# const 
if True:
    x = 130
    go_x = x
    y = 250
    y_go = y
    x_br = 0
    y_br = -1200
    lock_y = False
    lock_y_r = False

    walk_run = False
    k = 0
    flip = False
    right = False
    left = False
    rt_l = True
    rt_r = False

    rt_l_run = True
    rt_r_run = False
    right_run = False
    left_run = False

    run_game = True
    lock = True

    jump_run = False
    hight_jump = False
    run_run = False
    run_hight = True
    lock_jump = True
    jump_run2 = 0
    kj = 0
    khj = 0
    sl_jump = 0
    sl_hjump = 0
    sleep_j = 0

    walk_attack_run = False
    run_attack_run = False
    sleep_y = 3

    # kt = 0
    r_sleep = sleep_const
    sleep = r_sleep
    sleep_br = r_sleep
    br_sleep = r_sleep

    sl_br = 4

    run_idle = True
    lock_idle = True
    k_idle = 0
    idle_run = False
    k_run = 0

    r_attack = True
    run_walk_attack = False
    stop_walk = False

    ru_attack = True
    run_run_attack = False
    stop_run = False

    attack_run = False
    k_a = 0
    lock_attack = True

    k_f = 0
    sl_fire = 0
    fire_run = False
    run_fire_run = True
    x_fire = 0
    y_fire = 60
    sl_fire_run = 0
    fire_flip = True

    skill = 1
    ex = 0

    attack_extra_run = False
    lock_attack_extra = True
    k_a_e = 0

    fire_extra_run = False
    k_f_e = 0
    y_fire_extra = 0
    x_fire_extra = 0
    fire_extra_flip = True
    flip_fire_extra = False
    sl_fire_extra = 0
    lock_fire_extra = True
    lock_fire1 = True

    hp = 100
    hp_r = hp
    sleep_hp = 20
    mp = 300
    mp_r = 300
    sleep_mp = 5
    sleep_mp_run = 0.25
    mp_run = 0

    death_run = True
    live = True
    reset = True
    lock_death = True
    k_d = 0
    x_death, y_death = 0, 0

    hurt_run = False
    k_h = 0

    push_run = False
    run_push = False
    push_jump = False
    sleep_push = r_sleep / 2
    sleep_walk_run = r_sleep
    k_p = 0

    climb_run = False
    lock_climb = True
    k_c = 0
    sl_climb = 0
    climb_sl = 2

    x_rect = 0
    y_rect = 0
    nb_x = 0
    nb_y = 0

    fall_run = False
    k_r = 0
    y_max = 0
    run_fall = True
    sleep_fall = 0
    lock_fall = True
    lock_run = True

    load = True

    cao = 55
    rong = 105
    y_file = 0
    kc = 0

    lock_xet = True
    x_ng = 0
    run_x_ng = True
    lock_ng = True
    lock_flip = False

    sl_co = 0
    sl_ru = 0
    sl_ke = 0
    k_coin = 0.00001
    k_rune = 0.00001
    k_key = 0.00001
    k_chest = 0.0001
    k_flag = 0.00001
    run_chest = False
    chest_run = True
    x_chest = -1
    y_chest = -1


file_xy = []
for i in range(cao):
    x_file = 0
    rkt = []
    for t in range(rong):
        rkt.append([x_file, y_file])
        x_file += 32
    file_xy.append(rkt)
    y_file += 32
# for i in range(cao):
#     print(file_xy[i])
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
        k_file = int(f_map[i][t])
        fi_map.append(k_file)
    file_map.append(fi_map)  
file.close()

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
    br2 = br1.readline().split()
    f_br.append(br2)
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

while running:

    if doi_nv:
        doi_nv = False
        # load image
        walk = []
        for i in range(6):
            walk_load = pygame.image.load(f'{nguon}/{walk_st + str(i+1)}.png')
            walk.append(walk_load)
        walk_attack = []
        for i in range(6):
            walk_attack_load = pygame.image.load(f'{nguon}/{walk_attack_st + str(i+1)}.png')
            walk_attack.append(walk_attack_load)
        jump = []
        for i in range(7):
            jump_load = pygame.image.load(f'{nguon}/{jump_st + str(i+1)}.png')
            jump.append(jump_load)
        hight_jump_up = []
        for i in range(5):
            hight_load = pygame.image.load(f'{nguon}/{hight_jump_st + str(i+6)}.png')
            hight_jump_up.append(hight_load)
        idle = []
        for i in range(sl_id):
            idle_load = pygame.image.load(f'{nguon}/{idle_st + str(i+1)}.png')
            idle.append(idle_load)
        run = []
        for i in range(8):
            run_load = pygame.image.load(f'{nguon}/{run_st + str(i+1)}.png')
            run.append(run_load)
        run_attack = []
        for i in range(8):
            run_attack_load = pygame.image.load(f'{nguon}/{run_attack_st + str(i+1)}.png')
            run_attack.append(run_attack_load)
        attack = []
        for i in range(sl_atr):
            attack_load = pygame.image.load(f'{nguon}/{attack_st + str(i+1)}.png')  
            attack.append(attack_load)
        if mage_run:
            fire = []
            for i in range(9):
                fire_load = pygame.image.load(f'{nguon}/{fire_st + str(i+1)}.png')
                fire.append(fire_load)
        attack_extra = []
        for i in range(sl_atr_e):
            attack_extra_load = pygame.image.load(f'{nguon}/{attack_extra_st + str(i+1)}.png')
            attack_extra.append(attack_extra_load)
        if mage_run:
            fire_extra = []
            for i in range(9):
                fire_extra_load = pygame.image.load(f'{nguon}/{fire_extra_st + str(i+1)}.png')
                fire_extra.append(fire_extra_load)
        death = []
        for i in range(10):
            death_load = pygame.image.load(f'{nguon}/{death_st + str(i+1)}.png')
            death.append(death_load)
        hurt = []
        for i in range(4):
            hurt_load = pygame.image.load(f'{nguon}/{hurt_st + str (i+1)}.png')
            hurt.append(hurt_load)
        push = []
        for i in range(4):
            push_load = pygame.image.load(f'{nguon}/{push_st + str (i+1)}.png')
            push.append(push_load)
        climb = []
        for i in range(4):
            climb_load = pygame.image.load(f'{nguon}/{climb_st + str (i+1)}.png')
            climb.append(climb_load)
        mage = pygame.image.load(f'{nguon}/mage.png')

    x_mouse, y_mouse = pygame.mouse.get_pos()
    # time.sleep(0.05)
    clock.tick(60)
    screen.fill(XAM)
    # for i in range(sl_br):
    #     screen.blit(BG_1,(x_br + i*x_y[0] ,0))

    for i in range(cao):
        for t in range(rong):
            if file_br[i][t] > -1:
                a_map = file_br[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                x_img, y_img = Br[a_map].get_size()
                if y_img > 32:
                    y_xt = c_map + y_br - (y_img - 32)
                else:
                    y_xt = c_map + y_br + (32 - y_img)
                if x_img > 32:
                    x_xt = b_map + x_br + 16 - x_img / 2
                else:
                    x_xt = b_map + x_br + (32 - x_img) / 2
                screen.blit(Br[a_map], (x_xt, y_xt))
             
    for i in range(cao):
        for t in range(rong):
            if file_map[i][t] > -1:
                a_map = file_map[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                screen.blit(Tile[a_map], (b_map + x_br, c_map + y_br))
        
    if ve:
        for i in range(cao):
            pygame.draw.line(screen, TIM, (0, (i + 1) * 32), (800, (i + 1) * 32))
        for i in range(rong):
            pygame.draw.line(screen, TIM, ((i + 1) * 32, 0), ((i + 1) * 32, 416))

        for i in range(5):
            pygame.draw.line(screen, TIM, (0, (i + 11) * 40), (800, (i + 11) * 40))
        for i in range(20):
            pygame.draw.line(screen, TIM, ((i + 1) * 40, 440), ((i + 1) * 40, 600))
    
    if hp <= 0 and reset:
        death_run =False
        live = False
        reset = False
        lock_death = False
    if hp > 0:
        death_run =True
        live = True
        lock_death = True
    if True:
        hp_write = font.render('HP :',True,BLACK)
        mp_write = font.render('MP :',True,BLACK)
        screen.blit(hp_write,(40, 33))
        screen.blit(mp_write,(40, 50))
        hp_write = font.render(str(hp) + ' / ' + str(hp_r),True,RED)
        mp_write = font.render(str(mp) + ' / ' + str(mp_r),True,BLUE)
        screen.blit(hp_write,(66, 33))
        screen.blit(mp_write,(66, 50))

    if push_run:
        if r_sleep > 0:
            r_sleep = sleep_push
        if r_sleep == 0:
            br_sleep = sleep_push
        k_p += sleep_k
        if k_p > 4:
            k_p = 0
    else:
        if r_sleep > 0:
            r_sleep = sleep_walk_run
        if r_sleep == 0:
            br_sleep = sleep_walk_run

    if walk_run:
        run_push = True
        if walk_attack_run and r_attack:
            lock_attack = False
            k = 0
            r_attack = False
            print('walk attack')
        if left and rt_l:
            x -= 35
            rt_l = False
            rt_l_run = False
            if not push_run:
                print('right --> left')
        if right and rt_r:
            x += 35
            rt_r = False
            rt_r_run = False
            if not push_run:
                print('left --> right')
        if left:
            sleep = -r_sleep
            sleep_br = -br_sleep
        if right:
            sleep = r_sleep
            sleep_br = br_sleep
        if not stop_walk and not hurt_run and lock_climb and lock_map and lock_xet:
            x += sleep
            if r_sleep == 0:
                x_br -= sleep_br
        k += sleep_k
        if k > 5 and lock_jump and run_fire_run and walk_attack_run:
            sl_fire += 1
            run_fire_run = False
        if k >= 6:
            k = 0
            run_fire_run = True
            walk_attack_run = False
            lock_attack = True

    if walk_attack_run and not walk_run:
        stop_walk = True
        walk_run = True

    if stop_walk and not walk_attack_run:
        walk_run = False
        stop_walk = False
    if run_run:
        run_push = True
        if run_attack_run and ru_attack:
            lock_attack = False
            k_run = 0
            ru_attack = False
            print('run attack')
        if left_run and rt_l_run:
            x -= 35
            rt_l_run = False
            rt_l = False
            if not push_run:
                print('run :right --> left')
        if right_run and rt_r_run:
            x += 35
            rt_r_run = False
            rt_r = False
            if not push_run:
                print('run :left --> right')
        if left_run:
            sleep = - (r_sleep + r_sleep/2)
            sleep_br = -(br_sleep + br_sleep/2)
        if right_run:
            sleep = r_sleep + r_sleep/2
            sleep_br = br_sleep + br_sleep/2
        if not stop_run and not hurt_run and lock_climb and lock_map and lock_xet:
            x += sleep
            if r_sleep == 0:
                x_br -= sleep_br
        k_run += sleep_k
        if k_run > 5:
            if run_attack_run and run_fire_run and lock_jump:
                sl_fire += 1
                run_fire_run = False
        if k_run >= 8:
            k_run = 0 
            run_attack_run = False
            run_fire_run = True
            lock_attack = True

    if run_attack_run and not run_run:
        stop_run = True
        run_run = True

    if stop_run and not run_attack_run and lock_climb:
        run_run = False
        stop_run = False

    if jump_run and not fall_run:
        push_run= False
        lock_jump = False
        run_idle = False
        if kj == 0:
            print('jump')
        kj += sleep_j
        if jump_run2 >= 2 and kj > 3.6 and not fall_run:
            jump_run = False
            hight_jump = True
            khj = 0
            sl_hjump = 5
            run_hight = False
            print('hight jump')
        if kj < 3.6:
            if lock_y:
                y_br += sleep_y
            else:
                y -= sleep_y
        else:
            y += sleep_y
        if kj >= 5 and kj <= 5.1:
            if y_go - y + y_br > 78:
                sl_jump = 6
        if kj >= sl_jump :
            kj = 6.9
            jump_run = False
            run_game = True
            jump_run2 = 0
            run_hight = True
            run_idle = True
            lock_jump = True
            if push_jump:
                push_run = True

    if hight_jump:
        push_run = False
        khj += sleep_j
        if khj < 2.7:
            if lock_y:
                y_br += int(sleep_y / 3 * 2)
            else:
                y -= int(sleep_y / 3 * 2)
        else:
            y += int(sleep_y / 3 * 2)
        if khj >= sl_hjump:
            hight_jump = False
            jump_run = True
            jump_run2 = 0

    if idle_run:
        walk_run = False
        run_run = False
        walk_attack_run = False
        run_attack_run = False
        if k_idle == 0:
            print('idle')
        k_idle += sleep_k
        if k_idle >= sl_id:
            lock_idle = True
            idle_run = False
    if y < 100 and y_br < 0:
        lock_y = True
    else:
        lock_y = False
    if y > 200 and y_br > -1248:
        lock_y_r = True
    else:
        lock_y_r = False
    if (right or right_run) and x > x_y[0]-300 and x_br > -(sl_br-1)*x_y[0]:
        if r_sleep > 0 :
            print('right')
        r_sleep = 0

    if (left or left_run) and x > x_y[0]-350:
        r_sleep = 2

    if (left or left_run) and x < 100 and x_br < -2:
        if r_sleep > 0:
            print('left')
        r_sleep = 0

    if (right or right_run) and x < 150:
        r_sleep = 2

    if x_br > 1:
        x_br = 0
        r_sleep = 2

    if x_br < -(sl_br-1)*x_y[0]:
        x_br = -(sl_br-1)*x_y[0]
        r_sleep = 2

    if x < -30:
        r_sleep = 0

    if x > x_y[0]-70:
        r_sleep = 0

    if attack_run and not fall_run:
        walk_run = False
        run_run = False
        walk_attack_run = False
        run_attack_run = False
        lock_attack = False
        idle_run = False
        if k_a == 0:
            print('attack')
        k_a += sleep_k
        if k_a > 5 and lock_jump and run_fire_run and mage_run:
            sl_fire += 1
            if sl_fire > 1:
                sl_fire = 1
            run_fire_run = False
        if k_a >= sl_atr:
            k_a = 0
            run_fire_run = True
            attack_run = False
            lock_attack = True

    if sl_fire > 0:
        fire_run = True
    else:
        fire_run = False
        
    if fire_run and mage_run:
        lock_fire1 = False
        if fire_flip == True:
            flip_fire = flip
            fire_flip = False
        if k_f == 0:
            sl_fire_run += 1
            print('fire :' + str(sl_fire_run))
            y_fire = y + 60
            if not flip:
                x_fire = x + 90
            else:
                x_fire = x - 10
        k_f += sleep_k
        if k_f >= 9:
            k_f = 0
            lock_fire1 = True
            fire_run = False
            fire_flip = True
            sl_fire -= 1
        if not flip_fire:
            x_fire += k_f * 2
        if flip_fire:
            x_fire -= k_f * 2

    if attack_extra_run and not fall_run:
        if k_a_e == 0:
            print('attack extra')
        k_a_e += sleep_k
        if k_a_e > 5.7 and lock_fire_extra and mage_run:
            fire_extra_run = True
            lock_fire_extra = False
        if k_a_e >= sl_atr_e:
            attack_extra_run = False
            lock_attack_extra = True
            lock_fire_extra = True
            k_a_e = 0

    if fire_extra_run and mage_run:
        lock_fire1 = False
        if fire_extra_flip == True:
            flip_fire_extra = flip
            fire_extra_flip = False
        if k_f_e == 0:
            sl_fire_extra += 1
            print('fire extra:' + str(sl_fire_extra))
            y_fire_extra = y + 10
            if not flip:
                x_fire_extra = x + 70
            else:
                x_fire_extra = x - 80
        k_f_e += sleep_k
        if k_f_e >= 9:
            k_f_e = 0
            fire_extra_run = False
            fire_extra_flip = True
            lock_fire1 = True
        if not flip_fire_extra:
            x_fire_extra += k_f_e * 2
        if flip_fire_extra:
            x_fire_extra -= k_f_e * 2
    
    if not death_run and not live:
        lock_death = False
        if k_d == 0:
            print('death')
        k_d += sleep_k
        if k_d >= 10:
            k_d = 0
            live = True
        if not flip:
            x_death = x - 80
        else:
            x_death = x - 40
        y_death = y - 45

    if hurt_run and lock_death:
        lock_death = False
        if k_h == 0:
            print('hurt')
        k_h += sleep_k
        if k_h >= 4:
            k_h = 0
            hurt_run = False
            lock_death = True

    if climb_run:
        if k_c == 0:
            print('climb')
        k_c += sleep_k
        if k_c > 4:
            sl_climb +=1
            k_c = 1
        if sl_climb == climb_sl:
            climb_run = False
            lock_climb = True
            k_c = 0
            sl_climb = 0

    run_game = True

    mp_run += sleep_mp_run
    if mp_run > 20 and death_run and live:
        mp += sleep_mp
        if mp > mp_r:
            mp = mp_r
        mp_run = 0

    if fall_run:
        if lock_y_r:
            y_br -= sleep_y
        else:
            y += sleep_y

    kc = 0
    nb_x = 45
    if not flip:
        x_rect = x + 22
        x_dot1 = x_rect + 42
        x_dot2 = x_rect + 33
        x_dot3 = x_rect + 10
    else:
        x_rect = x + 59
        x_dot1 = x_rect + 4
        x_dot2 = x_rect + 12
        x_dot3 = x_rect + 35
    if hight_jump:
        y_dot4 = y_rect + 5
    else:
        y_dot4 = y_rect
    x_dot4 = x_dot3
    y_dot5 = y_dot4
    x_dot6 = x_dot2
    y_dot6 = y_dot4
    x_dot5 = x_dot1
    y_rect = y + 60
    y_dot1 = y_rect + 32
    y_dot2 = y_rect + 52
    y_dot3 = y_dot2
    if ve and ve1:
        pygame.draw.rect(screen, BLACK, (x_dot1,y_dot1,10,10))
        pygame.draw.rect(screen, BLACK, (x_dot2,y_dot2,10,10))
        pygame.draw.rect(screen, BLACK, (x_dot3,y_dot2,10,10))
        pygame.draw.rect(screen, BLACK, (x_dot4,y_dot4,10,10))
        pygame.draw.rect(screen, BLACK, (x_dot5,y_dot5,10,10))
        pygame.draw.rect(screen, BLACK, (x_dot6,y_dot6,10,10))

    nb_y = 62
    if not flip:
        x_nv = x_rect + nb_x / 2 + kc - x_br
    else:
        x_nv = x_rect + nb_x / 2 - kc - x_br
    y_nv = y_rect + int(nb_y / 4 * 3) - y_br
    x_nv1, y_nv1 = x_dot1 - x_br, y_dot1 - y_br
    x_nv2, y_nv2 = x_dot2 - x_br, y_dot2 - y_br
    x_nv3, y_nv3 = x_dot3 - x_br, y_dot3 - y_br
    x_nv4, y_nv4 = x_dot4 - x_br, y_dot4 - y_br
    x_nv5, y_nv5 = x_dot5 - x_br, y_dot5 - y_br
    x_nv6, y_nv6 = x_dot6 - x_br, y_dot6 - y_br

    for i in range(cao):
        for t in range(rong):
            xy_vt = file_xy[i][t]
            if x_nv >= xy_vt[0] and x_nv < xy_vt[0] + 32 and y_nv >= xy_vt[1] and y_nv < xy_vt[1] + 32 :
                vtr = [i, t]
            if x_nv1 >= xy_vt[0] and x_nv1 < xy_vt[0] + 32 and y_nv1 >= xy_vt[1] and y_nv1 < xy_vt[1] + 32 :
                vtr1 = [i, t]
            if x_nv2 >= xy_vt[0] and x_nv2 < xy_vt[0] + 32 and y_nv2 >= xy_vt[1] and y_nv2 < xy_vt[1] + 32 :
                vtr2 = [i, t]
            if x_nv3 >= xy_vt[0] and x_nv3 < xy_vt[0] + 32 and y_nv3 >= xy_vt[1] and y_nv3 < xy_vt[1] + 32 :
                vtr3 = [i, t]
            if x_nv4 >= xy_vt[0] and x_nv4 < xy_vt[0] + 32 and y_nv4 >= xy_vt[1] and y_nv4 < xy_vt[1] + 32 :
                vtr4 = [i, t]
            if x_nv5 >= xy_vt[0] and x_nv5 < xy_vt[0] + 32 and y_nv5 >= xy_vt[1] and y_nv5 < xy_vt[1] + 32 :
                vtr5 = [i, t]
            if x_nv6 >= xy_vt[0] and x_nv6 < xy_vt[0] + 32 and y_nv6 >= xy_vt[1] and y_nv6 < xy_vt[1] + 32 :
                vtr6 = [i, t]

    x_map, y_map = vtr[0], vtr[1]
    x_map1, y_map1 = vtr1[0], vtr1[1]
    x_map2, y_map2 = vtr2[0], vtr2[1]
    x_map3, y_map3 = vtr3[0], vtr3[1]
    x_map4, y_map4 = vtr4[0], vtr4[1]
    x_map5, y_map5 = vtr5[0], vtr5[1]
    x_map6, y_map6 = vtr6[0], vtr6[1]
    if file_item[x_map][y_map] == 0:
        sl_co += 1
        print('number coin :' + str(sl_co))
        file_item[x_map][y_map] = -1
    if file_item[x_map - 1][y_map] == 0:
        sl_co += 1
        print('number coin :' + str(sl_co))
        file_item[x_map - 1][y_map] = -1

    if file_item[x_map][y_map] == 1:
        sl_ru += 1
        print('number rune :' + str(sl_ru))
        file_item[x_map][y_map] = -1
    if file_item[x_map - 1][y_map] == 1:
        sl_ru += 1
        print('number rune :' + str(sl_ru))
        file_item[x_map - 1][y_map] = -1

    if file_item[x_map][y_map] == 2:
        sl_ke += 1
        print('number key :' + str(sl_ke))
        file_item[x_map][y_map] = -1
    if file_item[x_map - 1][y_map] == 2:
        sl_ke += 1
        print('number key :' + str(sl_ke))
        file_item[x_map - 1][y_map] = -1

    if file_item[x_map][y_map] == 3 and sl_ke > 0 and run_chest and chest_run:
        print('open the box')
        x_chest = x_map
        y_chest = y_map
        sl_ke -= 1
        chest_run = False
        run_chest = False

    if file_map[x_map4][y_map4] > -1 or file_map[x_map6][y_map6] > -1:
        sl_jump = kj
        sl_hjump = khj
        fall_run = True
        lock_jump = True
    for i in range(x_map + 1, cao):
        if file_map[i][y_map] > -1:
            y_go = file_xy[i][y_map][1] - 112
            break
    if file_map[x_map2][y_map2] > -1:
        y_go = file_xy[x_map2][y_map2][1] - 112

    if file_map[x_map1][y_map1] > -1 or file_map[x_map5][y_map5] > -1:
        lock_map = False
    else:
        lock_map = True

    if y - y_br < y_go and lock_jump:
        fall_run = True
        k_r = 5
    if y - y_br >= y_go and fall_run:
        y = y_go
        fall_run = False
        run_fall = True


    # roi
    if file_map[x_map2][y_map2] < 0 and file_map[x_map3][y_map3] < 0 and lock_jump:
        fall_run = True
    else:
        fall_run = False
    if y - y_br > y_go:
        y = y_go + y_br
        sleep_j = sleep_k + 0.1
    else:
        sleep_j = sleep_k

    y11 = y + 2

    if mage_run:
        if fire_run :
            screen.blit(pygame.transform.flip(fire[int(k_f)],flip_fire,False),(x_fire, y_fire))

        if fire_extra_run:
            screen.blit(pygame.transform.flip(fire_extra[int(k_f_e)],flip_fire_extra,False),(x_fire_extra, y_fire_extra))

    if not death_run and not live:
        run_game = False
        screen.blit(pygame.transform.flip(death[int(k_d)],flip,False),(x_death, y_death))

    if attack_extra_run and death_run and live and not fall_run:
        run_game = False
        screen.blit(pygame.transform.flip(attack_extra[int(k_a_e)],flip,False),(x, y11))

    if hurt_run and death_run and live and not fall_run:
        run_game = False
        screen.blit(pygame.transform.flip(hurt[int(k_h)],flip,False),(x, y11))

    if push_run and not hurt_run and death_run and live and run_push and not climb_run:
        run_game = False
        screen.blit(pygame.transform.flip(push[int(k_p)],flip,False),(x, y11))

    if climb_run and not hurt_run and death_run and live:
        run_game = False
        screen.blit(pygame.transform.flip(climb[int(k_c)],flip,False),(x, y11))

    if ex > 0:
        nani = font.render('khong du mana',True,BLACK)
        screen.blit(nani,(350,10))
        ex -= 1

    if fall_run:
        run_game = False
        screen.blit(pygame.transform.flip(jump[int(k_r)],flip,False),(x,y11))
    if lock_attack_extra and death_run and not hurt_run and (not push_run or not run_push) and lock_climb and not fall_run:
        
        if attack_run:
            run_game = False
            screen.blit(pygame.transform.flip(attack[int(k_a)],flip,False),(x,y11))

        if idle_run:
            run_game = False
            screen.blit(pygame.transform.flip(idle[int(k_idle)],flip,False),(x,y11))

        if walk_run and not jump_run and not hight_jump:
            run_game = False
            if walk_attack_run:
                screen.blit(pygame.transform.flip(walk_attack[int(k)],flip,False),(x,y11))

            else:
                screen.blit(pygame.transform.flip(walk[int(k)],flip,False),(x,y11))

        if run_run and not jump_run and not hight_jump:
            run_game = False
            if run_attack_run:
                screen.blit(pygame.transform.flip(run_attack[int(k_run)],flip,False),(x,y11))

            else:
                screen.blit(pygame.transform.flip(run[int(k_run)],flip,False),(x,y11))

        if jump_run:
            run_game = False
            if int(kj) > sl_jump or int(kj) < 0:
                run_game = True
                jump_run = False
            else:
                screen.blit(pygame.transform.flip(jump[int(kj)],flip,False),(x,y11))

        if hight_jump:
            run_game = False
            screen.blit(pygame.transform.flip(hight_jump_up[int(khj)],flip,False),(x,y11))

        if run_game:
            k_run = 0
            screen.blit(pygame.transform.flip(mage,flip,False),(x,y11))
    
    for i in range(cao):
        for t in range(rong):
            if file_item[i][t] > -1:
                a_map = file_item[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                # screen.blit(Item[a_map], (b_map + x_br, c_map + y_br))
                if a_map == 0:
                    screen.blit(Coin[int(k_coin)], (b_map + x_br, c_map + y_br))
                if a_map == 1:
                    screen.blit(Rune[int(k_rune)], (b_map + x_br, c_map + y_br))
                if a_map == 2:
                    screen.blit(Key[int(k_key)], (b_map + x_br, c_map + y_br))
                if a_map == 3:
                    if x_chest == i and y_chest == t:
                        chest_run
                        screen.blit(Chest[int(k_chest)], (b_map + x_br, c_map + y_br))
                        k_chest += 0.05
                        if k_chest > sl_chest:
                            k_chest =0
                            file_item[i][t] = -1
                            x_chest = - 1
                            y_chest = -1
                            chest_run = True
                    else:
                        screen.blit(Chest[0], (b_map + x_br, c_map + y_br))
                if a_map == 4:
                    screen.blit(Flag[int(k_flag)], (b_map + x_br - 6, c_map + y_br - 17))
                    
    k_coin += sleep_k
    if k_coin > sl_coin:
        k_coin = 0

    k_rune += sleep_k
    if k_rune > sl_rune:
        k_rune = 0

    k_key += sleep_k
    if k_key > sl_key:
        k_key = 0

    k_flag += sleep_k
    if k_flag > sl_flag:
        k_flag = 0
             
    for i in range(cao):
        for t in range(rong):
            if file_br2[i][t] > -1:
                a_map = file_br2[i][t]
                b_map = file_xy[i][t][0]
                c_map = file_xy[i][t][1]
                if c_map + y_br <= 410:
                    x_img, y_img = Br2[a_map].get_size()
                    if y_img > 32:
                        y_xt = c_map + y_br - (y_img - 32)
                    else:
                        y_xt = c_map + y_br + (32 - y_img)
                    if x_img > 32:
                        x_xt = b_map + x_br + 16 - x_img / 2
                    else:
                        x_xt = b_map + x_br + (32 - x_img) / 2
                    screen.blit(Br2[a_map], (x_xt, y_xt))

    if k_f < 4:
        rect_fire = 10
    else:
        rect_fire = 0

    if flip_fire_extra:
        rect_fire_extra = 40
        fire_rect = x_fire_extra + 50
    else:
        fire_rect = x_fire_extra + 40
    if k_f_e < 3:
        rect_fire_extra = 30
    else:
        if flip_fire_extra:
            fire_rect = x_fire_extra + 45
            rect_fire_extra = 40
        else:
            rect_fire_extra = 40
            rect_fire_extra = 40

    if ve:
        pygame.draw.line(screen, RED, (x_rect, y_rect),(x_rect + nb_x, y_rect))
        pygame.draw.line(screen, RED, (x_rect + nb_x, y_rect),(x_rect + nb_x, y_rect + nb_y))
        pygame.draw.line(screen, RED, (x_rect, y_rect),(x_rect ,y_rect + nb_y))
        pygame.draw.line(screen, RED, (x_rect ,y_rect + nb_y),(x_rect + nb_x, y_rect + nb_y))
    
    if fire_run and ve:
        pygame.draw.line(screen, XANH, (x_fire - 10, y_fire + rect_fire), (x_fire + 40, y_fire+ rect_fire))
        pygame.draw.line(screen, XANH, (x_fire + 40, y_fire + rect_fire), (x_fire + 40, y_fire + 30))
        pygame.draw.line(screen, XANH, (x_fire - 10, y_fire + rect_fire), (x_fire - 10, y_fire + 30))
        pygame.draw.line(screen, XANH, (x_fire - 10, y_fire + 30), (x_fire +40, y_fire + 30))

    if fire_extra_run and ve:
        pygame.draw.line(screen, XANH, (fire_rect, y_fire_extra + 50), (fire_rect + rect_fire_extra, y_fire_extra + 50))
        pygame.draw.line(screen, XANH, (fire_rect + rect_fire_extra, y_fire_extra + 50), (fire_rect + rect_fire_extra, y_fire_extra + 90))
        pygame.draw.line(screen, XANH, (fire_rect, y_fire_extra + 50), (fire_rect, y_fire_extra + 90))
        pygame.draw.line(screen, XANH, (fire_rect, y_fire_extra + 90), (fire_rect + rect_fire_extra, y_fire_extra + 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        if event.type == pygame.MOUSEBUTTONDOWN and hp <= 0 and live:
            hp = hp_r
            mp = 0
            y = y_go
            reset = True
            print('new game')
            hurt_run = False
        if event.type == pygame.KEYDOWN and run_game and lock_fire1:
            if event.key == K_F1 and nguon != 'anh1':   
                if not doi_nv:
                    print('doi nhan vat --> Knight')
                doi_nv = True          
                sl_atr = 5
                sl_atr_e = 8
                sl_id = 12
                nguon = 'anh1'
                skill = 1
                mage_run = False
            if event.key == K_F2 and nguon != 'anh':  
                if not doi_nv:
                    print('doi nhan vat --> Mage')
                k_f = 0
                sl_fire = 0
                doi_nv = True
                sl_atr = 7
                sl_atr_e = 7
                sl_id = 14
                nguon = 'anh'
                skill = 1
                mage_run = True
            if event.key == K_F3 and nguon != 'anh2':   
                if not doi_nv:
                    print('doi nhan vat --> Rogue')
                doi_nv = True          
                sl_atr = 7
                sl_atr_e = 11
                sl_id = 19
                nguon = 'anh2'
                skill = 1
                mage_run = False
        if event.type == pygame.KEYDOWN and lock_idle and lock_attack and lock_attack_extra and lock_death and lock_climb:

            if event.key == K_RIGHT and lock and not run_run and not walk_run:
                walk_run = True
                run_run = False
                flip =False
                right = True
                left =False
                lock = False
                rt_l = True
                rt_l_run = True

            if event.key == K_LEFT and lock and not run_run and not walk_run:
                walk_run = True
                run_run = False
                flip = True
                left = True
                right = False
                lock = False
                rt_r = True
                rt_r_run = True

            if (event.key == K_UP or event.key == K_w) and not jump_run and not hight_jump:
                jump_run = True
                kj = 0
                sl_jump = 7

            if (event.key == K_UP or event.key == K_w) and run_hight:
                jump_run2 += 1

            if event.key == K_g and not idle_run and not jump_run and not hight_jump and not run_attack_run and not walk_attack_run:
                idle_run = True
                lock_idle = False
                k_idle = 0

            if event.key == K_d and lock and not walk_run and not run_run:
                run_run = True
                walk_run = False
                flip =False
                right_run = True
                left_run =False
                lock = False
                rt_l_run = True
                rt_l = True

            if event.key == K_a and lock and not walk_run and not run_run:
                run_run = True
                walk_run = False
                flip = True
                left_run = True
                right_run = False
                lock = False
                rt_r_run = True
                rt_r = True

            if event.key == K_SPACE and skill == 1 and not walk_attack_run and walk_run and not fall_run:
                walk_attack_run = True
                run_walk_attack = False
                r_attack = True

            if event.key == K_SPACE and skill == 1 and not run_attack_run and run_run and lock_jump and not fall_run:
                run_attack_run = True
                run_run_attack = False
                ru_attack = True

            if event.key == K_SPACE and skill == 1 and not attack_run and run_game and lock_jump and not fall_run:
                attack_run = True
                lock_attack = False
                
            if event.key == K_F8:
                ve = not ve
                print('ve :' + str(not ve) + ' --> ' + str(ve))
                if not ve :
                    ve1 = ve
                    print('ve1 :' + str(not ve1) + ' --> ' + str(ve1))
            if event.key == K_F7 and ve:
                ve1 = not ve1
                print('ve1 :' + str(not ve1) + ' --> ' + str(ve1))

            if event.key == K_DOWN or event.key == K_s or event.key == K_F9:
                skill += 1
                if skill == 3:
                    skill = 1
                print('skill :' + str(skill))

            if event.key == K_SPACE and skill == 2 and not attack_extra_run and lock_jump and mp >= 100 and not fire_extra_run:
                mp -= 100
                attack_extra_run = True
                lock_attack_extra = False
                walk_run = False
                jump_run = False
                walk_attack_run = False
                run_attack_run = False
                run_run = False

            if event.key == K_SPACE and skill == 2 and not attack_extra_run and lock_jump and mp < 100:
                ex = 30

            if event.key == K_F10:
                hp -= sleep_hp
                if not hurt_run:
                    hurt_run = True

            if event.key == K_F11:
                push_run = not push_run
                push_jump = not push_jump
                print('push :' + str(not push_run) + ' --> ' + str(push_run))

            if event.key == K_F12 and lock_jump:
                lock_climb = False
                climb_run = True
            
            if event.key == K_k and not run_chest:
                run_chest = True

        if event.type == pygame.KEYUP:
            lock = True
            rq = True

            if event.key == K_RIGHT:
                walk_run = False
                right = False
                run_push = False

            if event.key == K_d:
                run_run = False
                right_run = False
                run_push = False

            if event.key == K_LEFT:
                walk_run = False
                left =False
                run_push = False

            if event.key == K_a:
                run_run = False
                left_run =False
                run_push = False

    pygame.display.flip()
pygame.quit()