import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import draw_bg
from character import create_characters

world_length = 5 * 1059  # 5 background images width
person, enemy = create_characters(world_length)
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
    is_scrolling = False
    if keys[pg.K_RIGHT]:
        if person.x > WIDTH - scroll_threshold and scroll < world_length - WIDTH:
            scroll += person.vx
            bg_scroll += person.vx
            person.x = WIDTH - scroll_threshold  # Keep the player at the scroll threshold
            is_scrolling = True
        else:
            person.x += person.vx

    if keys[pg.K_LEFT]:
        if person.x < scroll_threshold and scroll > 0:
            scroll -= person.vx
            bg_scroll -= person.vx
            person.x = scroll_threshold  # Keep the player at the scroll threshold
            is_scrolling = True
        else:
            person.x -= person.vx

    # Ensure the player doesn't move beyond the world boundaries
    if scroll <= 0:
        scroll = 0
        bg_scroll = 0
        person.x = max(person.x, scroll_threshold)
    if scroll >= world_length - WIDTH:
        scroll = world_length - WIDTH
        bg_scroll = world_length - WIDTH
        person.x = min(person.x, WIDTH - scroll_threshold)

    draw_bg(screen, bg_scroll)
    person.movement()
    person.draw(screen)
    enemy.movement(is_scrolling, -scroll if is_scrolling else 0)
    enemy.draw(screen)
    
    pg.display.update()

pg.quit()