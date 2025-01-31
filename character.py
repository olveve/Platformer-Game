import pygame as pg
from settings import *
from assets import *

class Samurai:
    def __init__(self, x, y, char_type, vx):
        self.x = x
        self. y = y
        self.char_type = char_type
        self.vx = vx
        self.vy = 0
        self.jump = -22
        self.width = 64
        self.height = 64
        self.color = (255, 0, 0)
        self.following = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def movement(self):
        screen_scroll = 0
        self.vy += GRAVITY
        self.y += self.vy

        if self.y > HEIGHT - (self.height + 67):
            self.y = HEIGHT - (self.height + 67)
            self.vy = 0

        if self.char_type == "samurai":
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
                if self.y == HEIGHT - (self.height + 67):
                    self.vy = self.jump

        if self.char_type == "ai":
            distance_to_person = abs(self.x - person.x)
            if distance_to_person <= 100:
                self.following = True
            if self.following:
                if self.x < person.x:
                    self.x += self.vx
                if self.x > person.x:
                    self.x -= self.vx
        
        # Oppdatere screen_scroll basert på x-posisjonen til spilleren
        # if self.char_type == "samurai":


person = Samurai(100, 100, "samurai", 10)
enemy = Samurai(800, 100, "ai", 2)