import math
import pygame,sys
from bullet import Bullet
from mega_bullet import Mega_Bullet as Mbullets
from alien import Alien
from time import sleep
def check_updata(ship,ai_sett,screen,stats,paly_button,story_button,bullets,Mbullet,alien,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            keydown_event(ship,event,ai_sett,screen,bullets,Mbullet)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_sett,screen,stats,paly_button,mouse_x, mouse_y,bullets,Mbullet,alien,ship,sb)
            check_story_button(ai_sett,screen,mouse_x,mouse_y,story_button,stats)
        elif event.type ==pygame.KEYUP:
            keyup_event(ship,event)
def keyup_event(ship,event):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key ==pygame.K_UP:
            ship.moving_up =False
        elif event.key==pygame.K_DOWN:
            ship.moving_down=False
def keydown_event(ship ,event,ai_sett,screen,bullets,Mbullet):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==pygame.K_UP:
        ship.moving_up =True
    elif event.key ==pygame.K_DOWN:
        ship.moving_down =True
    elif event.key == pygame.K_SPACE and ai_sett.bullet_allowed >len(bullets):
        new_bullet =Bullet(ai_sett,screen,ship)
        bullets.add(new_bullet)
    elif event.key ==pygame.K_c:
        new_bullet2 = Mbullets(ai_sett, screen, ship)
        Mbullet.add(new_bullet2)
def updata_screen(ai_sett,screen,ship,bullets,Mbullets,aliens,stats,play_button,story_button,sb):
    # fill color to background
    screen.fill(ai_sett.bg_color)
    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for Mbullets in Mbullets.sprites():
        Mbullets.draw_bullet()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
        #story_button.draw_button()
    pygame.display.flip()
def check_play_button(ai_settings,screen,stats, play_button, mouse_x, mouse_y,bullet,Mbullet,alien,ship,sb):
    clicked=play_button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not stats.game_active :
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        #empty
        bullet.empty()
        Mbullet.empty()
        alien.empty()
        create_fleet(ai_settings,screen,alien,ship)
        ship.center_ship()
def check_story_button(ai_settings,screen,mousex,mousey,story_button,state):
        clicked=story_button.rect.collidepoint(mousex,mousey)
        if clicked and not state.game_active:
            screen.fill('black')
def ubdata_bullets(ai_settings,screen,ship,bullets,Mbullet,aliens,stats,sb):
    bullets.update()
    Mbullet.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for mbullet in Mbullet.copy():
        if mbullet.rect.bottom <= 0:
            Mbullet.remove(mbullet)
    check_collsiton_bullet_alien(ai_settings,screen,ship,bullets,Mbullet,aliens,stats,sb)

def check_collsiton_bullet_alien(ai_settings,screen,ship,bullets,Mbullet,aliens,stats,sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions2 = pygame.sprite.groupcollide(Mbullet, aliens, False, True)
    if collisions or collisions2:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        for aliens in collisions2.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        bullets.empty()
        Mbullet.empty()
        stats.level += 1
        sb.prep_level()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets,Mbullet,sb):
    if stats.ship_left >0:
        stats.ship_left -= 1
        aliens.empty()
        sb.prep_ships()
        bullets.empty()
        Mbullet.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def update_alien(ai_settings,stats,screen,aliens,ship,bullets,Mbullets,sb):
    check_fleet_edge(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,Mbullets,sb)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,Mbullets,sb)
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,Mbullet,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets,Mbullet,sb)
            break
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 1.5 * alien_width
    number_aliens_x = int(available_space_x / (1.9 * alien_width))
    return number_aliens_x
def create_alien(ai_settings, screen, aliens, alien_number,row_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y =alien.rect.height +2*alien.rect.height*row_num
    aliens.add(alien)
def num_of_rows(ai_settings,alien_heigh,ship_height):
    avliable_space =ai_settings.screen_height -3*alien_heigh -ship_height
    num_rows =avliable_space/(alien_heigh*2)
    return num_rows

def create_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings, screen)
    number_aliens_x =get_number_aliens_x(ai_settings,alien.rect.width)
    num_row=math.floor(num_of_rows(ai_settings,alien.rect.height,ship.rect.height))
    # Create the first row of aliens.
    for num_of_row in range(num_row):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings,screen,aliens,alien_number,num_of_row)
def check_fleet_edge(ai_sett,aliens):
    for alien in aliens:
        if alien.check_edge():
            change_fleet_direction(ai_sett,aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
       alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
