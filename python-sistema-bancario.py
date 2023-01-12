## Desafio: Criando um sistema bancário em python, com  limite de  três saques diário de R$ 500,00 cada um.

menu = """ 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input(" Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falhou! O valor informado é invalido")
    elif opcao == "s":
        valor = float(input(" Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! O número máximo de saque excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:  R$: {valor: .2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é invalido")
    elif opcao == 'e':
        print("\n=====EXTRATO=====")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=========================")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
         
                  