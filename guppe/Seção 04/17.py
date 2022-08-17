"""
Leia um valor de comrpimento em centimetros e apresente-o convertido em polegadas.
A formula de conversão é: P - C / 2.54, sendo C o comprimento em centimentros e P o comprimento em polegadas.
"""

c = float(input('Informe a medida em centimetros que deseja convertar para polegadas: \n'))
p = c / 2.54

print(f'O resultado da conversão de {c} centimetros para polegadas é de {p}')
