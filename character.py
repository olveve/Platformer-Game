import pygame as pg
from settings import *
from assets import *

class Character:
    def __init__(self, x, y, vx):
        self.x = x
        self. y = y
        self.vx = vx
        self.vy = 0
        self.jump = -22
        self.width = 64
        self.height = 64
        self.color = (255, 0, 0)
        self.following = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # TODO: Draw the image of the character using blit
        # screen.blit(self.image, (self.x, self.y))

    def movement(self):
        screen_scroll = 0
        self.vy += GRAVITY
        self.y += self.vy

        if self.y > HEIGHT - (self.height + 67):
            self.y = HEIGHT - (self.height + 67)
            self.vy = 0


        # Oppdatere screen_scroll basert på x-posisjonen til spilleren
        # if self.char_type == "samurai":



class Samurai(Character):
    def __init__(self, x, y, vx):
        super().__init__(x, y, vx)
        self.color = (0, 255, 0)
        # TODO: Set self.image to the image of the samurai


    def movement(self):
        super().movement()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_UP]:
            if self.y == HEIGHT - (self.height + 67):
                self.vy = self.jump
        """""
        if keys_pressed[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
            
        if keys_pressed[pg.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vx
        """



class Enemy(Character):
    def __init__(self, x, y, vx):
        super().__init__(x, y, vx)
        # TODO: Set self.image to the image of the enemy

    def movement(self, is_scrolling, scroll):
        if not is_scrolling:
            super().movement()
            distance_to_person = abs(self.x - person.x)
            if distance_to_person <= 300:
                self.following = True
            if self.following:
                if self.x < person.x:
                    self.x += self.vx
                if self.x > person.x:
                    self.x -= self.vx


person = Samurai(100, 100, 7)
enemy = Enemy(800, 100, 2)