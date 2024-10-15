import pygame, random

class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        path = f"sprites/alien_{type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, direction):
        self.rect.x += direction

class Mystery_Ship(pygame.sprite.Sprite):
    def __init__(self, screen_x):
        super().__init__()
        self.image = pygame.image.load("sprite/spaceship")
        self.screen_x = screen_x

        x = random.choice([0,self.screen_x - self.image.get_width()])   

        self.rect = self.image.get_rect(topleft=(x,40))
        self.speed = 5

    def update(self):
        self.rect += self.speed