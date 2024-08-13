import pygame
import bullet
from pygame.sprite import Sprite
class Mega_Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Mega_Bullet, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.Mbullet_width, ai_settings.Mbullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet as deimal
        self.y = float(self.rect.y)
        self.color = ai_settings.Mbullet_color
        self.speed_factor = ai_settings.Mbullet_speed_factor
    def update(self):
        self.y -=self.speed_factor
        self.rect.y =self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
