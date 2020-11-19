# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 09                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_09.py                                   *
***************************************************************************/
"""
from validation import Validate
import pygame


class Questao_09():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 09')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.BLUE = (0, 0, 255)
        self.finish = False


    def draw_circle(self, surface, color, position, radius):
        """ This functions draws a circle """
        pygame.draw.circle(surface, color, position, radius)

    def init_game(self):
        """ Docstring """

        while not self.finish:
            # Checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

            self.draw_circle(
                self.SCREEN, self.BLUE, (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2), 100)

            # Atualiza o desenho na tela
            pygame.display.update()

            # 60 frames por segundo
            self.FPSCLOCK.tick(self.FPS)
        # Finaliza a janela
        pygame.display.quit()


Questao_09().init_game()
