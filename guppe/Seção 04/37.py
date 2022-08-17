"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de
12%.
"""
p = float(input('Insita o valor do produto que deverá ter desconto de 12%: \n'))
d = p - (p * 12 / 100)
print(f'O valor a ser cobrado é de {d}.')
