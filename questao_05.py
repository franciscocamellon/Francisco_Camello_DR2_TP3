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


class Questao_05():
    """ Docstring """

    def __init__(self):
        """ Constructor. """
        self.students = []
        self.average = 0
        self.out_of_average = []

    def init_class(self):
        """ This function receives the input data from users. """
        finish = False
        while not finish:
            student = input('Digite o nome do aluno: ')
            if student != 'sair':
                height = float(input('Digite a altura do aluno: '))
                self.students.append([student, height])
            else:
                finish = True

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        _sum = 0

        for i in range(len(self.students)):
            _sum += float(self.students[i][1])
        self.average = _sum / len(self.students)

        for i in range(len(self.students)):
            if float(self.students[i][1]) > self.average:
                self.out_of_average.append(self.students[i][0])

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 05'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, 'Média das alturas {} metros'.format(round(self.average, 2)),
              'Alunos acima da média: {0}'.format(self.out_of_average), '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_05().print_result()
