# -*- coding: utf-8 -*-
import pygame
import pygame.gfxdraw
from pygame.locals import *
import math
from sys import exit


class MW():
    def __init__(self, config):
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        if 'caption' in self.config:
            pygame.display.set_caption(self.config['caption'])
        else:
            pygame.display.set_caption("Math!")
        self.font = pygame.font.SysFont("timesnewroman", 16)
        self.math_font = pygame.font.SysFont("timesnewroman", 16, False, True)
        self.event_list = []
        self.clock = pygame.time.Clock()
        self.sin_param = {}
        self.sin_param['A'] = 1
        self.sin_param['w'] = 1
        self.sin_param['ψ'] = 0
        self.sin_param['b'] = 0
        self.b = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 3:
                        pass
                    if event.button == 1:
                        for el in self.event_list:
                            if el[0].collidepoint(event.pos):
                                el[1](event)
            self.update()
            pygame.display.update()

    def __register_callback(self, hotspot, callback=None, name=''):
        self.event_list.append((hotspot, callback, name))

    def __draw_valueBar(self, x, y, params, key, width=80, height=20, scale=1.0, label=None, callback=None, name=''):
        hotspot = Rect(x, y, width, height)
        pygame.draw.line(self.screen, (0, 0, 0), (x, y + height / 2), (x + width, y + height / 2))
        if key == 'ψ':
            current_x = (params[key] / math.pi + scale) / 2 / scale * width + x
        else:
            current_x = (params[key] + scale) / 2 / scale * width + x
        pygame.draw.line(self.screen, (0, 0, 0), (current_x, y + height / 4), (current_x, y + height / 4 * 3))

        def click_valueBar(event):
            value = round((event.pos[0] - x) / width * scale * 2 - scale, 1)
            if key == 'ψ':
                params[key] = value * math.pi
                pygame.draw.line(self.screen, (0, 0, 0), (event.pos[0], y + height / 4), (event.pos[0], y + height / 4 * 3))
            else:
                params[key] = value
                pygame.draw.line(self.screen, (0, 0, 0), (event.pos[0], y + height / 4), (event.pos[0], y + height / 4 * 3))

        self.__register_callback(hotspot, click_valueBar, name)

    def __get_sin_str(self):
        fun_str = ''
        if -1e-4 < self.sin_param['A'] - 1 < 1e-4:
            fun_str = fun_str + 'sin'
        elif -1e-4 < self.sin_param['A'] + 1 < 1e-4:
            fun_str = fun_str + '-sin'
        elif -1e-4 < self.sin_param['A'] - round(self.sin_param['A']) < 1e-4:
            fun_str = fun_str + '%dsin' % int(self.sin_param['A'])
        else:
            fun_str = fun_str + '%.1fsin' % self.sin_param['A']
        if self.sin_param['ψ'] > 1e-4 or self.sin_param['ψ'] < -1e-4:
            fun_str = fun_str + '('
        if self.sin_param['w'] - 1 < 1e-4 and self.sin_param['w'] - 1 > -1e-4:
            fun_str = fun_str + 'x'
        else:
            fun_str = fun_str + '%.1fx' % self.sin_param['w']
        coinf = self.sin_param['ψ'] / math.pi
        if -1e-4 < coinf - round(coinf) < 1e-4:
            if -1e-4 < coinf - 1 < 1e-4:
                fun_str = fun_str + '+π)'
            elif -1e-4 < coinf + 1 < 1e-4:
                fun_str = fun_str + '-π)'
            elif -1e-4 < coinf < 1e-4:
                fun_str = fun_str
            else:
                fun_str = fun_str + '+%dπ)' % coinf
        else:
            if coinf > 1e-4:
                fun_str = fun_str + '+%.1fπ)' % coinf
            if coinf < -1e-4:
                fun_str = fun_str + '-%.1fπ)' % -coinf
        if self.sin_param['b'] > 1e-4:
            if -1e-4 < self.sin_param['b'] - round(self.sin_param['b']) < 1e-4:
                fun_str = fun_str + '+%.1d' % int(self.sin_param['b'])
            else:
                fun_str = fun_str + '+%.1f' % self.sin_param['b']
        if self.sin_param['b'] < -1e-4:
            if -1e-4 < self.sin_param['b'] - round(self.sin_param['b']) < 1e-4:
                fun_str = fun_str + '-%.1d' % int(-self.sin_param['b'])
            else:
                fun_str = fun_str + '-%.1f' % -self.sin_param['b']
        return fun_str

    def update(self):
        self.draw_bg()
        if 'test' in self.config:
            if self.config['test']:
                self.test()
        if 'scene' in self.config:
            if self.config['scene'] == 'standard_sin':
                self.draw_standard_sin()
            elif self.config['scene'] == 'dynamic_sin':
                self.draw_dynamic_sin()
            else:
                self.draw_axis()

    def draw_bg(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 800, 600))

    def draw_axis(self):
        if 'axis_type' in self.config:
            if self.config['axis_type'] == 'normal':
                self.draw_normal_axis()
            elif self.config['axis_type'] == 'tri':
                self.draw_tri_axis()
            else:
                self.draw_normal_axis()
        else:
            self.draw_normal_axis()

    def draw_normal_axis(self):
        pygame.draw.line(self.screen, (0, 0, 0), (10, 300), (790, 300))
        pygame.gfxdraw.line(self.screen, 790, 300, 785, 295, (0, 0, 0))
        pygame.gfxdraw.line(self.screen, 790, 300, 785, 305, (0, 0, 0))
        pygame.draw.line(self.screen, (0, 0, 0), (400, 590), (400, 10))
        pygame.gfxdraw.line(self.screen, 400, 10, 395, 15, (0, 0, 0))
        pygame.gfxdraw.line(self.screen, 400, 10, 405, 15, (0, 0, 0))
        self.screen.blit(self.font.render('0', True, (0, 0, 0)), (405, 305))
        for i in [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]:
            pygame.draw.line(self.screen, (240, 20, 0), (400 + i * 50, 300), (400 + i * 50, 295))
            self.screen.blit(self.font.render('%d' % i, True, (0, 0, 0)), (396 + i * 50, 305))
        for j in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
            pygame.draw.line(self.screen, (240, 20, 0), (400, 300 - j * 50), (405, 300 - j * 50))
            self.screen.blit(self.font.render('%d' % j, True, (0, 0, 0)), (410, 294 - j * 50))
        pass

    def draw_tri_axis(self):
        pygame.draw.line(self.screen, (0, 0, 0), (10, 300), (790, 300))
        pygame.gfxdraw.line(self.screen, 790, 300, 785, 295, (0, 0, 0))
        pygame.gfxdraw.line(self.screen, 790, 300, 785, 305, (0, 0, 0))
        pygame.draw.line(self.screen, (0, 0, 0), (400, 590), (400, 10))
        pygame.gfxdraw.line(self.screen, 400, 10, 395, 15, (0, 0, 0))
        pygame.gfxdraw.line(self.screen, 400, 10, 405, 15, (0, 0, 0))
        self.screen.blit(self.font.render('0', True, (0, 0, 0)), (405, 305))
        x_label = ['-7/2π', '-3π', '-5/2π', '-2π', '-3/2π', '-π', '-1/2π', '1/2π', 'π', '3/2π', '2π', '5/2π', '3π', '7/2π']
        for i in [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]:
            pygame.draw.line(self.screen, (240, 20, 0), (400 + i * 50, 300), (400 + i * 50, 295))
            self.screen.blit(self.font.render('%s' % x_label[i + 7 - (i > 0)], True, (0, 0, 0)), (390 + i * 50, 305))
        for j in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
            pygame.draw.line(self.screen, (240, 20, 0), (400, 300 - j * 50), (405, 300 - j * 50))
            self.screen.blit(self.font.render('%.1f' % (j / 2), True, (0, 0, 0)), (410, 294 - j * 50))

    def draw_standard_sin(self):
        self.draw_tri_axis()
        coords = []
        for i in range(0, 800, 1):
            x = (i - 400) / 100 * math.pi
            y = math.sin(x)
            j = 300 - y * 100
            coords.append((i, j))
        for index, coord in enumerate(coords):
            if index == 0:
                continue
            pygame.draw.aaline(self.screen, (0, 0, 0), coords[index - 1], coords[index])

    def draw_dynamic_sin(self):
        self.draw_tri_axis()
        self.draw_sin_param_clip()
        self.screen.set_clip()
        coords = []
        for i in range(0, 800, 1):
            x = (i - 400) / 100 * math.pi
            y = self.sin_param['A'] * math.sin(self.sin_param['w'] * x + self.sin_param['ψ']) + self.sin_param['b']
            j = 300 - y * 100
            coords.append((i, j))
        for index, coord in enumerate(coords):
            if index == 0:
                continue
            pygame.draw.aaline(self.screen, (0, 0, 0), coords[index - 1], coords[index])
        pass

    def draw_sin_param_clip(self):
        self.screen.set_clip(0, 0, 200, 200)
        self.screen.blit(self.math_font.render('A:', True, (0, 0, 0)), (10, 20))
        self.screen.blit(self.math_font.render('w:', True, (0, 0, 0)), (10, 50))
        self.screen.blit(self.math_font.render('ψ:', True, (0, 0, 0)), (10, 80))
        self.screen.blit(self.math_font.render('b:', True, (0, 0, 0)), (10, 110))
        self.__draw_valueBar(30, 20, self.sin_param, 'A', height=20, name='A')
        self.__draw_valueBar(30, 50, self.sin_param, 'w', height=20, name='w', scale=2.0)
        self.__draw_valueBar(30, 80, self.sin_param, 'ψ', height=20, name='ψ')
        self.__draw_valueBar(30, 110, self.sin_param, 'b', height=20, name='b')
        fun_str = self.__get_sin_str()
        self.screen.blit(self.math_font.render(fun_str, True, (0, 0, 0)), (30, 140))

    def test(self):
        self.draw_normal_axis()
        self.screen.blit(self.math_font.render('f(x)= x^2 - %fx + 2' % self.b, True, (0, 0, 0)), (50, 50))
        coords = []
        for i in range(0, 800, 1):
            x = (i - 400) / 50
            y = x * x - self.b * x + 2
            j = 300 - y * 50
            coords.append((int(i), int(j)))
        for index, coord in enumerate(coords):
            if index == 0:
                continue
            pygame.draw.aaline(self.screen, (0, 0, 0), coords[index - 1], coords[index])
        pygame.gfxdraw.aacircle(self.screen, 400, 200, 5, (255, 0, 0))
        self.b = self.b + (self.clock.tick()) / 1000 * 0.3


if __name__ == '__main__':
    config = {}
    config['axis_type'] = 'tri'
    config['scene'] = 'dynamic_sin'
    # config['test'] = True
    m = MW(config)
