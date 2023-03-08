'''
Calculadora: Crie um programa que recebe dois números do usuário e realiza as operações 
matemáticas básicas (adição, subtração, multiplicação e divisão).
'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

print('Valores digitados foram 1º:{}, 2º:{}'.format(numero1, numero2))

print('Adição: {:.2f}'.format(numero1+numero2))
print('Subtração: {:.2f}'.format(numero1-numero2))
print('Multiplicação: {:.2f}'.format(numero1*numero2))
print('Divisão: {:.2f}'.format(numero1/numero2))