### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

registros_vendas = [
    {'categoria': 'Eletrônicos', 'valor': 1000},
    {'categoria': 'Roupas', 'valor': 500},
    {'categoria': 'Eletrônicos', 'valor': 800},
    {'categoria': 'Alimentos', 'valor': 300},
    {'categoria': 'Roupas', 'valor': 700},
    {'categoria': 'Alimentos', 'valor': 400}
]

total_vendas_por_categoria = {}

for venda in registros_vendas:
    categoria = venda['categoria']
    valor_venda = venda['valor']
    
    if categoria in total_vendas_por_categoria:
        total_vendas_por_categoria[categoria] += valor_venda
    else:
        total_vendas_por_categoria[categoria] = valor_venda

for categoria, total_vendas in total_vendas_por_categoria.items():
    print(f"Total de vendas na categoria {categoria}: R${total_vendas}")