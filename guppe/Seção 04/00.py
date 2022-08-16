"""
Criar um programa onde identifica a quantidade de trapos para determinada costura.
"""
p1 = int(input('Digite em centimetros a altura necessária para o projeto: '))
p2 = int(input('Digite em centimetros a largura necessária para o projeto: '))
t1 = int(input('Digite em centimetros a altura desejada do trapo: '))
t2 = int(input('Digite em centimetros a largura desejada do trapo: '))

projeto = p1 * p2
t3 = t1 - 2
t4 = t1 - 2
trapo = t3 * t4

t = projeto / trapo

print(f'O numero total de trapo necessarios para a criação é de {t}')
