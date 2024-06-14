menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":

        print("Qual o valor que sará depositado?")
        valor = float(input())

        if valor > 0:
            saldo += valor
            print("Deposito realizado com sucesso!")
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    elif opcao == "s":

        if LIMITE_SAQUES > 0:
            print("Qual o valor que sará sacado?")
            valor = float(input())
            if valor <= 500 and valor <= saldo:
                saldo -= valor
                print("Saque realizado com sucesso!")
                LIMITE_SAQUES -= 1
                extrato += f"Saque: R$ {valor:.2f}\n"
            else:
                print("Saque inválido.")
        elif LIMITE_SAQUES <= 0:
            print("Limite de saques atingido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")