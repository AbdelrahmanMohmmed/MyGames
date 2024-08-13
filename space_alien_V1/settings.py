class Settings():
    def __init__(self):
       self.screen_width = 1024
       self.screen_height = 720
       self.bg_color = (130, 230, 230)
       self.moving_speed =4
       # Bullet settings
       self.bullet_speed_factor = 4
       self.bullet_width = 8
       self.bullet_height = 15
       self.bullet_color = (100,0,20)
       self.bullet_allowed =6
       # Mega_bullet
       self.Mbullet_width=500
       self.Mbullet_height=40
       self.Mbullet_color=(100,255,20)
       self.Mbullet_speed_factor=10
       #alien settings
       self.alien_speed_factor = 1
       self.fleet_drop_speed = 5
       # fleet_direction of 1 represents right; -1 represents left.
       self.fleet_direction = 1
       self.ship_limit =3
       self.speedup_scale = 1.15
       self.score_scale = 1.5
       #button
       self.storyy= self.screen_width / 3
       self.starty = self.screen_height / 4
       self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
      self.ship_speed_factor = 4
      self.bullet_speed_factor = 4
      self.alien_speed_factor = 1
      self.fleet_direction = 1
      # Scoring
      self.alien_points = 50
    def increase_speed(self):
      """Increase speed settings."""
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale
      self.alien_speed_factor *= self.speedup_scale
      self.alien_points = int(self.alien_points * self.score_scale)


