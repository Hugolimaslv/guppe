"""
Leia um numero inteiro e imprima a soma do sucessor do seu triplo com o antecessor de seu dobro.
"""
n = int(input('Digite um numero inteiro para obter a soma do triplo de seu sucessor com o dobro de seu antecessor: '))
t = ((n+1) * 3) + ((n-1) * 2)
print(f'A equação tem como resultado {t}')
