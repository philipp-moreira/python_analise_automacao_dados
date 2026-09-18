# Bloco do desafio
class Cliente:
    def __init__(self, nome: str, email: str, saldo: int):
        self.nome = nome
        self.email = email
        self.saldo = saldo

    def is_vip(self) -> bool:
        # TODO: Retorne True se o saldo for igual ou maior que 1000, senão False
        return self.saldo >= 1000


# # Entrada: nome, email e saldo do cliente (um por linha)
# nome = input()
# email = input()
# saldo = int(input())

# cliente = Cliente(nome, email, saldo)

# # Saída: imprima "VIP" se o cliente for VIP, senão "REGULAR"
# if cliente.is_vip():
#     print("VIP")
# else:
#     print("REGULAR")


# Encapsula/modulariza o mecanismo de teste da função  principal
def mock_test():

    # Leitura das listas de clientes de cada projeto
    mock_testes_aberto = [
        {
            "valor_linha1": "Lucas Silva",
            "valor_linha2": "lucas@techbiz.com",
            "valor_linha3": "1500",
        },
        {
            "valor_linha1": "Ana Costa",
            "valor_linha2": "ana@techbiz.com",
            "valor_linha3": "999",
        },
        {
            "valor_linha1": "Joao Pedro",
            "valor_linha2": "joao@techbiz.com",
            "valor_linha3": "1000",
        },
        {
            "valor_linha1": "Maria Lima",
            "valor_linha2": "maria@techbiz.com",
            "valor_linha3": "0",
        },
    ]

    for index, teste in enumerate(mock_testes_aberto):
        input_linha_1 = teste.get("valor_linha1", "")
        input_linha_2 = teste.get("valor_linha2", "")
        input_linha_3 = teste.get("valor_linha3", "")

        print(
            f"Teste {index + 1}/{len(mock_testes_aberto)} : \n\t>>Saída/Retorno:\t",
            end="",
        )
        nome = input_linha_1
        email = input_linha_2
        saldo = int(input_linha_3)

        cliente = Cliente(nome, email, saldo)

        if cliente.is_vip():
            print("VIP")
        else:
            print("REGULAR")


# Executa o teste efetivamente, chamando a função principal do desáfio
mock_test()
