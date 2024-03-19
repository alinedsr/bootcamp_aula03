### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

produto_valido = False
quantidade_valida = False
preco_valido = False

while produto_valido is not True:
    try:
        produto = input("Digite o nome do produto: ")
        if produto.strip() != "":
            produto_valido = True
        else:
            print("Você não inseriu um nome de produto válido. Por favor, revise a entrada.")
    except Exception as e:
        print(e)
        

while quantidade_valida is not True:
    try:
        quantidade = int(input(f"Insira a quantidade de {produto} disponível no estoque: "))
        if quantidade >= 0:
            quantidade_valida = True
        else:
            print("A quantidade deve ser maior ou igual a zero. Por favor, insira a quantidade novamente.")
    except Exception as e:
        print(e)
        print("A quantidade digitada não é válida. Insira a quantidade novamente.")


while preco_valido is not True:
    try:
        preco = float(input(f"Digite o preço de cada unidade de {produto}: "))
        if preco >= 0:
            preco_valido = True
        else:
            print("O preço deve ser maior ou igual a zero. Por favor, digite novamente.")
    except Exception as e:
        print(e)
        print("O valor digitado não é um preço válido. Insira o preço novamente")