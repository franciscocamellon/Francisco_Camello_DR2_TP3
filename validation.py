# -*- coding: utf-8 -*-
""" Validate exceptions """
import re


class Custom_Error(Exception):
    """ Handle custom exceptions. """

    def __init__(self):
        super().__init__()


class Less_Than_Zero(Custom_Error):
    """ Raised when the input value is less than zero. """
    pass


class Zero(Custom_Error):
    """ Raised when the input value is equal zero. """
    pass


class Equal_Length(Custom_Error):
    """ Raised when the input value is not an value. """
    pass


class Months(Custom_Error):
    """ Raised when the input value is greater than 12. """
    pass


class Days(Custom_Error):
    """ Raised when the input value is greater than 30. """
    pass


class String(Custom_Error):
    """ Raised when the error involves strings. """
    pass


class Not_Found(Custom_Error):
    """ Raised when the input value is not found. """
    pass


class Validate(Custom_Error):

    def validate_value_tuple(self, title, _list):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = input(title)
                for i in range(len(_list)):
                    if re.search(value, _list[i], re.IGNORECASE):
                        return value
                else:
                    raise Not_Found
                break
            except ValueError:
                print('{}Erro desconhecido, tente novamente!'.format(' '*3))
            except Not_Found:
                print('{}Erro! O elemento digitado não pertence à tupla!'.format(' '*3))

    def validate_values(self, title, zero=True):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = int(input(title))
                if value < 0:
                    raise Less_Than_Zero
                elif value == 0 and zero == False:
                    raise Zero
                else:
                    return value
                break
            except ValueError:
                print('{}Erro! Digite um número inteiro!'.format(' '*3))
            except Less_Than_Zero:
                print('{}Erro! Digite um número maior que zero!'.format(' '*3))
            except Zero:
                print('{}Erro! Digite um número diferente de zero!'.format(' '*3))

    def validate_strings(self, title, length):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = str(input(title))
                if len(value) < length:
                    raise String
                else:
                    return value
                break
            except ValueError:
                print('{}Erro! Digite uma palavra!'.format(' '*3))
            except String:
                print('{1}Erro! String tem menos de {0} caracteres!'.format(
                    length, ' '*3))

    def validate_numbers(self, title, zero=True):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = input(title)
                if str(value[0]) == '-' and str(value[1:]).isnumeric() \
                        or value.isnumeric():
                    new = int(value)
                    if isinstance(new, int):
                        return new
                    else:
                        raise String
                elif str(value[0]) == '-' and \
                    str(value[1:]).replace('.', '', 1).isdigit() or \
                        value.replace('.', '', 1).isdigit():
                    new = float(value)
                    if isinstance(new, float):
                        return new
                    else:
                        raise String
                elif str(value[0]) == '-' and \
                        str(value[1:]).replace(',', '.', 1).replace('.', '', 1).isdigit()\
                        or value.replace(',', '.', 1).replace('.', '', 1).isdigit():
                    new = float(value.replace(
                        ',', '.', 1))
                    if isinstance(new, float):
                        return new
                    else:
                        raise String
                elif value.isalpha():
                    raise String
                else:
                    raise ValueError

            except ValueError:
                print('{}Erro! Digite um número!'.format(' '*3))
            except String:
                print('{}Erro! Digite um número!'.format(' '*3))
