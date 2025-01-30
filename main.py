import pygame as pg
from settings import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)


running = True
while running:

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)
