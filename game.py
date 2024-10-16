import pygame, random
from spaceship import Spaceship, Lasers
from obstacle import Obstacle
from obstacle import grid
from alien import Alien, Mystery_Ship
from lasers import Lasers

class Game:
    def __init__(self, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_x, self.screen_y))
        self.obstacles = self.spawn_obstacle()
        self.aliens_group = pygame.sprite.Group()
        self.spawn_aliens()
        self.alien_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()

    def spawn_obstacle(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_x - (4 * obstacle_width)) / 5
        obstacles = []
        for _ in range(4):
            offset_x = (_ + 1) * gap + _ * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_y - 100)
            obstacles.append(obstacle)
        return obstacles
    
    def spawn_aliens(self):
        for row in range(5):
            for column in range(11):
                cell_size = 55
                x = 75 + column * cell_size
                y = 110 + row * cell_size
                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                elif row in (3,4):
                    alien_type = 1
                alien = Alien(alien_type, x, y)
                self.aliens_group.add(alien)
    
    def move_aliens(self):
        self.aliens_group.update(self.alien_direction)
        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_x:
                self.alien_direction = -1
                self.move_aliens_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.move_aliens_down(2)

    def move_aliens_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Lasers(random_alien.rect.center, -6, self.screen_y)
            self.alien_lasers_group.add(laser_sprite)

    def spawn_mystery_ship(self):
        self.mystery_ship_group.add(Mystery_Ship(self.screen_x))

    def check_for_collisions(self):
        #Check for Spaceship Laser collsions
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True):
                    laser_sprite.kill()
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    laser_sprite.kill()
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
        
        #Check for Alien Laser collisions

        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

            if self.aliens_group:
                for alien in self.aliens_group:
                    for obstacle in self.obstacles:
                        pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

            


        








            

