

'''Faça um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiusculas.
    - O nome com todas as letras minusculas.
    - Quantas letras ao todo(sem considerar espaços).
    - Quantas letras tem o primeiro nome.'''


nome = input('Qual seu nome completo? ')

print("Nome em letras maiúsculas: ", nome.upper()) #vai imprimir o nome todo em maiusculo. 
print("Nome em letras Minúsculas", nome.lower()) #vai imprimir o nome todo em minusculo.

qtd_letras = len(nome.replace(" ", "")) # LEN para contar o número de caracteres e usei o replace para reposicionar o que for espaço para "" não ter espaço.
print("Quantidade de letras do nome completo digitado: {}".format(qtd_letras)) #vai imprimir resultado armazenado em qtd_letras.


p_nome = nome.split()[0] #vai separar cada palavra de acordo com o espaço em branco, na mesma linha puxei o indice 0 do split que seria a primeira palavra.
qtd_nome = len(p_nome) #com a primeira palavra armazenada na variavel p_nome, usei o len para contar a quantidade de letras da palavra.
print("A quantidade de letras no primeiro nome digitado: {}".format(qtd_nome)) # imprimindo na tela!
