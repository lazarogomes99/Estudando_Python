# Faça um programa que leia algo e imprima na tela o seu tipo primitivo e todas as informações sobre ela.
# Fazendo teste de tipo.

algo = input('Digite algo:\n')

print(type(algo))

print('O que digitou é um número?')
print(algo.isnumeric())

print('O que digitou está escrita com CAPSLOOK?')
print(algo.isupper())

print('O que digitou é Alfanúmerico?')
print(algo.isalnum())

print('O que digitou é Alfabetico?')
print(algo.isalpha())

print('Só tem espaços?')
print(algo.isspace())
