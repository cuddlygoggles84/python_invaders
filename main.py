import pygame, sys
from game import Game

pygame.init()

screen_x = 750

screen_y = 700

GREY = (10, 25, 25)

SHOOT_LASER = pygame.USEREVENT

pygame.time.set_timer(SHOOT_LASER, 300)

SCREEN = pygame.display.set_mode((screen_x, screen_y))

#objects

game = Game(screen_x, screen_y)

pygame.display.set_caption("Python Invaders")   

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == SHOOT_LASER:
            game.alien_shoot_laser()

    #update movements
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_groups.update()
    

    #draw
    SCREEN.fill(GREY)
    game.spaceship_group.draw(SCREEN)
    game.spaceship_group.sprite.laser_groups.draw(SCREEN)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(SCREEN)
    game.aliens_group.draw(SCREEN)
    game.alien_lasers_groups.draw(SCREEN)

    #clock - must be at bottom
    pygame.display.update()
          
    clock.tick(60)





