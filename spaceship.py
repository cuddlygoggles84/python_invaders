import pygame

class Spaceship (pygame.sprite.Sprite):
    def __init__(self, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        super().__init__()
        self.image = pygame.image.load("sprites/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_x/2,self.screen_y))
        self.speed = 6
    

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys [pygame.K_LEFT]:
            self.rect.x -= self.speed

    
    def update(self):
        self.get_user_input()
        self.movement_constraints

    def movement_constraints(self):
        if self.rect.right > self.screen_x:
            self.rect.right = self.screen_x
        if self.rect.left < 0:
            self.rect.left = 0
            


    







