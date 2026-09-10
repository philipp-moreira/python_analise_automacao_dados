# Exemplo de uso do tipo de loop "for"
# Comummente usado em contextos, onde o limite de repetições é conhecido ou será informado

print("Mini Programa: Imprimindo lista de números")
numero = int(input("Informe um número inteiro: "))

for n in range(numero):
    print(f"{(n + 1)}", end=",  ")


# Exemplo de uso do tipo de loop "while"
# Comummente usado em contextos, onde o limite de repetições NÃO é conhecido

print("\nMini Programa: Imprimi próximo número ímpar")
continuar_executando = True  # True | False
limite_execucao = 5
contador_execucao = 0

while continuar_executando:
    if contador_execucao == limite_execucao:
        break  # Gera a saida do lado while, devolvendo a execução para o nivel superior do escopo de execução

    numero = int(
        input("\nInforme o  número para deseja obter o próximo número  ímpar: ")
    )

    numero_atual_ímpar = True if numero % 2 > 0 else False

    numero_atualizado = (numero + 2) if numero_atual_ímpar else (numero + 1)

    print(
        f"\t\tExecução # {contador_execucao + 1} | O próximo número ímpar é {numero_atualizado}"
    )

    contador_execucao += 1
else:  # Será executado somente se a condição do while não for atendida, ou seja, ele não for executado nenhuma vez
    print(
        "continuar_executando esta definida como False,  ocasionando não execução  da lógica."
    )
