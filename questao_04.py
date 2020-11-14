# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 04                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_04.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_04():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.title1 = 'Digite o tamanho da lista: '
        self.title2 = 'Digite um número: '
        self.list = []
        self.length = 0

    def init_class(self):
        """ This function receives the input data from users. """
        self.length = Validate().validate_values(self.title1, zero=False)
        while len(self.list) < self.length:
            self.list.append(Validate().validate_numbers(self.title2))

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        l = [value for value in self.list if value == 0]
        self.list.clear()
        self.list = l

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 04'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25)
        if len(self.list) > 0:
            print('Existem {} números iguais a zero nesta lista'.format(len(self.list)),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")
        else:
            print('Não existem números iguais a zero nesta lista',
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_04().print_result()
