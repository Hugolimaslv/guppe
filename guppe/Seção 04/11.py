"""
Leia uma velocidade em m/s e apresente-a convertida em km/h.
A formula da conversão é: m = k / 3.6, sendo k a velocidade em km/h e m a velocidade em m/s.
"""

m = float(input('Digite uma velocidade em m/s para ser convertira para km/h: '))
k = m * 3.6
print(f'O resultado da conversão de {m}m/s é de {k}km/s.')
