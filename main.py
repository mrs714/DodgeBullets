import pygame
from consts import *
from entity import Entity
from player import Player
from bullet import Bullet
from logic import tryMove


pygame.init()

win = pygame.display.set_mode((map_size, map_size))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()
