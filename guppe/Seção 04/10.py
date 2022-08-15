"""
Leia uma velocidade em km/h e apresente-a convertida em m/s.
A formula da conversão é: m = k / 3.6, sendo k a velocidade em km/h e m a velocidade em m/s.
"""

k = float(input('Digite uma velocidade em km/h para ser convertira para m/s: '))
m = k / 3.6
print(f'O resultado da conversão de {k}km/h é de {m}m/s.')
