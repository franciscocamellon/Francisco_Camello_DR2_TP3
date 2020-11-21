# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 14                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_14.py                                   *
***************************************************************************/
"""

import pygame

class Questao_14():
    """ This function draws a rectangle where the user clicks. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 14')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.position = (self.SCREEN_WIDTH * 3/8, self.SCREEN_HEIGHT * 3/8)
        self.finish = False

    def draw_square(self, surface, color, position):
        """ This functions draws a square """
        rect = pygame.Rect(position, (50, 50))
        pygame.draw.rect(surface, color, rect)

    def init_game(self):
        """ This function starts the game. """
        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.position = pygame.mouse.get_pos()

            self.SCREEN.fill(self.BLACK)

            self.draw_square(self.SCREEN, self.RED, self.position)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_14().init_game()
