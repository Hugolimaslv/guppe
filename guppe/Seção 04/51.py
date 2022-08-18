"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule a sua distancia da origem (0, 0).
"""
x = float(0)
y = float(0)
z = float(0)
xp = float(input('Digite a coordenada de x: '))
yp = float(input('Digite a coordenada de y: '))

d = ((((xp - x) ** 2) + ((yp - y) ** 2)) ** 0.5)

print(f'A distancia entre as cordenadas de sua origem é de {d}.')
