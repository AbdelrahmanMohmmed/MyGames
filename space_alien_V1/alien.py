import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
     def __init__(self, ai_settings, screen):
         super(Alien, self).__init__()
         self.screen = screen
         self.ai_settings = ai_settings
         # Load the alien image and set its rect attribute.
         self.image = pygame.image.load('image/ufo.png')
         # make it smaller
         defult_size = (90, 60)
         self.image = pygame.transform.scale(self.image, defult_size)
         self.rect = self.image.get_rect()
         self.rect.x =self.rect.width/10
         self.rect.y =self.rect.height/3
         self.x =float(self.rect.x)
     def blitme(self):
         self.screen.blit(self.image,self.rect)
     def update(self):
         self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
         self.rect.x = self.x
     def check_edge(self):
         screen_rect =self.screen.get_rect()
         if self.rect.right>=screen_rect.right:
             return True
         elif self.rect.left<=0:
             return True
