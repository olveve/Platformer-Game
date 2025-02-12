import pygame as pg
from settings import *
from main import world_length


gras = pg.image.load("assets/Background/Gras.png").convert_alpha()
ground = pg.image.load("assets/Background/Ground.png").convert_alpha()
trees = pg.image.load("assets/Background/Trees.png").convert_alpha()
backgroundtrees = pg.image.load("assets/Background/BackgroundTrees.png").convert_alpha()
mountain_front = pg.image.load("assets/Background/Mountain_Front.png").convert_alpha()
mountain_middle = pg.image.load("assets/Background/Mountain_Middle.png").convert_alpha()
mountain_back = pg.image.load("assets/Background/Mountain_Back.png").convert_alpha()
clouds = pg.image.load("assets/Background/Clouds.png").convert_alpha()
sky = pg.image.load("assets/Background/Sky.png").convert_alpha()

house = pg.image.load("assets/Background/House.png").convert_alpha()
fuji = pg.image.load("assets/Background/Fuji.png").convert_alpha()


gras = pg.transform.scale(gras, (1059, 504))
ground = pg.transform.scale(ground, (1059, 504))
trees = pg.transform.scale(trees, (1059, 504))
backgroundtrees = pg.transform.scale(backgroundtrees, (1059, 504))
mountain_front = pg.transform.scale(mountain_front, (1059, 504))
mountain_middle = pg.transform.scale(mountain_middle, (1059, 504))
mountain_back = pg.transform.scale(mountain_back, (1059, 504))
clouds = pg.transform.scale(clouds, (1059, 504))
sky = pg.transform.scale(sky, (1059, 504))

house = pg.transform.scale(house, (1059, 504))
fuji = pg.transform.scale(fuji, (1059, 504))



def draw_bg(screen, scroll):
    width = sky.get_width()
    
    # Tegn de øvre lagene (parallax-bevegelse)
    for x in range(5):
        screen.blit(sky, ((x * width) - scroll * 0.1, 0))
        screen.blit(clouds, ((x * width) - scroll * 0.2, HEIGHT - clouds.get_height() - 150))
        screen.blit(mountain_back, ((x * width) - scroll * 0.3, HEIGHT - mountain_back.get_height()))
        screen.blit(mountain_middle, ((x * width) - scroll * 0.4, HEIGHT - mountain_middle.get_height()))
        screen.blit(mountain_front, ((x * width) - scroll * 0.5, HEIGHT - mountain_front.get_height()))
    
    draw_fuji(screen, bg_scroll, world_length)  # Bruk scroll, ikke world_x!

    # Nedre lag med parallax-effekt (disse lagene kommer foran Fuji)
    for x in range(5):
        screen.blit(backgroundtrees, ((x * width) - scroll * 0.6, HEIGHT - backgroundtrees.get_height()))
        screen.blit(trees, ((x * width) - scroll * 0.7, HEIGHT - trees.get_height()))
        screen.blit(ground, ((x * width) - scroll * 0.8, HEIGHT - ground.get_height()))
        screen.blit(gras, ((x * width) - scroll * 0.9, HEIGHT - gras.get_height()))

def draw_fuji(screen, scroll, world_length):
    start_x = 50  # Fuji i starten av verden
    end_x = world_length - WIDTH + 50  # Fuji i slutten av verden

    if scroll < WIDTH:  # Startområdet
        screen.blit(fuji, (start_x - scroll, HEIGHT - fuji.get_height() - 50))
    elif scroll > world_length - WIDTH - WIDTH:  # Sluttområdet
        screen.blit(fuji, (end_x - scroll, HEIGHT - fuji.get_height() - 50))
"""
def draw_fuji(screen, scroll, world_length):
    if scroll < WIDTH:  # Startområdet
        screen.blit(fuji, (50, HEIGHT - fuji.get_height() - 50))
    elif scroll > world_length - WIDTH * 2:  # Sluttområdet
        screen.blit(fuji, (world_length - WIDTH + 50 - scroll, HEIGHT - fuji.get_height() - 50))
"""