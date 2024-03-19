### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

parada = 100

lista = [1, 10, 200, 500, 100, 400, 85]

for item in lista:
    if item != parada:
        print(item)
    else:
        break