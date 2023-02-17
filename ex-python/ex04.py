'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
                                                                        '''
from math import hypot

catetoOp = float(input('Digite o comprimento do cateto oposto:\n '))
catetoAd = float(input('Digite o comprimento do cateto adjacente:\n '))

# o .hypot é para calcular a hipotenusa desde que oferecemos os valores dos catetos.
hipotenusa = hypot(catetoOp, catetoAd)

print('O comprimento do cateto oposto "{}" mais o cateto Adjacente "{}" é igual à {:.2f} '.format(
    catetoOp, catetoAd, hipotenusa))
