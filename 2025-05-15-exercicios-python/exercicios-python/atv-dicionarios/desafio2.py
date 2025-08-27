# Crie um programa que converta valores entre diferentes unidades de distância astronômica (parsec, ano-luz, unidade astronômica, minuto-luz e segundo-luz).
# O programa deve solicitar o valor, a unidade de origem e a unidade de destino, e exibir o resultado da conversão.


ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz(ml)", "Segundo-Luz (sl)"]
for i in unidades:
    print(f"As unidades de medida são: {i}")
valor = float(input("Valor a ser convertido: "))
unidade_origem = input("Converter de: ")
unidade_destino = input("Converter para: ")
if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
    print("Essa unidade não é valida.")
else:
    valor_em_ano_luz = valor * ano_luz[unidade_origem]
    valor_convertido = valor_em_ano_luz / ano_luz[unidade_destino]
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido} {unidade_destino}")