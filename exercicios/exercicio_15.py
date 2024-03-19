### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

parada = 100
i = 0
lista = [1, 10, 200, 500, 100, 400, 85]

while i < len(lista):
    if lista[i] == parada:
        print("Encerrando o processamento.")
        break
    print(f'Processando item nro {lista[i]}')
    i += 1