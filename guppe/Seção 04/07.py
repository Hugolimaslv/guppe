"""
Leia uma temperatura em graus Farenheit e apresente-a convertida em graus Celcius.
A formula de conversao é: C = 5 * ( F - 32) / 9, sendo F a temperatura em Farenheit e C a temperatura em Celsius.
"""

f = float(input('Digite a temperatura em graus Farenheit que deseja a conversão para Celsius: '))
c = 5 * (f - 32) / 9
print(f'O resultado da conversão de {f}ºC é de {c}ºF')

