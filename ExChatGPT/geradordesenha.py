'''
Gerador de senhas:
 Crie um programa que gera senhas aleatórias para o usuário, com um número definido de caracteres e
 possibilidade de escolher se quer letras maiúsculas, minúsculas, números e símbolos.
'''

import random
import string

# Define os caracteres disponíveis para gerar senhas
letras_min = string.ascii_lowercase
letras_mai = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

# Pergunta ao usuário a quantidade de caracteres da senha e quais tipos de caracteres usar
comprimento = int(input("Quantos caracteres deve ter a senha? "))
usar_min = input("Usar letras minúsculas? (S/N)").lower() == "s"
usar_mai = input("Usar letras maiúsculas? (S/N)").lower() == "s"
usar_num = input("Usar números? (S/N)").lower() == "s"
usar_simb = input("Usar símbolos? (S/N)").lower() == "s"

# Cria a lista de caracteres a serem usados na senha com base nas preferências do usuário
caracteres = ""
if usar_min:
    caracteres += letras_min
if usar_mai:
    caracteres += letras_mai
if usar_num:
    caracteres += numeros
if usar_simb:
    caracteres += simbolos

# Gera a senha aleatória e a exibe na tela
senha = "".join(random.choice(caracteres) for i in range(comprimento))
print("Senha gerada: ", senha)

