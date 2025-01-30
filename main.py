import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import *
from character import Samurai

person = Samurai(100, 100)


running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    draw_bg(screen)
    person.movement()
    person.draw(screen)
    
    pg.display.update()

pg.quit()
