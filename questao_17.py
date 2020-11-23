# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 17                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_17.py                                   *
***************************************************************************/
"""
import pygame
import sys
from pygame.locals import *

from components import Tenis_Court as court
from components import Pong_Player as player
from components import Pong_Ball as ball
from components import Movements as mov


class Questao_17():
    """ This class implements the Pong game """

    def __init__(self):
        """ Constructor """
        pygame.init()
        pygame.display.set_caption('Questão 17')
        self.FONTSIZE = 20
        self.FONT = pygame.font.Font('freesansbold.ttf', self.FONTSIZE)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 200
        self.FPSCLOCK = pygame.time.Clock()
        self.BORDER_SIZE = 5
        self.finish = False
        self.ball_x_dir = -1
        self.ball_y_dir = -1
        self.score_player_one = 0
        self.score_player_two = 0

    def init_game(self):
        """ This function starts the game. """

        player_one_pos = player().player_position()
        player_two_pos = player().player_position()

        player_one = pygame.Rect(70, player_one_pos, 5, 50)
        player_two = pygame.Rect((430), player_two_pos, 5, 50)

        _ball = pygame.Rect(245, 195, 5, 5)

        while True:
            self.SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    player_one.y = mouseY
                    pygame.mouse.set_visible(1)

            # creates the court
            court().create_court(self.SCREEN)

            # creates the players
            player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_one)
            player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_two)

            # creates the ball
            ball().create_ball(self.SCREEN, _ball)

            # inits the ball movements
            _ball = mov().ball_movement(_ball, self.ball_x_dir, self.ball_y_dir, self.score_player_one)

            # verifies the collision existence
            self.ball_x_dir, self.ball_y_dir = mov().verify_collision(_ball,
                                                                      self.ball_x_dir,
                                                                      self.ball_y_dir)

            # verifies the ball collision
            new_dir = mov().ball_collision(_ball, player_one, player_two, self.ball_x_dir)

            # changes the direction accordingly with the direction's state
            if new_dir == 1:
                self.ball_x_dir *= new_dir
            elif new_dir == -1:
                self.ball_x_dir *= new_dir
            else:
                self.ball_x_dir = self.ball_x_dir

            # computer movements
            player_two = mov().computer_movements(_ball, self.ball_x_dir, player_two)
            player_one = mov().computer_movements2(_ball, self.ball_x_dir, player_one)

            # scores points for player one
            self.score_player_one = mov().compute_score(
                player_one, _ball, self.score_player_one, self.ball_x_dir, True)

            # scores points for player two
            self.score_player_two = mov().compute_score(
                player_two, _ball, self.score_player_two, self.ball_x_dir, player_two=True)

            # shows the score for both players
            player().create_score(self.SCREEN, 'You', self.score_player_one, self.FONT, (100, 15))
            player().create_score(self.SCREEN, 'PC', self.score_player_two, self.FONT, (300, 15))

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)


Questao_17().init_game()
