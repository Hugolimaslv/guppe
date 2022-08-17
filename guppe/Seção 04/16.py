"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A formula de conversão é: C = P * 2.54, sendo C o comprimento em centimetros e P o comprimento em polegadas.
"""
p = float(input('Informe a medida em polegadas que deseja convertar para centimetros: \n'))
c = p * 2.54

print(f'O resultado da conversão de {p} polegadas para centimetros é de {c}')
