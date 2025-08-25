import pygame
from fighters import Fighter

pygame.init()
#screen
screen_width =1024
screen_hight =720

screen =pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption("Fight")
# intro
into_connt =3
last_count_ubdate =pygame.time.get_ticks()
score =[0,0]
round_over =False
round_over_cooldown=2000
clock= pygame.time.Clock()
fps =60
#info about fighters
cat_size =50
cat_scale =4
cat_data =[cat_size,cat_scale]
skill_size = 60
skull_scale =3
skill_data =[skill_size,skull_scale]
#load image
bg_image =pygame.image.load('9e0a805a0d4420a555df6741aebffd4b.gif').convert_alpha()
victory_img =pygame.image.load('victory.png')
#load fighter sheet
cat_sheet =pygame.image.load('fighters/cat_fighter_sprite1.png').convert_alpha()
skill_sheet =pygame.image.load('fighters/mon2_sprite_base.png').convert_alpha()
#animation steps
cat_animat =[4,2,4,6,1,4,4,6]
skill_animat =[4,4,4,4,1,3,7,7]
#number
counter_font =pygame.font.Font("font/type.ttf",80)
score_font =pygame.font.Font('font/type.ttf',30)
def draw_text(text,font,text_col,x,y):
    img =font.render(text,True,text_col)
    screen.blit(img,(x,y))
def draw_bg():
    scale_bg =pygame.transform.scale(bg_image,(screen_width,screen_hight))
    screen.blit(scale_bg,(0,0))
#draw healthbar
def draw_health(health,x,y):
    ratio = health /160
    pygame.draw.rect(screen, 'white', (x -5, y -5, 410, 35))
    pygame.draw.rect(screen,'red',(x,y,400,30))
    pygame.draw.rect(screen,"yellow",(x,y,400*ratio,30))
#`fighters
fighter_1 =Fighter(1,50,500,False,cat_data,cat_sheet,cat_animat)
fighter_2 =Fighter(2,700,500,True,skill_data,skill_sheet,skill_animat)

#gameloop
run = True
while run:

    clock.tick(60)

    draw_bg()
    if into_connt <=0:
        fighter_1.move(screen_width, screen_hight, fighter_2,round_over)
        fighter_2.move(screen_width, screen_hight,  fighter_1,round_over)
    else:
        draw_text(str(into_connt),counter_font,'red',screen_width/2,screen_hight/2)
        if(pygame.time.get_ticks()-last_count_ubdate) >=1000:
            into_connt -=1
            last_count_ubdate =pygame.time.get_ticks()
    #health
    draw_health(fighter_2.health,600,30)
    draw_health(fighter_1.health, 20, 30)
    draw_text("P1 : "+ str(score[0]),score_font,'red',20,70)
    draw_text("P2 : " + str(score[1]), score_font, 'red', 600, 70)
    #check player defeat
    if round_over ==False:
        if fighter_1.alive ==False:
            score[1] =1
            round_over =True
            round_over_time =pygame.time.get_ticks()
        elif fighter_2.alive ==False:
            score[0] =1
            round_over =True
            round_over_time =pygame.time.get_ticks()
    else:
        screen.blit(victory_img,(100,200))
        if pygame.time.get_ticks() -round_over_time >round_over_cooldown:
            round_over =False
            into_connt =3
            fighter_1 = Fighter(1, 50, 500, False, cat_data, cat_sheet, cat_animat)
            fighter_2 = Fighter(2, 700, 500, True, skill_data, skill_sheet, skill_animat)

    #ubdate
    fighter_1.ubdate()
    fighter_2.ubdate()
    #draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
