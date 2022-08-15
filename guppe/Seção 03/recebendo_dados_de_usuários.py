"""
Recebendo dados de usuários

input() -> Todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples; -> 'Hugo Lima'
- Aspas duplas; -> "Hugo Lima"
- Aspas simples triplas; -> '''Hugo Lima'''
- Aspas duplas trilas; -> Igual toda a formatação deste comentário
"""
# Entrada de dados
nome = input('Qual o seu nome? ')

# Processamento


# Saída de dados

print('Olá {}, tenha um bom dia!'.format(nome.title()))

idade = int(input('Qual a sua idade? '))

print(f'{nome.upper()} nasceu em {2022 - idade}.')
