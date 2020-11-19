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
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 10')
        self.KEY = pygame.key.get_pressed()
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
        if self.KEY[pygame.K_LEFT]:
            rect.move_ip(-10, 0)
        if self.KEY[pygame.K_RIGHT]:
            rect.move_ip(10, 0)
        if self.KEY[pygame.K_UP]:
            rect.move_ip(0, -10)
        if self.KEY[pygame.K_DOWN]:
            rect.move_ip(0, 10)

    def draw_rectangle(self, surface, color, rect):
        """ This functions draws a rectangle """
        pygame.draw.rect(surface, color, rect)

    def init_game(self):
        """ Docstring """

        while not self.finish:
            # Checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

            self.SCREEN.fill(self.BLACK)

            self.draw_rectangle(
                self.SCREEN, self.RED, self.RECT)
            self.move_keys(self.RECT)
            # Atualiza o desenho na tela
            pygame.display.update()

            # 60 frames por segundo
            self.FPSCLOCK.tick(self.FPS)
        # Finaliza a janela
        pygame.display.quit()


Questao_10().init_game()
