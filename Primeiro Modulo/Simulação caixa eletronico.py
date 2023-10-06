# exercicio de simulação de caixa eletronico

saldo = float(1000.0)

opcao = 0

while opcao != 4 :

    print(" ")
    print("Caixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Realizar Deposito")
    print("3 - Realizar Saque")
    print("4 - Sair")
    print(" ")

    opcao = int(input("Escolha a opção desejada (1 - 4)  "))   


        # Verificar Saldo

    if opcao == 1 :

        print("O Seu saldo é R$", saldo)


      # Depositar dinheiro

    if opcao == 2 :

        deposito = float(input("Digite a quantia a depositar:  "))

        if deposito > 0 :

            saldo = float(saldo + deposito)
        
            print(f"Deposito de R${deposito} realizado com sucesso!")

        
        else :
        
            print("Houve um erro na tentativa do deposito")
            print("Tente novamente!")


      # Sacar dinheiro

    if opcao == 3 :

        saque = float(input("Digite a quantia do saque:  "))

        if saque > 0 and saque <= saldo :

            saldo = float(saldo - saque)

            print(f"Saque de R${saque} realizado com sucesso!")
        
        else :
            
            print("Saldo insuficiente")


    #Sair do caixa eletrônico

print("Obrigado por utilizar nosso caixa eletrônico. Até mais!")