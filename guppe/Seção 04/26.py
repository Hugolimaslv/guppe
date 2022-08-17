"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A formula de conversão é: H = M * 0.0001, sendo M a area em metros quadrados e H a area em hectares.
"""
m = float(input('Digite o valor em metros quadrados que deseja converter para hectares: '))
h = m * 0.0001

print(f'O resultado da conversão é de {h} hectares.')
