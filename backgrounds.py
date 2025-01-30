import pygame as pg
from main import screen


gras = pg.image.image.load("assets/Background/Gras.png").convert_alpha()
ground = pg.image.image.load("assets/Background/Ground.png").convert_alpha()
trees = pg.image.image.load("assets/Background/Trees.png").convert_alpha()
backgroundtrees = pg.image.image.load("assets/Background/BackgroundTrees.png").convert_alpha()
mountain_front = pg.image.image.load("assets/Background/Mountain_Front.png").convert_alpha()
mountain_middle = pg.image.image.load("assets/Background/Mountain_Middle.png").convert_alpha()
mountain_back = pg.image.image.load("assets/Background/Mountain_Back.png").convert_alpha()
clouds = pg.image.image.load("assets/Background/Clouds.png").convert_alpha()
sky = pg.image.image.load("assets/Background/Sky.png").convert_alpha()





def draw_bg():
    # screen.fill(BG)
    screen.blit(sky, (0,0))