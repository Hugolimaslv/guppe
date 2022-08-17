"""
Sejam a e b os catetos de um triangulo, onde a hipotenusa é obitida pela equação: h = (a² + b²) * ¹/².
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa atraves da equação.
"""
a = float(input('Digite o valor do cateto maior:\n'))
b = float(input('Digite o valor do cateto menor:\n'))


h = (((a ** 2) + (b ** 2)) ** (1 / 2))
print(f'O valor da hipotenusa é de {h}.')
