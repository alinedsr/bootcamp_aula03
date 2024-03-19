### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacoes = [
    {'id': 1, 'valor': 1000, 'hora': '17:59'},
    {'id': 2, 'valor': 12000, 'hora': '20:11'},
    {'id': 3, 'valor': 12000, 'hora': '10:30'}
]

for transacao in transacoes:
    if transacao['valor'] > 10000 or transacao['hora'] > '18:00' or transacao['hora'] < '09:00':
        print(f'A transação {transacao['id']} foi bloqueada.')
    else:
        print(f'A transação {transacao['id']} está liberada.')