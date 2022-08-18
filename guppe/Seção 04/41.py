"""
Faça um programa que leia o valor da hora de trabalho e o numero de horas trabalhadas no mes.
Imprima o valor a ser pago ao funcionario, adicionando 10% sobre o valor calculado.
"""
h = int(input('Informe o numero de horas trabalhadas no mês: '))
s = float(input('informe o valor da hora trabalhada: '))
m = h * s
a = m * 10 / 100
t = m + a
print(f'o valor a receber pelo mês trabalhado é de R$ {t}.')

