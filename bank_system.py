menu = """


    [1] depositar
    [2] sacar
    [3] extrato
    [4] sair
    
    
=>"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        
        if valor_deposito < 0:
            print("Digite valores inteiros e positivos!")
        else:
            mensagem_deposito = f"| Foi depositado R$ {valor_deposito} |\n"
            extrato += mensagem_deposito
            saldo += valor_deposito

        print(f"Saldo Atual: {saldo:.2f}")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque < 0:
            print("Digite valores inteiros e positivos!")
        else:
            if numero_saques < LIMITE_SAQUE:
                if valor_saque <= limite:
                    if valor_saque <= saldo:
                        saldo -= valor_saque
                        mensagem_saque = f"| Foi sacado R$ {valor_saque}  |\n"
                        extrato += mensagem_saque
                        numero_saques += 1
                    else:
                        print(f"Não é possível sacar esse valor pois o saldo é insuficiente")
                else:
                    print(f"Você só pode sacar até R$ {limite}")
            else:
                print("Você já atingiu o limite de saques dessa sessão!")
        
        print(f"Saldo Atual: {saldo:.2f}")
        
    elif opcao == 3:
        print("\n============================ EXTRATO ============================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"Saldo Atual: {saldo:.2f}")
        print("===================================================================")
    elif opcao == 4:
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')