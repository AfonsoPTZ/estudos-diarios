# Criar um programa que solicita valor de vendas e o mês onde
# cada venda ocorreu. Independente de repetição de mese o
# aplicativo deve totalizar por mês todas as vendas cadastradas.
# Ao final deve informar o valor de vendas de todos os meses do
# ano. Obs.: se for digitado errado o nome do mê informar que o
# mês é inválido.
meses = {
    'janeiro': 0,
    'fevereiro': 0,
    'março': 0,
    'abril': 0,
    'maio': 0,
    'junho': 0,
    'julho': 0,
    'agosto': 0,
    'setembro': 0,
    'outubro': 0,
    'novembro': 0,
    'dezembro': 0
}
while True:
    valor = float(input('Digite o valor da venda: '))
    mes = input('Digite o mês da venda: ').lower()
    if mes in meses:
        meses[mes] += valor
    else:
        print('Mês inválido. Tente novamente.')
    if  input('Deseja continuar? (s/n): ').lower() == 'n':
        break
print('Total de vendas por mês:')
for mes, total in meses.items():
    print(f"mes: {mes} - total: R$ {total:.2f}")