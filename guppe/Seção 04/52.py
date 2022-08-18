"""
Três amigos jogaram na loteria. Caso eles ganhem, o premia deve ser repartido proporcionalmente ao valor que cada um
deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do premio e imprima o quanto cada um ganharia com
base no valor investido.
"""

p1 = input('Digite o seu primeiro nome: ')
a1 = float(input(f'{p1.capitalize()}, insira o valor de seu investimento: '))
p2 = input('Digite o seu primeiro nome: ')
a2 = float(input(f'{p2.capitalize()}, insira o valor de seu investimento: '))
p3 = input('Digite o seu primeiro nome: ')
a3 = float(input(f'{p3.capitalize()}, insira o valor de seu investimento: '))

va = a1 + a2 + a3

print(f'O valor total arrecado para as apostas foi de R$ {va}0.')

l = float(input('Insira o valor do prêmio da loteria: '))

print(f'O valor da premio é de R$ {l}0.')

r1 = (a1 * 100) / va
r2 = (a2 * 100) / va
r3 = (a3 * 100) / va

print(f'{p1.capitalize()} apostou {a1} e receberá R$ {l * r1 / 100}0.\n'
      f'{p2.capitalize()} apostou {a2} e receberá R$ {l * r2 / 100}0.\n'
      f'{p3.capitalize()} apostou {a3} e receberá R$ {l * r3 / 100}0.\n')

