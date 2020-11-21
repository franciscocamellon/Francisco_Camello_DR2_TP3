# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""
import pygame


class Questao_11():
    """ This function draws a rectangle capable of moving yourself on the
    horizontal axis. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 11')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.x_pos = self.SCREEN_WIDTH // 2
        self.y_pos = self.SCREEN_HEIGHT // 2
        self.finish = False

    def move_keys(self):
        """ This functions moves a rectangle in place"""
        key = pygame.key.get_pressed()

        if self.x_pos > 350:
            self.x_pos = 50
            if key[pygame.K_RIGHT]:
                self.x_pos += 5
        else:
            if key[pygame.K_RIGHT]:
                self.x_pos += 5


    def draw_circle(self, surface, color, position, radius):
        """ This functions draws a circle """
        pygame.draw.circle(surface, color, position, radius)

    def init_game(self):
        """ This function starts the game. """
        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

            self.SCREEN.fill(self.BLACK)

            self.draw_circle(self.SCREEN, self.BLUE,
                             (self.x_pos, self.y_pos), 50)
            self.move_keys()

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_11().init_game()
