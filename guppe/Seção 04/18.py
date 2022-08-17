"""
Leia um valor de volume em metros cubicos m³ e apresente-o convertido em litros.
A formula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cubicos
"""

m = float(input('Insira o valor em metros cubicos para ser convertido em litros:\n'))
l = m * 1000

print(f'O resultado da conversão de {m}m³ equivale a {l} litros')
