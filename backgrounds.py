import pygame as pg
from settings import *


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
double_house = pg.image.load("assets/Background/Shrine_Multiple.png").convert_alpha()


gras = pg.transform.scale(gras, (1059, 504))
ground = pg.transform.scale(ground, (1059, 504))
trees = pg.transform.scale(trees, (1059, 504))
backgroundtrees = pg.transform.scale(backgroundtrees, (1059, 504))
mountain_front = pg.transform.scale(mountain_front, (1059, 504))
mountain_middle = pg.transform.scale(mountain_middle, (1059, 504))
mountain_back = pg.transform.scale(mountain_back, (1059, 504))
clouds = pg.transform.scale(clouds, (1059, 504))
sky = pg.transform.scale(sky, (1059, 504))

house = pg.transform.scale(house, (1255, 604))
fuji = pg.transform.scale(fuji, (1059, 700))
double_house = pg.transform.scale(double_house, (1255, 604))

# laste spritesheet
samurai_sheet = pg.image.load("assets/mainCharacter/Samurai.png").convert_alpha()
# npc_sheet = pg.image.load("assets/npc/NPC_Ronin.png").convert_alpha()


def draw_bg_base(screen, scroll):
    width = sky.get_width()
    for x in range(5):
        screen.blit(sky, ((x * width) - scroll * 0.1, 0))
        screen.blit(clouds, ((x * width) - scroll * 0.2, HEIGHT - clouds.get_height() - 150))
        screen.blit(mountain_back, ((x * width) - scroll * 0.3, HEIGHT - mountain_back.get_height()))
        screen.blit(mountain_middle, ((x * width) - scroll * 0.4, HEIGHT - mountain_middle.get_height()))
        screen.blit(mountain_front, ((x * width) - scroll * 0.5, HEIGHT - mountain_front.get_height()))

def draw_fg(screen, scroll):
    width = gras.get_width()
    for x in range(5):
        screen.blit(backgroundtrees, ((x * width) - scroll * 0.6, HEIGHT - backgroundtrees.get_height()))
        screen.blit(trees, ((x * width) - scroll * 0.7, HEIGHT - trees.get_height()))
        screen.blit(ground, ((x * width) - scroll * 0.8, HEIGHT - ground.get_height()))
        screen.blit(gras, ((x * width) - scroll * 0.9, HEIGHT - gras.get_height()))
        
def draw_fuji(screen, scroll):
    start_x = -350  
    fuji_y = HEIGHT - fuji.get_height() + 25  

    fuji_scroll_factor = 0.62
    adjusted_scroll = scroll * fuji_scroll_factor

    if scroll < WIDTH:  
        screen.blit(fuji, (start_x - adjusted_scroll, fuji_y))

def draw_house(screen, scroll, world_length):
    house_x = world_length - WIDTH - 1720 
    house_y = HEIGHT - house.get_height()  

    house_scroll_factor = 0.62  
    adjusted_scroll = scroll * house_scroll_factor

    if scroll > world_length - WIDTH - WIDTH:
        screen.blit(double_house, (house_x - adjusted_scroll + 400, house_y ))  
        screen.blit(house, (house_x - adjusted_scroll, house_y))
