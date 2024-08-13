from scoreboard import Scoreboard
import pygame
import  functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button

def run_game():
    # initilize window with title
    pygame.init()
    ai_sett=Settings()
    screen=pygame.display.set_mode((ai_sett.screen_width,ai_sett.screen_height))
    pygame.display.set_caption("Alien game")
    stats = GameStats(ai_sett)
    sb = Scoreboard(ai_sett, screen, stats)
    ship =Ship(screen,ai_sett)
    play_button =Button(ai_sett,screen,"play",ai_sett.starty)
    story_button=Button(ai_sett,screen,"story",ai_sett.storyy)
    bullets=Group()
    Mbullets=Group()
    #alien =Alien(ai_sett,screen)
    aliens =Group()
    gf.create_fleet(ai_sett, screen, aliens,ship)
    while True:
        #checks for player input
        gf.check_updata(ship, ai_sett, screen,stats,play_button,story_button, bullets,Mbullets,aliens,sb)
        #updates the position of the ship
        if stats.game_active:
            ship.update()
            # ubdate any bullets that have been fired
            gf.ubdata_bullets(ai_sett, screen, ship, bullets, Mbullets, aliens,stats,sb)
            gf.update_alien(ai_sett, stats, screen, aliens, ship, bullets, Mbullets,sb)
        #updated positions to draw a new screen
        gf.updata_screen(ai_sett, screen, ship, bullets,Mbullets, aliens,stats,play_button,story_button,sb)

run_game()


