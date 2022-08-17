"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da equação V = pi * r² * h, onde pi = 3,141592.
"""
h = float(input('Digite a altura do cilindro circular que deseja obter o volume:\n'))
r = float(input('Digite o raio do cilindro circular que deseja obter o volume:\n'))
pi = 3.141592
v = pi * (r ** 2) * h
print(f'O volume do cilindro circular é de {v}.')
