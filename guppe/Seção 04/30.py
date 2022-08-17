"""
Leia um valor em real e a cotação do dolar.
Em seguida, imprima o valor correspondente em dolares.
"""
r = float(input('Digite o valor em reais que deseja converter para dolar: '))
d = float(input('Insira a cotação atual do dolar: '))
t = r / d

print(f'O resultado de sua conversão é de {t}')
