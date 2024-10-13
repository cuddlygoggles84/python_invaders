import pygame

YELLOW = (243, 216, 63)

class Lasers(pygame.sprite.Sprite):
    def __init__(self, position,speed, screen_y):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((YELLOW))
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_y = screen_y

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_y + 15 or self.rect.y < 0:
            self.kill()


