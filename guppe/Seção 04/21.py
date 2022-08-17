"""
Leia o valor de massa em libras e apresente-o convertido em quilogramas.
A formula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

l = float(input('Insira o valor da massa em libras para ser convertida para quilogramas: '))
k = l * 0.45
print(f'O resultado da conversão é de {k} quilogramas')
