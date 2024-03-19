### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

import random

def gerar_lista_numeros_aleatorios(tamanho, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

# Defina o tamanho da lista e os limites mínimo e máximo dos números aleatórios
tamanho_lista = 10
minimo = 1
maximo = 100

# Gera a lista de números aleatórios
numeros_aleatorios = gerar_lista_numeros_aleatorios(tamanho_lista, minimo, maximo)

pares = []

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        pares.append(numero)

print(f'Lista de números pares: {pares}')