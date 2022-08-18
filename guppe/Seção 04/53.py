"""
Faça um programa para ler as dimensões de um terreno (comprimento e largura), bem como o preço do metro de tela.
Imprima o custo para cercar este mesmo terreno com a tela.
"""
c = float(input('Insira o comprimento do terreno: '))
k = float(input('Insira a largura do terreno: '))
p = float(input('Insira o valor do metro da tela: '))

t = ((c * 2) + (k * 2)) * p

print(f'O valor para da tela para cercar todo terreno é de R$ {t}0.')
