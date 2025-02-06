import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import *
from character import *

scroll = 0
scroll_threshold = 300

running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    keys = pg.key.get_pressed()
    is_scrolling = False
    if keys[pg.K_RIGHT]:
        if person.x > WIDTH - scroll_threshold:
            scroll += person.vx
            is_scrolling = True
        else:
            person.x += person.vx

    if keys[pg.K_LEFT]:
        if person.x < scroll_threshold:
            scroll -= person.vx
            is_scrolling = True
        else:
            person.x -= person.vx


    draw_bg(screen, scroll)
    person.movement()
    person.draw(screen)
    enemy.draw(screen)
    enemy.movement(is_scrolling, scroll)
    
    pg.display.update()

pg.quit()
