'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente. 

'''
nome_completo = str(input('Digite seu nome compelto: ')).split() #método split separa a string de acordo com o separador, nesse caso como padrão é o espaço.
print('Seu primeiro nome é {}'.format(nome_completo[0])) #peço para imprimir a variavel com indice 0, oque vai puxar a primeira cadeia de caracteres separada.
print('Seu último nome é {}'.format(nome_completo[-1])) # mesma coisa, apenas puxo a ultima cadeia de caracteres que foi separada pelo split.
