"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A formula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""
j = float(input('Digite o valor em jardas que deseja converter para metros: '))
m = 0.91 * j

print(f'O resultado da conversão é de {m} metros.')
