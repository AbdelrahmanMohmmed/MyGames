import pygame
from pygame.sprite import Sprite
class Ship(Sprite):

    def __init__(self,screen,ai_sett):
        super(Ship, self).__init__()
        self.screen =screen
        self.ai_sett =ai_sett
        #load image
        self.image =pygame.image.load('image/space-ship.png')
        # make it smaller
        defult_size =(60,80)
        self.image =pygame.transform.scale(self.image,defult_size)
        self.rect =self.image.get_rect()
        self.screen_rect =screen.get_rect()

        #start ship at the bottom center
        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center =float(self.rect.centerx)
        self.centery =float(self.rect.bottom)
        self.moving_right =False
        self.moving_left =False
        self.moving_up=False
        self.moving_down=False
    def update(self):
        if self.moving_right and self.rect.right <self.screen_rect.right :
            self.center += self.ai_sett.moving_speed
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_sett.moving_speed
        self.rect.centerx =self.center
        if self.moving_up and self.rect.top >0:
            self.centery -=self.ai_sett.moving_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery +=self.ai_sett.moving_speed
        self.rect.bottom=self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom
