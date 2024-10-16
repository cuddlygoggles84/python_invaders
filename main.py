import pygame, sys, random
from game import Game

pygame.init()

screen_x = 750

screen_y = 700

GREY = (10, 25, 25)

SHOOT_LASER = pygame.USEREVENT

MYSTER_SHIP = pygame.USEREVENT + 1


pygame.time.set_timer(MYSTER_SHIP, random.randint(4000, 8000))

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

        if event.type == MYSTER_SHIP:
            game.spawn_mystery_ship()
            pygame.time.set_timer(MYSTER_SHIP, random.randint(4000, 8000))

    #update movements
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()
    game.mystery_ship_group.update()
    game.check_for_collisions()
    

    #draw
    SCREEN.fill(GREY)
    game.spaceship_group.draw(SCREEN)
    game.spaceship_group.sprite.lasers_group.draw(SCREEN)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(SCREEN)
    game.aliens_group.draw(SCREEN)
    game.alien_lasers_group.draw(SCREEN)
    game.mystery_ship_group.draw(SCREEN)

    #clock - must be at bottom
    pygame.display.update()
          
    clock.tick(60)





