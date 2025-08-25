import pygame , sys ,random
class Crosshair (pygame.sprite.Sprite) :
    def __init__(self,picture_path):
        super().__init__()
        self.image =pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot =pygame.mixer.Sound("gunshot.mp3")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,targetGroup,True)
    def update(self):
        self.rect.center =pygame.mouse.get_pos()
class Target (pygame.sprite.Sprite) :
    def __init__(self,picture_path,posX,posY):
        super().__init__()
        self.image =pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center =[posX,posY]
class GameState():
    def __init__(self):
        self.state = 'intro'
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'
        pygame.display.flip()
        screen.blit(background, (0, 0))
        screen.blit(text_ready,(screen_heigh/2 -109,screen_wiht/2 -40))

        crosshair_group.draw(screen)
        crosshair_group.update()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
        pygame.display.flip()
        screen.blit(background, (0, 0))
        targetGroup.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
    def state_manger(self):
        if self.state == 'intro' :
            self.intro()
        if self.state == 'main_game':
            self.main_game()




#screen
pygame.init()
clock =pygame.time.Clock()
game_state =GameState()
screen_wiht =720
screen_heigh =1024
screen =pygame.display.set_mode((screen_heigh,screen_wiht))
background =pygame.image.load("bg.png")
pygame.mouse.set_visible(False)
text_ready =pygame.image.load("text_ready.png")
#crosshair
crosshair = Crosshair("crosshair.png")
crosshair_group =pygame.sprite.Group()
crosshair_group.add(crosshair)

#target
targetGroup =pygame.sprite.Group()
for target in range(38):
    new_target =Target("target.png",random.randrange(0,screen_heigh),random.randrange(0,screen_wiht))
    targetGroup.add(new_target)
while True:
    game_state.state_manger()
    clock.tick(60)