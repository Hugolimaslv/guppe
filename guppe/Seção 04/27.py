"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A formula de conversão é: M = H * 1000, sendo M a area em metros quadrados e H a area em hectares.
"""
h = float(input('Digite o valor em hectares que deseja converter para metros quadrados: '))
m = h * 1000

print(f'O resultado da conversão é de {m}m².')
