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

gras = pg.transform.scale(gras, (1024, 704))
ground = pg.transform.scale(ground, (1024, 704))
trees = pg.transform.scale(trees, (1024, 704))
backgroundtrees = pg.transform.scale(backgroundtrees, (1024, 704))
mountain_front = pg.transform.scale(mountain_front, (1024, 704))
mountain_middle = pg.transform.scale(mountain_middle, (1024, 704))
mountain_back = pg.transform.scale(mountain_back, (1024, 704))
clouds = pg.transform.scale(clouds, (1024, 704))
sky = pg.transform.scale(sky, (1024, 704))



def draw_bg(screen):
    # screen.fill(BG)
    screen.blit(sky, (0,0))
    screen.blit(clouds, (0, HEIGHT - clouds.get_height() - 300))
    screen.blit(mountain_back, (0, HEIGHT - mountain_back.get_height() - 300))
    screen.blit(mountain_middle, (0, HEIGHT - mountain_middle.get_height() - 300))


