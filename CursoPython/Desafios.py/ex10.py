#faça um conversor de moedas. 

real = float(input('Quanto dinheiro você tem em carteira? R$'))

dolar = real / 5.26

print('Com R${} você pode comprar U${:.2f}'.format(real, dolar))