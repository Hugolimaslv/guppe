"""
Leia uma temperatura em graus Celsius e aprensente-a convertida em graus Kelvin.
A formula de conversão é k = c + 273.15, sendo que c é a temperatura em Celsius e K a temperatura em Kelvin.
"""

c = float(input('Digite uma temperatura em graus Celsius para ser convertida para graus Kelvin: '))
k = c + 273.15
print(f'O resultado da conversão de {c}ºC é de {k}ºK.')
