"""
Leia um angulo em graus e aprensente-o convertido em radianos.
A formula de conversão é R = G * Pi / 180, sendo G o angulo em graus, R em radianos e Pi = 3,14.
"""

g = float(input('Digite o angulo em graus que será convertido para radianos: '))
pi = 3.14
r = g * pi / 180
print(f'O resultado da conversão de {g}º é de {r}.')
