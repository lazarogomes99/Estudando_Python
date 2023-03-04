#Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Qual o nome da sua cidade?  '))

cidade = cidade.strip() # Remove todos os espaços no inicio e no fim.

if cidade[:5].upper() == "SANTO": # condição que vai deixar do indice 0 até o 5 em maiusculo e confirmar se é igual a "SANTO"
    print('O nome da cidade começa com "SANTO".' )
else:
     print('Não começa com "SANTO"')

