#sortear a ordem de apresentação de 4 alunos, e mostrar em ordem sorteada.

from random import shuffle
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)# o método SHUFFLE irá embaralhar conteudo do array lista.

print(lista)