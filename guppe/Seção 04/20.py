"""
Leia o valor de massa em quilogramas e apresente-o convertido em libras.
A formula de conversão é: L = k / 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

k = float(input('Insira o valor da massa em quilogramas para ser convertida para libras: '))
l = k / 0.45
print(f'O resultado da conversão é de {l} libras')
