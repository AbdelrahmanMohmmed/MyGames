import pygame
class Fighter():
    def __init__(self,player,x,y,flip,data,sprite_sheet,animation_steps):
        self.player =player
        self.size =data[0]
        self.image_scale =data[1]
        self.flip =flip
        self.ubdate_time =pygame.time.get_ticks()
        self.animation_list =self.load_image(sprite_sheet,animation_steps)
        self.action =0 # 1.idle 2.walk 3.attack  6.hit 7.death 4.attack2 8.spcial 5.jumb
        self.frame_index =0
        self.image =self.animation_list[self.action][self.frame_index]
        self.rect =pygame.Rect(x,y,80,180)
        self.vel_y=0
        self.jump =False
        self.running =False
        self.attacking =False
        self.style_attack=0
        self.health =160
        self.attacking_cooldown =0
        self.hit =False
        self.alive =True
    def load_image(self,sprite_sheet,sprite_animat):
         animation_list =[]
         for y, animation in enumerate(sprite_animat):
             temp_img_list = []
             for x in range(animation):
                 temp_img = sprite_sheet.subsurface(x * self.size, y *self.size, self.size, self.size)
                 temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale)))
             animation_list.append(temp_img_list)
         return animation_list
    def move(self,wind_wight,wind_high,target,round_over):
        speed =10
        gravity =2
        dx=0
        dy=0
        self.running =False
        self.style_attack = 0
        key =pygame.key.get_pressed()
        if self.attacking ==False and self.alive ==True and round_over ==False:
            #control 1 player
            if self.player ==1:
                if key[pygame.K_a]:
                    dx = -speed
                    self.running = True
                if key[pygame.K_d]:
                    dx = speed
                    self.running = True
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -40
                    self.jump = True
                # attack
                if key[pygame.K_k] or key[pygame.K_l]:
                    self.attack( target)
                    if key[pygame.K_k]:
                        self.style_attack = 1
                    if key[pygame.K_l]:
                        self.style_attack = 2
             # control 2 player
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -speed
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = speed
                    self.running = True
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -40
                    self.jump = True
                # attack
                if key[pygame.K_n] or key[pygame.K_m]:
                    self.attack( target)
                    if key[pygame.K_n]:
                        self.style_attack = 1
                    if key[pygame.K_m]:
                         self.style_attack = 2
        self.vel_y += gravity
        dy += self.vel_y
        if self.rect.left +dx <0 :
          dx=  -self.rect.left
        if self.rect.right +dx > wind_wight:
            dx =wind_wight -self.rect.right
        if self.rect.bottom +dy >wind_high -100:
            self.vel_y =0
            dy =wind_high -100 -self.rect.bottom
            self.jump =False
        if target.rect.centerx > self.rect.centerx:
            self.flip =False
        else:
            self.flip =True
        if self.attacking_cooldown >0 :
            self.attacking_cooldown -=1
        self.rect.x += dx
        self.rect.y += dy
    def ubdate(self):
        if self.health <=0:
           self.health =0
           self.alive =False
           self.ubdate_action(6)
        elif self.hit ==True:
            self.ubdate_action(5)
        elif self.attacking ==True:
            if self.style_attack == 1:
                self.ubdate_action(4)
            elif self.style_attack == 2:
                self.ubdate_action(3)
        elif self.jump ==True:
            self.ubdate_action(4)
        elif self.running ==True:
            self.ubdate_action(1)
        else:
            self.ubdate_action(0)
        animation_cooldown=100
        self.image=self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.ubdate_time >animation_cooldown:
            self.frame_index +=1
            self.ubdate_time =pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive ==False:
                self.frame_index =len(self.animation_list[self.action]) -1
            else:
                self.frame_index = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attacking_cooldown = 30
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attacking_cooldown = 30

    def attack(self,target):
       if self.attacking_cooldown ==0 :
           self.attacking = True
           attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y,
                                        2 * self.rect.width, self.rect.height)
           if attacking_rect.colliderect(target):
               target.health -= 20
               target.hit =True

    def ubdate_action(self,new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index =0
            self.ubdate_time =pygame.time.get_ticks()
    def draw(self,surface):
        img =pygame.transform.flip(self.image,self.flip,False)
        surface.blit(img ,(self.rect.x,self.rect.y))
