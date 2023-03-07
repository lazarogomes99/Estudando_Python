'''
Jogo da adivinhação: Crie um jogo onde o programa escolhe um número aleatório e o usuário tem que adivinhar qual é.
O programa deve dar dicas se o número é maior ou menor do que o escolhido.
'''

import random

numero_alet = random.randint(0 , 1000)

tentativas = 0

while True:
    numero_esco = int(input('Digite um número entre 0 e 1000: '))
    tentativas += 1

    if numero_esco == numero_alet:
        print('Parabéns, você acertou em {} tentativas'.format(tentativas))
        break
    elif numero_esco < numero_alet:
        print('O número secreto é maior do que {}'.format(numero_esco))
    else:
        print('O número secreto é menor do que {}'.format(numero_esco))
    