# Encapsula/modulariza o desafio principal
def clientes_exclusivos(input1, input2):
    """
    1 / 3 - Clientes Exclusivos: Filtrando Dados Sem Duplicidade
    """

    # linha1 = input().strip()
    linha1 = input1.strip()

    # linha2 = input().strip()
    linha2 = input2.strip()

    # TODO: Converta cada linha em um conjunto de nomes, garantindo que listas vazias resultem em conjuntos vazios
    # Dica: Use split() para separar os nomes e set() para eliminar duplicatas

    clientes_projeto1 = set(linha1.split())
    clientes_projeto2 = set(linha2.split())

    # Identificação dos nomes exclusivos usando a operação de diferença simétrica
    exclusivos = clientes_projeto1.symmetric_difference(clientes_projeto2)

    # Impressão dos nomes exclusivos em ordem alfabética, ou "Nenhum" se não houver
    if exclusivos:
        print(" ".join(sorted(exclusivos)))
    else:
        print("Nenhum")


# Encapsula/modulariza o mecanismo de teste da função  principal
def mock_test(funcao_to_test):

    # Leitura das listas de clientes de cada projeto
    mock_testes_aberto = [
        {"valor_linha1": "ana bruno carla", "valor_linha2": "carla diego"},
        {"valor_linha1": "lucas maria", "valor_linha2": "lucas maria"},
        {"valor_linha1": "joao"},
        {"valor_linha1": "paula rafa"},
    ]

    for index, teste in enumerate(mock_testes_aberto):
        input_linha_1 = teste.get("valor_linha1", "")
        input_linha_2 = teste.get("valor_linha2", "")

        print(
            f"Teste {index + 1}/{len(mock_testes_aberto)} : \n\t>>Saída/Retorno:\t",
            end="",
        )
        funcao_to_test(input_linha_1, input_linha_2)


# Executa o teste efetivamente, chamando a função principal do desáfio
mock_test(clientes_exclusivos)
