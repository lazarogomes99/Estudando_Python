'''
Conversor de temperatura: Crie um programa que 
converte temperaturas de Celsius para Fahrenheit e vice-versa.
'''

celsius = float(input('Digite a temperatura em CELSIUS: '))
fah = float(input('Digite a temperatura em FAHRENHEIT: '))
converte_cf = (celsius * 1.8 + 32)
converte_fc = (fah -32)/1.8

print(' C O N V E R T E N D O  .........')

print('A temperatura digitada em Celsius, {} graus Celsius, convertida para Fahrenheit seria: {} graus Fahrenheit.'.format(celsius, converte_cf))
print('A temperatura digitada em Fahrenheit, {} graus Fahrenheit, convertida para Celsius seria {} graus Celsius.'.format(fah, converte_fc))
