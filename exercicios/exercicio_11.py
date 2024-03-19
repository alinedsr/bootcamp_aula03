### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

fl_continue = False

while fl_continue is not True:
    entrada = input("Insira um valor ou digite 'sair' para interromper. ")
    if entrada == 'sair':
        fl_continue = True
    else:
        pass