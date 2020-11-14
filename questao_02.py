# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 02                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_02.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_02():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.title = 'Digite um número inteiro: '
        self.list = []

    def init_class(self):
        """ This function receives the input data from users. """
        while len(self.list) <= 5:
            _input = Validate().validate_values(self.title, zero=True)
            self.list.append(_input)

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 02'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, '{}'.format(self.list),
              '---' * 25,
              'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_02().print_result()
