"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A formula de conversão é: M = A * 4048.58,sendo M a area em metros quadrados e A a area em acres.
"""
a = float(input('Digite o valor da area em acres que deseja converter para metros quadrados: '))
m = a * 4048.58

print(f'O resultado da conversão é de {m}m².')
