# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_01():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.my_list = []


    def init_class(self):
        """ This function receives the input data from users. """



    def process_data(self):
        """ This function process the input data from init_class. """

        for i in range(1, 6):
            self.my_list.append(i)

        print(self.my_list)

        for i in self.my_list:
            Validate.validate_value_tuple()





    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 09'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' *25, '{}','---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_01().print_result()
