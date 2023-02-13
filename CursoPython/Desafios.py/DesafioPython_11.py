#faça um programa que leia altura e largura de uma parede e diga 
# quantos litros o usuario precisa para pintar a parede.

largura = float(input('Qual largura da parede?'))
altura = float(input('Qual a altura? '))
litros = (largura*altura)/2

print('Sua parede tem dimenção {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(largura, altura, largura*altura))
print('Para pintar essa parede você vai precisar de {:.2f} litros de tinta.'.format(litros))