def cadastrar_gasto():
    data = input("Digite a data: ")
    valor = float(input("Digite o valor gasto: "))

    while valor <= 0:
        print("Valor precisa ser maior que zero.")  
        valor = float(input("Digite novamente: "))

    descricao = input("Descreva o gasto: ")
    categoria = input("Digite a categoria do gasto: ")

    gasto = {
        "data": data,
        "valor": valor,
        "descrição": descricao,
        "categoria": categoria
    }

    return gasto

def mostrar_gastos(gastos):
    for gasto in gastos:    
        print(f"===== GASTO =====\nData: {gasto['data']} \nValor: R$ {gasto['valor']:.2f} \nDescrição: {gasto['descrição']} \nCategoria: {gasto['categoria']}\n")

def calcular_total(gastos):
    total = 0

    for gasto in gastos:
        total = total + gasto['valor']
    return total

def buscar_categoria(gastos, categoria):
    gastos_categoria = []

    for gasto in gastos:
        if gasto['categoria'] == categoria:
            gastos_categoria.append(gasto)

    return gastos_categoria

gastos = []

while True:
    opcao = input("Escolha uma opção: \n1- Cadastrar gasto \n2- Ver gastos cadastrados \n3- Ver total de gastos \n4- Buscar por categoria \n5- Sair \n ")

    if opcao == '1':

        while True:
            gasto = cadastrar_gasto()

            gastos.append(gasto)
            resposta = input("Deseja adicionar outro gasto? (s/n): ")
            if resposta == 'n':
                break

    elif opcao == '2':
        if not gastos:
            print("Nenhum gasto cadastrado.")
        else:
            mostrar_gastos(gastos)


    elif opcao == '3':
        if not gastos:
            print("Nenhum gasto cadastrado.")
        else:
            total = calcular_total(gastos)
            print(f"O total de gastos é: R$ {total:.2f}")

    elif opcao == '4': 
        if not gastos:
            print("Nenhum gasto cadastrado.")
        else:
            categoria = input("Digite a categoria para buscar: ")
            gastos_categoria = buscar_categoria(gastos, categoria)
            if not gastos_categoria:
                print("Nenhum gasto cadastrado nessa categoria.")
            else:
                mostrar_gastos(gastos_categoria)

    elif opcao == '5':
        print ("Você escolheu sair!")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 5.")
