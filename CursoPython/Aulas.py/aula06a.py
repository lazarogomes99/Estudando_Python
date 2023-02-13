# um programa que leia dois números e mostre cada um dos números antes de somar.


n1 = int(input('Qual o primeiro número?\n '))
n2 = int(input('Qual o segundo número?\n '))

soma = n1 + n2

# print('A soma entre', n1, 'e', n2, 'vale ', soma)
# veja um jeito mais simplificado de fazer essa impressão usando o método .format

print('A soma entre {} e {}, vale {}.'.format(n1, n2, soma))
