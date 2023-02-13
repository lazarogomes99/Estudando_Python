#Faça um programa que leia um número e mostre em tela o dobro, o triplo e a raiz quadrada. 


numero = float(input('Digite um número: '))

print('O dobro deste número é {}, e o triplo é {}.'.format(numero *2, numero *3))
print('A raiz quadrada é {:.2f}'.format(numero**(1/2)))