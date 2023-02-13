#Faça um programa que converta metros em centimentos e em milimetros. 

metros = float(input('Quantos metros você quer converter para centimetros e milimetros? '))

centimetros = metros * 100
milimetros = metros * 1000

print('Convertendo {}m em Centimentros ficaria {}cm e em Milimetros ficaria {}mm'.format(metros, centimetros, milimetros))