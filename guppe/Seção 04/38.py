"""
Leia o salário de um funcionário.
Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
"""
s = float(input('Digite o valor do seu salário para calcular o reajuste de 25%: '))
r = s + (s * 25 / 100)
print(f'O valor do salário após o reajuste é de R$ {r}.')
