# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 15                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_15.py                                   *
***************************************************************************/
"""
import pygame
import math


class Questao_15():
    """ This function draws a five point star. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 15')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.position = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        self.finish = False

    def draw_star(self, surface, color, x, y, radius):
        """ This functions draws a square """

        pts = []
        for i in range(90, 450, 72):
            x = x + radius * math.cos(54.05 + math.pi * 2 * i / 5)
            y = y + radius * math.sin(54.05 + math.pi * 2 * i / 5)
            pts.append([x, y])
        pygame.draw.polygon(surface, color, pts)

    def init_game(self):
        """ This function starts the game. """
        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

            self.SCREEN.fill(self.BLACK)

            self.draw_star(self.SCREEN, self.RED,
                           self.position[0] + math.cos(19)*30,
                           self.position[1], 100)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_15().init_game()
