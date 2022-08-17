"""
Leia quatro notas, calcule a media aritimetica e imprima o resultado
"""
b1 = float(input('Digite o valor de sua nota no primeiro bimestre: '))
b2 = float(input('Digite o valor de sua nota no segundo bimestre: '))
b3 = float(input('Digite o valor de sua nota no terceiro bimestre: '))
b4 = float(input('Digite o valor de sua nota no quarto bimestre: '))
m = (b1 + b2 + b3 + b4) / 4

print(f'A média de suas notas é: {m}')
