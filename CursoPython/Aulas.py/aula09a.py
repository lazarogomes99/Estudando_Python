# Análise de Strings

frase = 'Curso em Video Python'

print(len(frase)) # vem de length "comprimento". e aqui em python é usado para ver qual o comprimento da string.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

frase1 = 'Curso em Video Python'

print(frase1.count('o')) #vai contar quantas vezes aparece a letra 'o' na string, podemos passar os parametros entre aspas.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


frase2 = 'Curso em Video Python'

print(frase2.count('o', 0, 13)) #ele vai verificar quantos 'o' tem na string do indice 0 até o indice 13, lembrando que o indice 13 não é contabilizado.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


frase3 = 'Curso em Video Python'

print(frase3.find('deo')) #vai imprimir e indicar onde começou o indice referente ao parametro passado.
# se usassemos - print(frase3.find('android')) - o retorno seria -1, e não existe indice -1. isso significa que o parametro passado para busca não existe.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


print('Curso' in frase3) #existe a palavra curso na string frase? vai retornar true ou false.

print(frase3.replace('Python', 'Android')) #replace significa reposicionar, aqui ele vai trocar o python por android dentro da string.