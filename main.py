import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import draw_bg
from character import create_characters

world_length = 5 * WIDTH  # 5 background images width
person, enemies = create_characters(world_length)
scroll = 0
bg_scroll = 0
scroll_threshold = 300

running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    keys = pg.key.get_pressed()
    scrolling = ""
    if keys[pg.K_RIGHT]:
        if person.x > WIDTH - scroll_threshold and scroll < world_length - WIDTH:
            scroll += person.vx
            bg_scroll += person.vx
            person.x = WIDTH - scroll_threshold  # Keep the player at the scroll threshold
            scrolling = "R"
        else:
            person.x += person.vx

    if keys[pg.K_LEFT]:
        if person.x < scroll_threshold and scroll > 0:
            scroll -= person.vx
            bg_scroll -= person.vx
            person.x = scroll_threshold  # Keep the player at the scroll threshold
            scrolling = "L"
        else:
            person.x -= person.vx

    # Ensure the player doesn't move beyond the world boundaries
    if person.x < 0:
        person.x = 0
    if person.x > world_length - person.width:
        person.x = world_length - person.width

    draw_bg(screen, bg_scroll)
    person.movement()
    person.draw(screen)

    speed = -person.vx
    if scrolling == "R":
        speed = -person.vx * (2/7)
    if scrolling == "L":
        speed = person.vx * (2/7)

    for enemy in enemies:
        enemy.movement(scrolling,speed) 
        enemy.draw(screen)
    
    pg.display.update()

pg.quit()