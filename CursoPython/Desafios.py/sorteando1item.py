#faça um programa que leia uma lista de nomes e sorteie um nome da lista aleatóriamente. 
#soteie o nome e escreve o nome sorteado. 

from random import choice #entrando no modulo random e importando apenas o choice.
# método choice permite escolher aleatoriamente um elemento de um array etc....


n1 = input('Digite o primeiro nome para sorteio: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]

#variavel escolhido recebe um item aleatório que está no array lista. 
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))


