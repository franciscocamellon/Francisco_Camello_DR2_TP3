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


class Questao_01():
    """ This class handles lists """

    def __init__(self):
        """ Constructor. """
        self.my_list = []

    def init_class(self):
        """ This function receives the input data from users. """

    def process_data(self):
        """ This function process the input data from init_class. """

        for i in range(1, 6):
            self.my_list.append(i)

        print('Lista: ', self.my_list)

        remove = [3, 6]
        if remove[0] in self.my_list:
            self.my_list.remove(remove[0])
        else:
            print('O número {} não pertence à lista!'.format(remove[0]))
        if remove[1] in self.my_list:
            self.my_list.remove(remove[1])
        else:
            print('O número {} não pertence à lista!'.format(remove[1]))

        print('Lista modificada: ', self.my_list)

        print('O tamanho da lista é de {} elementos'.format(len(self.my_list)))

        self.my_list[-1] = 6
        print('Lista modificada novamente: ', self.my_list)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 01'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_01().print_result()
