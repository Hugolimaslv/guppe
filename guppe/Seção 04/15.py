"""
Leia um angulo em radianos e aprensente-o convertido em graus.
A formula de conversão é G = R * 180 / Pi, sendo G o angulo em graus, R em radianos e Pi = 3,14.
"""

r = float(input('Digite o angulo em radianos que será convertido para graus: '))
pi = 3.14
g = r * 180 / pi
print(f'O resultado da conversão de {r} é de {g}º.')
