"""
String

Um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> '1', 'hola', 'True', '45.7'
- Estiver entre aspas duplas -> "1", "hola", "True", "45.7"
- Estiver entre aspas simples triplas -> '''1''', '''hola''', '''True''', '''45.7'''
- Estiver entre aspas duplas triplas -> Exemplo consta no método de anotação

p.s. "\n" serve para pular linha

upper() -> Tudo maiusculo
lower() -> Tudo minusculo
title() -> Primeira letra de cada palavra maiuscula
capitalize() -> Primeira letra maiuscula
split() -> Transforma em uma lista de strings
print(nome[0:3])    # Slice de string
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
replace -> Troca caracteres
"""

nome = 'let me in'
print(nome.upper())
print(type(nome))
print(nome[0:3])    # Slice de string
print(nome.split()[1])
print(nome[::-1])
a = nome.split()
print(a)
print(nome.replace('i', 'in'))
