# Faça um programa que leia um número inteiroe mostre seu sucessor e seu antecessor.

numero = int(
    input('Digite um número inteiro e mostrarei o seu sucessor e antecessor: '))

print('O sucessor de {} é {}, e o antecessor é {}'.format(
    numero, numero + 1, numero - 1))
