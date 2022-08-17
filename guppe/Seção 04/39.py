"""
A importancia de R$ 780.000.00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
- O primeiro ganhador receberá 46%.
- O segundo ganhador receberá 32%.
- O terceiro ganhador receberá o restante.
"""
p = 780000.00
g1 = (p * (46 / 100))
g2 = (p * (32 / 100))
g3 = p - (g1 + g2)
t = g1 + g2 + g3
print(f'O primeiro ganhador levará a quantia de R$ {g1};\n'
      f'O segundo ganhador levará a quantia de R$ {g2};\n'
      f'O terceiro ganhador levará a quantia de R$ {g3}\n;'
      f'Com isto, toda a quantia R$ {t} foi distribuida entre os vencedores.')
