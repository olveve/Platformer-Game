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

gras = pg.transform.scale(gras, (1059, 504))
ground = pg.transform.scale(ground, (1059, 504))
trees = pg.transform.scale(trees, (1059, 504))
backgroundtrees = pg.transform.scale(backgroundtrees, (1059, 504))
mountain_front = pg.transform.scale(mountain_front, (1059, 504))
mountain_middle = pg.transform.scale(mountain_middle, (1059, 504))
mountain_back = pg.transform.scale(mountain_back, (1059, 504))
clouds = pg.transform.scale(clouds, (1059, 504))
sky = pg.transform.scale(sky, (1059, 504))



def draw_bg(screen, scroll):
    # screen.fill(BG)
    screen.blit(sky, (0,0))
    screen.blit(clouds, (scroll * 0.1, HEIGHT - clouds.get_height() - 150))
    screen.blit(mountain_back, (scroll * 0.2, HEIGHT - mountain_back.get_height()))
    screen.blit(mountain_middle, (scroll * 0.4, HEIGHT - mountain_middle.get_height()))
    screen.blit(mountain_front, (scroll * 0.6, HEIGHT - mountain_front.get_height()))
    screen.blit(backgroundtrees, (scroll * 0.8, HEIGHT - backgroundtrees.get_height()))
    screen.blit(trees, (scroll * 0.9, HEIGHT - trees.get_height()))
    screen.blit(ground, (scroll, HEIGHT - ground.get_height()))
    screen.blit(gras, (scroll * 1.1, HEIGHT - gras.get_height()))


