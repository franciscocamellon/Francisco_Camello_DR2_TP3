# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 12                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_12.py                                   *
***************************************************************************/
"""
import pygame


class Questao_12():
    """ This function draws a circle capable of moving yourself on the
    vertical and horizontal axis. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 12')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.YELLOW = (255, 255, 0)
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
        elif self.x_pos < 50:
            self.x_pos = 350
            if key[pygame.K_LEFT]:
                self.x_pos -= 5
        elif self.y_pos > 350:
            self.y_pos = 50
            if key[pygame.K_UP]:
                self.x_pos += 5
        elif self.y_pos < 50:
            self.y_pos = 350
            if key[pygame.K_DOWN]:
                self.x_pos -= 5
        else:
            if key[pygame.K_LEFT]:
                self.x_pos -= 5
            if key[pygame.K_RIGHT]:
                self.x_pos += 5
            if key[pygame.K_UP]:
                self.y_pos -= 5
            if key[pygame.K_DOWN]:
                self.y_pos += 5

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

            self.draw_circle(self.SCREEN, self.YELLOW,
                             (self.x_pos, self.y_pos), 50)
            self.move_keys()

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_12().init_game()
