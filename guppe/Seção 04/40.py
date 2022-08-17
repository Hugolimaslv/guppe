"""
Uma empresa contrata um encanador a R$ 30,00 por dia.
Faça um programa que solicite o numero de dias trabalhados pelo encanador e imprima a quantia liquida que devera ser
paga, sabendo-se que sao descontados 8% para imposto de renda.
"""
d = int(input('Digite o numero de dias trabalhados para saber o valor do salário líquido:\n'))
dia = 30.00
i = (d * dia) * 8 / 100

s = dia * d - i
print(f'O valor líquido para {d} dias trabalhados é de R$ {s}.')

