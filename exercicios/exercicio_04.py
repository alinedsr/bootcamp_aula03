### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
import re
validador_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')


idade_valida = False
email_valido = False

while idade_valida is not True:
    try:
        idade = int(input("Insira a sua idade: "))
        if idade >= 18 and idade <= 65:
            idade_valida = True
        else:
            print("Idade inválida.")
    except Exception as e:
        print(e)

while email_valido is not True:
    try:
        email = input("Insira o seu e-mail: ")
        if validador_email.match(email):
            email_valido = True
        else:
            raise ValueError("O e-mail está incorreto.")
    except Exception as e:
        print(e)