"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversao é: F = C * (9.0 / 5.0) + 32, sendo F a temperatura em Farenheit e C a temperatura em Celsius.
"""

c = float(input('Digite a temperatura em graus Celsius que deseja a conversão para Farenheit: '))
f = c * (9 / 5) + 32
print(f'O resultado da conversão de {c}ºC é de {f}ºF')

