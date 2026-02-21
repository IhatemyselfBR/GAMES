import random

opcao1 = "papel"
opcao2 = "pedra"
opcao3 = "tesoura"

while True:
    mresposta = input("Sua escolha : ")

    cresposta = random.choice([opcao1, opcao2, opcao3])
    print(cresposta)

    if mresposta == cresposta:
        print("empate")

    elif (
        (mresposta == opcao1 and cresposta == opcao2) or
        (mresposta == opcao2 and cresposta == opcao3) or
        (mresposta == opcao3 and cresposta == opcao1)
    ):
        print("voce ganhou")

    else:
        print("voce perdeu")
