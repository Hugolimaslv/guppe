"""
Faça uma leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
v1, v2, v3 = int(input('Digite um numero inteiro: ')), int(input('Digite um numero inteiro: ')), int(input('Digite um '
                                                                                                           'numero '
                                                                                                           'inteiro: '
                                                                                                           ''))
t = v1 ** 2 + v2 ** 2 + v3 ** 2

print(f'O resultado da soma dos quadrados de {v1}, {v2} e {v3} é de {t}')

