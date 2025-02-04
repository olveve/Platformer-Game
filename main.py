import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import *
from character import *

scroll = 0

running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    scroll -= person.vx if pg.key.get_pressed()[pg.K_RIGHT] else 0
    scroll += person.vx if pg.key.get_pressed()[pg.K_LEFT] else 0


    draw_bg(screen, scroll)
    person.movement()
    person.draw(screen)
    enemy.draw(screen)
    enemy.movement()
    
    pg.display.update()

pg.quit()
