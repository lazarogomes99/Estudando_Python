'''
Faça um programa que peça ao usuário para digitar a idade e exiba se ela é maior ou menor de 18 anos.
'''

idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('Sua idade é {}, parabéns você já pode tirar sua CNH.'.format(idade))
else:
    print('Infelizmente você tem {} anos de idade, não será possível tirar sua CNH nesse momento, aguarde até ter 18 anos.'.format(idade))
