# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_03():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.title = 'Digite uma palavra: '
        self.list = []

    def init_class(self):
        """ This function receives the input data from users. """
        while len(self.list) < 2:
            self.list.append(Validate().validate_strings(self.title, 2))

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        l = []
        for word in self.list:
            word[::-1]
            l.append(word[::-1])
        self.list.clear()
        self.list = l

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, '{}'.format([word for word in self.list]),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_03().print_result()
