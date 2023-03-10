# Faça um programa que leia um número inteiro e mostre sua tabuada.

numero = int(input('Digite um número inteiro: '))
print('A tabuada de {} segue mais abaixo.\n'.format(numero))

for i in range(1, 10, 1):
    print('{} x {}'.format(numero, i), numero * i)