# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 05                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_05.py                                   *
***************************************************************************/
"""

from validation import Validate


class Questao_05():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.input = {"Digite o nome do aluno: ":[],
        "Digite a altura do aluno: ":[]}


    def init_class(self):
        """ This function receives the input data from users. """
        while "sair" not in self.input["Digite o nome do aluno: "]:
            for k, v in self.input.items():
                self.input["Digite o nome do aluno: "].append(input(k))
                self.input["Digite a altura do aluno: "].append(input(k))



    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()



    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 05'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' *25, '{}'.format(self.input),'---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_05().print_result()
