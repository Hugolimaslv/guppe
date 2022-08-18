"""
Faça um programa que leia um numero inteiro positivo de três digitos (de 100 a 999).
Gere outro numero formado pelos digitos invertidos do numero lido.
Exemplo
    - numero_lido = 123
    = numero_gerado = 321
"""
numero_lido = int(input('Insira um numero de três dígitos: '))

print(f'O numero lido é {numero_lido}.')

numero_gerado = numero_lido[::-1]

print(f'O numero gerado é {numero_gerado}.')
