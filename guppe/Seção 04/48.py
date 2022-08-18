"""
Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.
"""
t = int(input('Digite uma quantidade de segundos: '))
h = t / 3600
resto = t % 3600
m = resto / 60
s = resto % 60

print(f'{h} horas, {m} minutos e {s} seguntos.')
