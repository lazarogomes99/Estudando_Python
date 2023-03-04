# Faça um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual o seu nome? ')).strip() # strip para retirar os espaços do começo e final.
divisão = nome.upper().split() #upper para deixar tudo em maiusculo, e o split para fazer a divisão de cada palavra.

print('SILVA' in divisão) #verifica se existe "SILVA" na divão onde foi armazenada o conteudo de nome divido em strings.