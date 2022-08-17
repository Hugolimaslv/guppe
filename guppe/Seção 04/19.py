"""
Leia um valor de volume em litros e apresente-o convertido em metros cubicos m³.
A formula de conversão é> M = L / 1000, sendo L o volume em litros e M o volume em metros cubicos.
"""

l = float(input('Insira o valor em litros para ser convertido em metros cubicos:\n'))
m = l / 1000

print(f'O resultado da conversão de {l} litros equivale a {m}m³')
