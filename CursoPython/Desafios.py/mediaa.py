# fazendo um programa que lê 4 notas e caso a média seja maior que 7, imprime na tela aprovado, caso contrario reprovado.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))
media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print('A média do aluno foi {:.2f}, PARABÉNS, APROVADO.'.format(media))
else:
    print('A média do aluno foi {:.2f}, foi REPROVADO.'.format(media))
