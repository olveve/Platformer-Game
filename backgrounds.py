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



def draw_bg(screen):
    # screen.fill(BG)
    screen.blit(sky, (0,0))
    screen.blit(clouds, (0, HEIGHT - clouds.get_height() - 150))
    screen.blit(mountain_back, (0, HEIGHT - mountain_back.get_height()))
    screen.blit(mountain_middle, (0, HEIGHT - mountain_middle.get_height()))
    screen.blit(mountain_front, (0, HEIGHT - mountain_front.get_height()))
    screen.blit(backgroundtrees, (0, HEIGHT - backgroundtrees.get_height()))
    screen.blit(trees, (0, HEIGHT - trees.get_height()))
    screen.blit(ground, (0, HEIGHT - ground.get_height()))
    screen.blit(gras, (0, HEIGHT - gras.get_height()))


