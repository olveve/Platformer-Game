import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import draw_bg_base, draw_fg, draw_fuji
from character import create_characters

world_length = 5 * WIDTH
person, enemies = create_characters(world_length)
scroll = 0
bg_scroll = 0
scroll_threshold = 200

# Reell posisjon i verden
person.world_x = person.x  

running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)
    keys = pg.key.get_pressed()
    scrolling = ""  # for scroll retningen

    if keys[pg.K_RIGHT]:
        if person.world_x + person.vx <= world_length - person.width:
            person.world_x += person.vx
        else:
            person.world_x = world_length - person.width

        if person.world_x - scroll > WIDTH - scroll_threshold and scroll < world_length - WIDTH:
            scroll = person.world_x - (WIDTH - scroll_threshold)
            bg_scroll = scroll
            scrolling = "R"

    if keys[pg.K_LEFT]:
        if person.world_x - person.vx >= 0:
            person.world_x -= person.vx
        else:
            person.world_x = 0

        if person.world_x - scroll < scroll_threshold and scroll > 0:
            scroll = person.world_x - scroll_threshold
            bg_scroll = scroll
            scrolling = "L"

    person.x = person.world_x - scroll

    # KAN MULIG FJERNES: siden vi har world.x nå
    if person.x < 0:
        person.x = 0
    if person.x > world_length - person.width:
        person.x = world_length - person.width

    draw_bg_base(screen, scroll)
    draw_fuji(screen, scroll)
    draw_fg(screen, scroll)
    person.movement()
    person.draw(screen)

    if enemies:
        enemy_factor = enemies[0].vx / person.vx
    else:
        enemy_factor = 1

    speed = -person.vx
    if scrolling == "R":
        speed = -person.vx * enemy_factor
    elif scrolling == "L":
        speed = person.vx * enemy_factor

    for enemy in enemies:
        enemy.movement(scrolling, speed)
        enemy.draw(screen)
    
    pg.display.update()

pg.quit()