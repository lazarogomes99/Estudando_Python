'''
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. 
'''
'''
num = int(input('Digite um número entre 0 e 9999:'))
n = str(num)

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

'''

#outra maneira de fazer.

num = int(input('Digite um número entre 0 e 9999:'))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))