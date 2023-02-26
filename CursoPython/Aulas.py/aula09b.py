# Transformação de String

frase = '   Curso em Video Python    '
frase1 = '   Curso em Video Python    '


print(frase.replace('Python', 'Android')) #replace significa reposicionar, aqui ele vai trocar o python por android dentro da string.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

print(frase.upper()) #Significa pra cima, ou seja, toda a string ficará em maiusculo.

print(frase.lower()) #Vai deixar toda a string em minusculo.

print(frase1.capitalize())#Vai deixar apenas o primeiro caractere da palavra em maiusculo dentro da string. Primeiro joga tudo pra minusculo, e apenas o primeiro caractere joga para maiusculo.


print(frase.title()) #vai contar as palavras de acordo com os espaços, e fazer o captalize palavra por palavra. deixando os primeiros caracteres em maiusculo.

print(frase.strip())# vai retirar espaços do inicio e do final da string.

print(frase.rstrip()) # r vem de right, vai retirar os espaços apenas da direita da string.

print(frase.lstrip()) # l vem de left, vai retirar os espaços apenas da esquerda da string.