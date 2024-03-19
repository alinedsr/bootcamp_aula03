### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando

dados = [
    {'id': 1, 'nome': 'Aline', 'endereco': 'Rua A', 'telefone': 123},
    {'id': 2, 'nome': 'João', 'endereco': 'Rua A', 'telefone': 321},
    {'id': 3, 'nome': 'Matheus', 'endereco': 'Rua A', 'telefone': 456},
    {'id': 4, 'nome': 'Helena', 'endereco': 'Rua A', 'telefone': 789},
    {'id': 5, 'nome': 'Joana', 'endereco': 'Rua A', 'telefone': 147},
    {'id': 6, 'nome': 'Danielli', 'endereco': 'Rua A', 'telefone': 258},
    {'id': 7, 'nome': 'Beatriz', 'endereco': 'Rua A', 'telefone': 369},
    {'id': 8, 'nome': 'Carlos', 'endereco': 'Rua A', 'telefone': 753},
    {'id': 9, 'nome': 'Lucas', 'endereco': 'Rua A', 'telefone': 000},
    {'id': 10, 'nome': 'Raquel', 'endereco': 'Rua A'},
]

usuarios_com_campos_faltando = []

for usuario in dados:
    if any(valor is None for valor in usuario.values()) or len(usuario) < 4:
        usuarios_com_campos_faltando.append(usuario)

for usuario in usuarios_com_campos_faltando:
    print(usuario)
