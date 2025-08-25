import time ,math
import pygame ,sys ,random
from random import  randint

def obtical_movement(obtical_list):
    if obtical_list:
        for obtical_rect in obtical_list:
            obtical_rect.x -= 5
            if obtical_rect.bottom ==500:
                screen.blit(enemy_snail1, obtical_rect)
            else:
                screen.blit(fly_surf, obtical_rect)

        obtical_list = [obtical for obtical in obtical_list if obtical.x > -100]
        return obtical_list
    else:
        return []
def player_animition ():
    global player,player_index
    if player_rect.bottom <500:
        player =player_jumb
    else:
        player_index +=0.15
        if player_index > len(player_walk):
            player_index=0
        player =player_walk[int(player_index)]
def collaps (player,obtical):
    if obtical :
        for obtical_rect in obtical:
            if player.colliderect(obtical_rect): return False
    return True
def display_score():
    current_time = int(pygame.time.get_ticks()/1000)  - start_time
    score = pygame.font.Font("font/type.ttf", 30)
    score_surfce = score.render(f'score : {current_time}', False, (64, 64, 64))
    score_rect = score_surfce.get_rect(topright=(750, 0))
    screen.blit(score_surfce, score_rect)
    return current_time
def max_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    max_time =0
    if max_time <= current_time:
        max_time = current_time

    max_score =pygame.font.Font("font/type.ttf", 60)
    max_score_surf =max_score.render(f'high score :{max_time}', False, 'blue')
    max_score_rect =max_score_surf.get_rect(bottomleft=(250,490))
    screen.blit(max_score_surf,max_score_rect)
def intro_game():
    text = pygame.font.Font("font/type.ttf", 50)

    gamename_surf =text.render('Super Runner',False,(111,196,169))
    gamename_rect =gamename_surf.get_rect(topleft=(280, 100))

    player_stand =pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
    player_stand =pygame.transform.rotozoom(player_stand,0,3)
    player_stand_rect =player_stand.get_rect(center=(410,300))

    press_surf =text.render('press space to start', False, (111,196,169))
    press_rect =press_surf.get_rect(bottomleft=(250,490))
    screen.blit(press_surf,press_rect)

    screen.blit(player_stand,player_stand_rect)
    screen.blit(gamename_surf,gamename_rect)
def game_over():

   gameover_surf = pygame.image.load("graphics/text_gameover.png")
   gameover_rect = gameover_surf.get_rect(topleft=(250, 100))
   player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
   player_stand = pygame.transform.rotozoom(player_stand, 0, 3)
   player_stand_rect = player_stand.get_rect(center=(410, 300))

   screen.blit(player_stand, player_stand_rect)
   screen.blit(gameover_surf,gameover_rect)

pygame.init()
#screen game and setup
widh =800
high = 600
screen =pygame.display.set_mode((widh,high))
pygame.display.set_caption('Crazy Run')
clock =pygame.time.Clock()
game_active =False
start_time =0
score =0

#backgroubd
background = pygame.image.load("picture/backgrounds.png").convert()
ground =pygame.image.load("picture/ground.png").convert()
background_sound =pygame.mixer.Sound('audio/music.wav')
background_sound.play(loops=-1)
scroll =0
scroll2 =0
bg_wiegh =background.get_width()
ground_width =ground.get_width()
#enemy
obtical_rect_list =[]
enemy_snail_animate1 =pygame.image.load("graphics/snail/snail1.png").convert_alpha()
enemy_snail_animate2 =pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_index =0
snail_frames =[enemy_snail_animate1,enemy_snail_animate2]
enemy_snail1 = snail_frames[snail_index]

fly_1 =pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_2 =pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frames =[fly_1,fly_2]
fly_index =0
fly_surf =fly_frames[fly_index]
#player
player_walk_1 =pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 =pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_index=0
player_walk =[player_walk_1,player_walk_2]
player_jumb =pygame.image.load("graphics/Player/jump.png").convert_alpha()
player =player_walk[player_index]
player_godown =0
player_rect =player.get_rect(midbottom=(100,500 +player_godown))
player_gravity =0
jump_count = 0
max_jumps = 1
player1 =pygame.sprite.GroupSingle()
#player1.add(Player())
jump_sound =pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.4)
#timer
if score > 50 and score <100 :
    obtical_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obtical_timer, 880)
    max_jumps=5
elif score >= 100:
    obtical_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obtical_timer, 680)
    max_jumps=10
else:
    obtical_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obtical_timer, 1280)
snail_animation_timer =pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,500)
fly_animation_timer =pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #obtical
        if game_active:
            if event.type == obtical_timer:
                if randint(0, 2):
                    obtical_rect_list.append(enemy_snail1.get_rect(bottomright=(randint(800, 900), 500)))
                else:
                    obtical_rect_list.append(fly_surf.get_rect(bottomright=(randint(800, 900), 440)))

            if event.type == snail_animation_timer:
                if snail_index ==0 :snail_index=1
                else: snail_index =0
                enemy_snail1 =snail_frames[snail_index]
            if event.type == fly_animation_timer:
                if fly_index ==0 :fly_index=1
                else:fly_index=0
                fly_surf =fly_frames[fly_index]

        # keyinput test
        if event.type ==pygame.MOUSEBUTTONDOWN and player_rect.bottom >=500:
            player_gravity =-20
    if game_active  :
            # draw all elements
        screen.fill('black')
        for i in range (0,2):
            screen.blit(background, (i*bg_wiegh +scroll, 0))
        for o in range (0,2):
            screen.blit(ground, (o * ground_width + scroll2, 500))
        if score > 50 and score <100 :
            scroll -= 8
            scroll2 -= 8
        elif score >= 100 :
            scroll -= 12
            scroll2 -= 12
        else:
            scroll -= 5
            scroll2 -= 5
        if abs(scroll) > bg_wiegh :
            scroll=0
        if abs(scroll2) > ground_width:
            scroll2 =0
        # score
        score =display_score()
        # enemy
        obtical_rect_list= obtical_movement(obtical_rect_list)
     # player
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and jump_count < max_jumps:
                player_gravity =-22 #jump value
                jump_sound.play()
                jump_count += 1
       # if key[pygame.K_s] and player_rect.bottom <= 500 :
           # player_godown = 50
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 500:
            player_rect.bottom = 500
            jump_count = 0
        player_animition()
        screen.blit(player, player_rect)

        # collid
        game_active =collaps(player_rect,obtical_rect_list)
    else:
        screen.fill((94,129,162))
        key = pygame.key.get_pressed()
        obtical_rect_list.clear()
        player_gravity =0
        player_rect.midbottom =(100,500)
        if score ==0:
            intro_game()
        else:
            game_over()
            max_score = pygame.font.Font("font/type.ttf", 60)
            max_score_surf = max_score.render(f'your score : {score}', False, (111,196,169))
            max_score_rect = max_score_surf.get_rect(bottomleft=(250, 490))
            screen.blit(max_score_surf, max_score_rect)

        if key[pygame.K_SPACE] :
            game_active =True

            start_time =int(pygame.time.get_ticks() /1000)

    clock.tick(60)
    pygame.display.update()