### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

valor = 105
fl_valido = False

while fl_valido is not True:
    valor_entrada = int(input("Insira um número: "))
    if valor_entrada == valor:
        fl_valido = True
    else:
        print("Valor inválido. Insira outro número: ")