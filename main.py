import pygame, sys
from spaceship import Spaceship

pygame.init()

screen_x = 750

screen_y = 700

GREY = (10, 25, 25)

SCREEN = pygame.display.set_mode((screen_x, screen_y))

#objects

spaceship = Spaceship(screen_x, screen_y)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

pygame.display.set_caption("Python Invaders")   

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    #update movements
    spaceship_group.update()

    #draw
    SCREEN.fill(GREY)
    spaceship_group.draw(SCREEN)
    spaceship_group.sprite.laser_groups.draw(SCREEN)

    #clock - must be at bottom
    pygame.display.update()
          
    clock.tick(60)





