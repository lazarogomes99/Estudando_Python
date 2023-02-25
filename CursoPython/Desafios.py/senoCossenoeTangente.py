#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite o ângulo que você deseja: '))
#pega o angulo e converte em radiano e depois calcula o SENO desse angulo convertido.
seno = math.sin(math.radians(angulo))
print('O Ângulo {} tem o SENO {:.2f}.'.format(angulo, seno))

#pega o angulo e converte em radiano e depois calcula o COSSENO desse angulo convertido.
cosseno = math.cos(math.radians(angulo))
print('O Ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))

#pega o angulo e converte em radiano e depois calcula a TANGENTE desse angulo convertido.
tangente = math.tan(math.radians(angulo))
print('O Ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
