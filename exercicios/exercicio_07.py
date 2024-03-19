### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

import random

def gerar_lista_numeros_aleatorios(tamanho, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

# Defina o tamanho da lista e os limites mínimo e máximo dos números aleatórios
tamanho_lista = 10
minimo = 1
maximo = 100

# Gera a lista de números aleatórios
numeros_aleatorios = gerar_lista_numeros_aleatorios(tamanho_lista, minimo, maximo)

numeros_aleatorios.sort()
print(numeros_aleatorios)