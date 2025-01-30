import pygame as pg
from settings import *
from assets import *

class Samurai:
    def __init__(self, x, y):
        self.x = x
        self. y = y
        self.vx = 5
        self.vy = 0
        self.jump = -5
        self.width = 64
        self.height = 64
        self.color = (255, 0, 0)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def movement(self):
        self.vy += GRAVITY
        self.y += self.vy

        #if not self.dead and self.y > HEIGHT - self.height:
        self.y = HEIGHT - self.height
        self.vy = 0

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
            #self.frame_counter += 1
            #self.image = #mario_sprites_left[(self.frame_counter // 3) % len(mario_sprites_left)]
        if keys_pressed[pg.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vx
            #self.frame_counter += 1 
            # (self.frame_counter + 1) % len(mario_sprites)
            #self.image = mario_sprites[ (self.frame_counter // 3) % len(mario_sprites) ]
        if keys_pressed[pg.K_UP]:
            if self.vy == 0:
                self.vy = self.jump
        