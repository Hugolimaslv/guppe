"""
Escopo de Variaveis

Variaveis globais;
    - Variaveis globai sao reconhecidas, ou seja, seu escopo compreende todo o programa.

        - numero = 50
        - nome = 'Let me in'

Variaveis locais;
    - Variaveis locais são reconhecidas apanas no bloco onde foram declaradas, ou seja, seu escopo esta limitado ao
    bloco onde foi declarada.

        numero = 2
        if numero > 10:
            novo = numero + 10
            print(novo)

    - Conforme exemplo acima, variavel local, caso não seja criada não conseguirá inprimi-la no código

Para declarar variaveis em python:

nome_da_variavel = valor_da_variavel // nome = 'let me in'

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variavel, nós não colocamos o tipo
de dado dela.
Este tipo é inferido ao atribuirmos um valor à mesma.
"""

nome = 'let me in'
print(nome)
print(type(nome))
