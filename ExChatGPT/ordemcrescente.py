# Faça um programa que leia 10 digitos e imprima em ordem crescente. 
#comentarei todo o codigo detalhadamente para facilitar minha própria leitura em futuros resumos de estudo.

contador = 0 #usei para ser o contador para ficar pedindo numero ao usuario.
numeros = [] #array para ser armazenado os numeros digitados.
while contador <= 9: #estrutura de repetição que enquanto o contador não for maior ou igual a 9, ele continuara rodando.
    num = float(input('Digite um número: '))
    numeros.append(num) #i método .append serve para armazenar o "num" ao final do array. cada numero digitado pelo user, vai pro final do array.
    contador = contador + 1 # quando chega aqui, é acrescentado + 1 ao contador.
    numeros.sort() # o método .sort ser para por a lista numeros em ordem crescente.

print('Os números digitados em ordem crescente aparecerá na tela logo abaixo:')

for i in range(len(numeros)): #variavel 'i' recebe o índice de cada elemento da lista.
    print(numeros[i]) #vai imprimindo o conteu da lista, o 'i' que é o indice vai de 0 a 9.