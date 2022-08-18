"""
Receba a altura do degrau de uma escada e a altura que o usuario deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuario devera subir para atingir o seu objetivo.
"""
d = float(input('Insira a altura do degrau: '))
h = float(input('Insira a altura que deseja alcançar: '))
t = h / d
print(f'Será necessário utilizar {t} degraus para chegar a altura desejada.')

