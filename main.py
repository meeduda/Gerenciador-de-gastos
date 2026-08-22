gastos = []

while True:
    opcao = input("Escolha uma opção: \n1- Cadastrar gasto \n2- Ver gastos cadastrados \n3- Ver total de gastos \n4- Sair\n")
    if opcao == '1':
        print("Você escolheu cadastrar gasto!") 

        while True:
            data = (input("Digite a data: "))
            valor = float(input("Digite o valor gasto: "))
            descricao = input("Descreva o gasto: ")
            categoria = input("Digite a categoria do gasto: ")

            gasto = {
                "data": data,
                "valor": valor,
                "descrição": descricao,
                "categoria": categoria
            }

            gastos.append(gasto)
       
            resposta = input("Deseja adicionar outro gasto? (s/n): ")
            if resposta == 'n':
                break

    elif opcao == '2':
        print ("Você escolheu ver os gastos cadastrados!")
        for gasto in gastos:
            print(f"===== GASTO =====\nData: {gasto['data']} \nValor: R$ {gasto['valor']:.2f} \nDescrição: {gasto['descrição']} \nCategoria: {gasto['categoria']}\n")

    elif opcao == '3':
        print ("Você escolheu ver o total de gastos!")

        total = 0

        for gasto in gastos:
            total = total + gasto['valor']
        print (f"Total: R$ {total:.2f}")
    elif opcao == '4':
        print ("Você escolheu sair!")
        break