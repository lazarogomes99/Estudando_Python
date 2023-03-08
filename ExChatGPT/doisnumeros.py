'''
Faça um programa que peça ao usuário para digitar dois números e exiba o maior deles.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número: {}, é maior que o segundo número digitado: {}.'.format(num1, num2))
elif num1 == num2:
    print('Os números são identicos!')
else:
    print('o segundo número: {}, é maior que o primeiro número digitado: {}.'.format(num2, num1))
