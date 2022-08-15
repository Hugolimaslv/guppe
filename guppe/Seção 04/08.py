"""
Leia uma temperatura em graus Kelvin e aprensente-a convertida em graus Celsius.
A formula de conversão é c = k - 273.15, sendo que c é a temperatura em Celsius e K a temperatura em Kelvin.
"""

k = float(input('Digite uma temperatura em graus Kelvin para ser convertida para graus Celsius: '))
c = k - 273.15
print(f'O resultado da conversão de {k}ºK é de {c}ºC.')
