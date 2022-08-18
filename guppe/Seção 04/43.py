"""
Escreva um programa de ajuda para vendedores. A partir de de um valor total lido, mostre:
- o total a pagar com 10% de desconto;
- o valor de cada parcela, no parcelamento em 3x sem juros;
- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com o desconto)
"""
p = float(input('Insira o valor do produto vendido: '))
v = p - (p * 10 / 100)
x = p / 3
c = v * 5 / 100
print(f'O valor para pagamento a vista á de R$ {v};\n'
      f'O valor da parcela para o parcelamento em 3x é de R$ {x};\n'
      f'O valor da comissão do vendedor é de R$ {c}.')

