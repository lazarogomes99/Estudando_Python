# Faça um programa que leia um número real e tire a parte inteira do número.
# ex: 6.123 a parte inteira é 6.

# importei apenas o floor da biblioteca math.
from math import floor

# solicitei que o usuario digitasse um numero real.
num = float(input('Digite um número flutuante: '))

# usei o floor para arredondar o numero digitado para baixo.
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, floor(num)))
