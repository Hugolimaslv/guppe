"""
Tipo Booleano

Algebra Boobleana, criada por George Boole

2 constantes: Verdadeiro ou Falso

True -> Verdadeiro
False -> False

obs. Sempre com a inicial maiúscula.
"""

ativo = True
off = False

print(ativo)

"""
Operações básicas
"""

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso.
Se for falso, o resultado será verdadeiro.
A resposta será sempre o contrário.
"""

print(not ativo)

# Ou (or):

"""
É uma operação binária, depende de dois valores.
Algum dos valores apresentados deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or off)

# E (and):

"""
É uma operação binária, depende de dois valores.
Ambos os valores deverão ser verdadeiros.

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""

print(ativo and off)
