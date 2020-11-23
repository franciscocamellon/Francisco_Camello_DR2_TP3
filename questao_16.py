# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 16                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_16.py                                   *
***************************************************************************/
"""
import pygame, math, random


class Questao_16():
    """ This function draws a five point star. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 16')
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

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.position = pygame.mouse.get_pos()
                    self.draw_star(self.SCREEN, self.RED,
                                   self.position[0],
                                   self.position[1], random.randint(1,10)*10)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_16().init_game()
