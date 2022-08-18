"""
Receba o salário-base de um funcionário.
Calcule e imprima o salario a receber, sabendo que:
- gratificação de 5% sobre salario base
- 7% de imposto sobre o salario base
"""
b = float(input('Insira o valor de seu salario base: '))
g = b * 5 / 100
i = b * 7 / 100
s = b + g - i
print(f'O valor que será recebido é de R$ {s}.')
