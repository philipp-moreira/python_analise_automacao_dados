conta_normal = False
conta_universitaria = False
conta_especial = True

cheque_especial = 450
limite_saque_conta_universitaria = 120

saldo = 1500
saque = float(input("Informe o valor da operação de saque: ").replace(",", "."))

if conta_normal:  # Exemplo de uso da estrutura condicional if, elif e else
    if (
        saque <= saldo
    ):  # Exemplo de uso da estrutura condicional if,  else, porém, aninhado dentro de outra estrutura if/else ou if/elif/else
        saldo -= saque
        print("Saque realizado com sucesso!")

    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:  # Exemplo de uso da estrutura condicional if, elif e else
    if (
        saque <= limite_saque_conta_universitaria
    ):  # Exemplo de uso da estrutura condicional if,  else, porém, aninhado dentro de outra estrutura if/else ou if/elif/else
        if (
            saque <= saldo
        ):  # Exemplo de uso da estrutura condicional if,  else, porém, aninhado dentro de outra estrutura if/else ou if/elif/else
            print("Saque realizado com sucesso!")

        else:
            print("Não foi possível realizar o saque, saldo insuficiente!")

    else:
        print("Valor de saque superior ao limite para conta do tipo  universitária!")

elif conta_especial:  # Exemplo de uso da estrutura condicional if, elif e else
    saldo_conta_mais_cheque_especial = saldo + cheque_especial

    # Exemplo de uso da estrutura condicional if ternario
    # Aqui devido ao tamanho da mensagem (valores de retorno) houve a transformação sintatica para tupla e atribuição deve estar ocorrento por desestruturação
    msg = (
        "Saque realizado com sucesso!"
        if saque <= saldo_conta_mais_cheque_especial
        else "Não foi possível realizar o saque, saldo insuficiente!"
    )

    if saque <= saldo_conta_mais_cheque_especial:
        print(msg)

    else:
        print(msg)

else:  # Exemplo de uso da estrutura condicional if, elif e else
    print("Tipo de conta não identificado ou não esperado!")
