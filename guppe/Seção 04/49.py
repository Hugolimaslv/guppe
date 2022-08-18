"""
Faça um programa para ler o horario (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiencia
biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""
h = int(input('Digite a hora inicial da experiência: '))
m = int(input('Digite o minuto inicial da experiência: '))
s = int(input('Digite o segundo inicial da experiência: '))

print(f'O inicio de sua  experiência foi as {h} horas, {m} minutos e {s} segundos.')

d = int(input('Digite a duração em segundos da experiencia: '))

print(f'O tempo de duração da sua experiencia é de {d} segundos.')

horas = d / 3600
resto = d % 3600
minutos = resto / 60
segundos = resto % 60

hf = h + horas
mf = m + minutos
sf = s + segundos

print(f'A sua experiencia terminará as {hf} horas, {mf} minutos e {sf} segundos.')