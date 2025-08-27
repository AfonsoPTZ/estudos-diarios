votos = []

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")
print("Digite 0 para encerrar a votação.")

while True:
    voto = int(input("Digite o número correspondente ao seu voto: "))
    if voto == 0:
        break
    if 1 <= voto <= 6:
        votos.append(voto)
    else:
        print("Opção inválida. Por favor, vote em um número entre 1 e 6.")
print("Votação encerrada.")
print("Sistema Operacional             Votos             %")
print("-----------------------------------------------------")
print("Windows Server             ", votos.count(1), "             ", (votos.count(1) / len(votos)) * 100, "%")
print("Unix                       ", votos.count(2), "             ", (votos.count(2) / len(votos)) * 100, "%")
print("Linux                      ", votos.count(3), "             ", (votos.count(3) / len(votos)) * 100, "%")
print("Netware                    ", votos.count(4), "             ", (votos.count(4) / len(votos)) * 100, "%")
print("Mac OS                     ", votos.count(5), "             ", (votos.count(5) / len(votos)) * 100, "%")
print("Outro                      ", votos.count(6), "             ", (votos.count(6) / len(votos)) * 100, "%")
print("-----------------------------------------------------")
print("Total de votos: ", len(votos))
if len(votos) == 0:
    print("Nenhum voto foi computado.")
elif max(set(votos), key=votos.count) == 1:
    print("Deu impate")
else:
    print("Sistema Operacional mais votado: ", max(set(votos), key=votos.count))
    ###professor nao consegui fazer o progama verificar o empate###