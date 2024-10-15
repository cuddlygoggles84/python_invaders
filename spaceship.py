import pygame, time
from lasers import Lasers


class Spaceship (pygame.sprite.Sprite):
    def __init__(self, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        super().__init__()
        self.image = pygame.image.load("sprites/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_x/2,self.screen_y))
        self.speed = 6
        self.laser_groups = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 400

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys [pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys [pygame.K_SPACE] and self.laser_ready == True:
            self.laser_ready = False
            laser = Lasers(self.rect.center, 5, self.screen_y)
            self.laser_groups.add(laser)
            self.laser_time = pygame.time.get_ticks()

    def update(self):
        self.get_user_input()
        self.movement_constraints()
        self.laser_groups.update()
        self.recharge_laser()

    def movement_constraints(self):
        if self.rect.right > self.screen_x:
            self.rect.right = self.screen_x
        if self.rect.left < 0:
            self.rect.left = 0

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
            


    







