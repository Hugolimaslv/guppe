"""
Leia uma distancia em milhas e apresente-a convertida em quilometros.
A formula de conversão é K = 1.61 * M, sendo K a distancia em quilometros e M a distancia em milhas.
"""

m = float(input('Informe a distancia em milhas que voce dejesa transformar em quilometros: '))
k = 1.61 * m
print(f'A transformacao de {m} milhas tem como resultado {k} quilometros')
