from random import choice

jagador_vitorias = 0
maq_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()

    if esc_jogador ==  "pedra":
        return(esc_jogador)
    elif esc_jogador  == "papel":
        return(esc_jogador)
    elif  esc_jogador == "tesoura":
        return(esc_jogador)
    else:
        print("Opção Inválida! Por favor escolha entre Pedra, Papel ou Tesoura.")
        Opcao_Jogador()

def Opcao_Maq():
    esc_marquina = choice(["pedra", "papel", "tesoura"])
    return(esc_marquina)



while True:

    print("-" *30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maq()
    print("-" *30)

    if esc_jogador == "pedra" and esc_maquina == "tesoura" \
        or esc_jogador == "papel" and  esc_maquina == "pedra" \
           or esc_jogador == "tesoura" and esc_maquina == "papel":
           # jogador ganha
           print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}"
            " resultado: Você Ganho! ")
           jagador_vitorias += 1

    elif esc_jogador == esc_maquina:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}"
            " resultado: Empate! ")
    else:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}"
            " resultado: Você Perdeu! ")
        maq_vitorias += 1

    

    print("-" *30)
    print(f"Vitorias do jogador:  {jagador_vitorias}")
    print(f"Vitorias do Maquina:  {maq_vitorias}")
    print("-" *30)

    esc_jogador = input("Você quer jogar novamente? ")

    if esc_jogador in ["SIM", "sim", "S", "s"]:
        pass
    elif  esc_jogador in ["NÃO", "não", "N", "n"]:
        break
    else:
        break