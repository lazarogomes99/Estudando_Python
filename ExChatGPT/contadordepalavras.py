'''
Contador de palavras: 
Crie um programa que conta quantas palavras existem em uma string dada pelo usuário.
'''

mensagem = str(input('Digite uma mensagem: ')).split()
print('A mensagem digitada tem {} palavras.'.format(len(mensagem)))