'''
Faça um programa que peça ao usuário para digitar um número e exiba se ele é positivo ou negativo.
'''

numero = float(input('Digite um número: '))

if numero >= 0:
    print('O numero {}, é um número positivo.'.format(numero))
else:
    print('Esse número {}, é negativo.'.format(numero))
    