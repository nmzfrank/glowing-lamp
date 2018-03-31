import pygame
from pygame.locals import *
import pygame.gfxdraw
import math


class PW(object):
    def __init__(self, config):
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        if 'caption' in self.config:
            pygame.display.set_caption(self.config['caption'])
        else:
            pygame.display.set_caption("Physics!")
        self.font = pygame.font.SysFont("timesnewroman", 16)
        self.math_font = pygame.font.SysFont("timesnewroman", 16, False, True)
