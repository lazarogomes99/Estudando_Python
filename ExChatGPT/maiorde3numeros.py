#Faça um programa que leia três números e exiba o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número digitado foi: {}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número digitado foi: {}.'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior número digitado fo: {}.'.format(n3))