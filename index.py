def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    =>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if(valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(("\n=== Depósito realizado com sucesso! ==="))
    else:
        print("O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nO valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nNúmero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
