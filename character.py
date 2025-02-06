import pygame as pg
from settings import *
from assets import *

class Character:
    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = 0
        self.jump = -22
        self.width = 64
        self.height = 64
        self.color = (255, 0, 0)
        self.following = False
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        # TODO: Draw the image of the character using blit
        # screen.blit(self.image, (self.x, self.y))

    def movement(self):
        self.vy += GRAVITY
        self.y += self.vy

        if self.y > HEIGHT - (self.height + 67):
            self.y = HEIGHT - (self.height + 67)
            self.vy = 0

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
        if keys_pressed[pg.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vx
        if keys_pressed[pg.K_UP]:
            if self.y == HEIGHT - (self.height + 67):
                self.vy = self.jump

        # Oppdatere rektangelet basert på spillerens posisjon
        self.rect.topleft = (self.x, self.y)

class Samurai(Character):
    def __init__(self, x, y, vx):
        super().__init__(x, y, vx)
        self.color = (0, 255, 0)
        # TODO: Set self.image to the image of the samurai

class Enemy(Character):
    def __init__(self, x, y, vx, target, world_length):
        super().__init__(x, y, vx)
        self.target = target
        self.world_length = world_length
        # TODO: Set self.image to the image of the enemy

    def movement(self, scrolling, scroll):
        self.vy += GRAVITY
        self.y += self.vy

        if self.y > HEIGHT - (self.height + 67):
            self.y = HEIGHT - (self.height + 67)
            self.vy = 0

        if not scrolling:
            distance_to_person = abs(self.x - self.target.x)
            if distance_to_person <= 300:
                self.following = True
            if self.following:
                if self.x < self.target.x:
                    self.x += self.vx
                if self.x > self.target.x:
                    self.x -= self.vx
        else:
            self.x += scroll  # Adjust enemy position based on scroll

        # Ensure the enemy doesn't move beyond the world boundaries
        if self.x < 0:
            self.x = 0
        if self.x > self.world_length - self.width:
            self.x = self.world_length - self.width

        # Oppdatere rektangelet basert på fiendens posisjon
        self.rect.topleft = (self.x, self.y)

def create_characters(world_length):
    person = Samurai(100, 100, 7)
    enemy = Enemy(800, 100, 2, person, world_length)
    return person, enemy