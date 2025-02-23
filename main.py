import pygame as pg
from settings import *
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Runner")

from backgrounds import draw_bg_base, draw_fg, draw_fuji, draw_house, rules_img, rules_rect
from character import create_characters


world_length = 5 * WIDTH
person, boss, npc, enemies = create_characters(world_length)
scroll = 0
bg_scroll = 0
scroll_threshold = 200

# health bar
def health_bar(health, x, y,):
    ratio_person = health / 100
    pg.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pg.draw.rect(screen, RED, (x, y, 400, 30))
    pg.draw.rect(screen, YELLOW, (x, y, 400 * ratio_person, 30))

# Reell posisjon i verden
person.world_x = person.x 
npc.world_x = npc.x
boss.world_x = boss.x
boss_activated = False


running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)
    keys = pg.key.get_pressed()
    scrolling = ""

    if not boss_activated and person.rect.colliderect(boss.rect):
        boss_activated = True

    draw_bg_base(screen, scroll)
    draw_fuji(screen, scroll)
    draw_house(screen, scroll, world_length)
    draw_fg(screen, scroll)
    health_bar(person.health, 20, 20)
    health_bar(boss.health, 630, 20)
    
    if abs(person.world_x - npc.world_x) < 100:
        screen.blit(rules_img, rules_rect)


    if keys[pg.K_d]:
        if person.world_x + person.vx <= world_length - person.rect.width:
            person.world_x += person.vx/3
        else:
            person.world_x = world_length - person.rect.width

        if boss.world_x + boss.vx <= world_length - boss.rect.width:
            boss.world_x += boss.vx/3
        else:
            boss.world_x = world_length - boss.rect.width

        if person.world_x - scroll > WIDTH - scroll_threshold and scroll < world_length - WIDTH:
            scroll = person.world_x - (WIDTH - scroll_threshold)
            bg_scroll = scroll
            scrolling = "R"
            scrolling = True

    if keys[pg.K_d] and keys[pg.K_LSHIFT]:
        if person.world_x + person.vx <= world_length - person.rect.width:
            person.world_x += person.vx
        else:
            person.world_x = world_length - person.rect.width

        if boss.world_x + boss.vx <= world_length - boss.rect.width:
            boss.world_x += boss.vx
        else:
            boss.world_x = world_length - boss.rect.width

        if person.world_x - scroll > WIDTH - scroll_threshold and scroll < world_length - WIDTH:
            scroll = person.world_x - (WIDTH - scroll_threshold)
            bg_scroll = scroll
            scrolling = "R"
            scrolling = True

    if keys[pg.K_a]:
        if person.world_x - person.vx >= 0:
            person.world_x -= person.vx/3
        else:
            person.world_x = 0

        if boss.world_x - boss.vx >= 0:
            boss.world_x -= boss.vx/3
        else:
            boss.world_x = 0

        if person.world_x - scroll < scroll_threshold and scroll > 0:
            scroll = person.world_x - scroll_threshold
            bg_scroll = scroll
            scrolling = "L"
            scrolling = True
    
    if keys[pg.K_a] and keys[pg.K_LSHIFT]:
        if person.world_x - person.vx >= 0:
            person.world_x -= person.vx
        else:
            person.world_x = 0

        if boss.world_x - boss.vx >= 0:
            boss.world_x -= boss.vx
        else:
            boss.world_x = 0

        if person.world_x - scroll < scroll_threshold and scroll > 0:
            scroll = person.world_x - scroll_threshold
            bg_scroll = scroll
            scrolling = "L"
            scrolling = True
            
    person.x = person.world_x - scroll

    if boss_activated:
        if boss.world_x < person.world_x:  
            boss.world_x += boss.vx  
        elif boss.world_x > person.world_x:  
            boss.world_x -= boss.vx   
    
    boss.x = boss.world_x - scroll

    #if boss:
    boss_factor = boss.vx / person.vx
    speed = 0
    if scrolling == "R":
        speed = -person.vx * boss_factor
        boss.flip = True
    elif scrolling == "L":
        speed = person.vx * boss_factor
        boss.flip = False


    if not boss.alive:
        boss_activated = False
        boss.x = boss.death_x - scroll
    boss.movement(speed, scrolling, person, None, None, screen)
    boss.update()
    boss.draw(screen)

    for enemy in enemies:
        if not enemy.alive:
            enemy.x = enemy.death_x - scroll
        enemy.movement(speed, scrolling, person, None, None, screen)
        enemy.update()
        enemy.draw(screen)

    person.movement(scroll, scrolling, None, boss, enemies, screen)
    person.update()
    person.draw(screen)
    npc.movement(scroll, scrolling, None, None, None, screen)
    npc.update()  
    npc.x = npc.world_x - scroll
    npc.draw(screen)  
    pg.display.update()

pg.quit()