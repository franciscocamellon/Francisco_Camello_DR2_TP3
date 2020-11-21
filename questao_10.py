# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 10                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_10.py                                   *
***************************************************************************/
"""
import pygame


class Questao_10():
    """ This function draws a rectangle capable of moving yourself on the
    vertical and horizontal axis. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 10')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.RECT = pygame.Rect(
            (self.SCREEN_WIDTH * 3/8, self.SCREEN_HEIGHT * 3/8), (100, 100))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.finish = False

    def move_keys(self, rect):
        """ This functions moves a rectangle in place"""

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            rect.move_ip(-10, 0)
        if key[pygame.K_RIGHT]:
            rect.move_ip(10, 0)
        if key[pygame.K_UP]:
            rect.move_ip(0, -10)
        if key[pygame.K_DOWN]:
            rect.move_ip(0, 10)

    def draw_rectangle(self, surface, color, rect):
        """ This functions draws a rectangle """

        pygame.draw.rect(surface, color, rect)

    def init_game(self):
        """ This function starts the game. """

        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

            self.SCREEN.fill(self.BLACK)

            self.draw_rectangle(self.SCREEN, self.RED, self.RECT)
            self.move_keys(self.RECT)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_10().init_game()
