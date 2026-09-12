# Encapsula/modulariza o desafio principal
def busca_eficiente_livros(input1, *args, **kwargs):
    """
    2 / 3 - Busca Eficiente de Livros em Acervo Digital com Dicionários
    """

    # Leitura da quantidade de livros cadastrados
    # n = int(input())
    n = int(input1)

    # Dicionário para armazenar o acervo: título -> código
    acervo = {}

    # Leitura dos pares título-código
    for i in range(n):
        # linha = input().strip()
        linha = args[0][i].strip()

        # TODO: Separe o título e o código da linha e adicione ao dicionário 'acervo'
        # Dica: Use split() para separar e atribua corretamente no dicionário
        dados = linha.split()
        k, v = dados
        acervo.setdefault(k, v)

    # Leitura do título a ser consultado
    # consulta = input().strip()
    consulta = kwargs.get("termo_pesquisa", "").strip()

    # Busca pelo título no acervo e impressão do resultado
    if consulta in acervo:
        print(acervo[consulta])
    else:
        print("Livro nao encontrado")


# Encapsula/modulariza o mecanismo de teste da função  principal
def mock_test(funcao_to_test):

    # Leitura das listas de clientes de cada projeto
    mock_testes_aberto = [
        {
            "valor_linha1": "3",
            "valor_linha2": ["Python101 001", "Algoritmos 002", "Redes 003"],
            "valor_linha3": "Python101",
        },
        {
            "valor_linha1": "2",
            "valor_linha2": ["IntroJava 100", "Estruturas 200"],
            "valor_linha3": "Estruturas",
        },
        {
            "valor_linha1": "1",
            "valor_linha2": ["BancoDeDados 555"],
            "valor_linha3": "Redes",
        },
        {
            "valor_linha1": "2",
            "valor_linha2": ["LivroA 10", "LivroB 20"],
            "valor_linha3": "LivroC",
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
        funcao_to_test(input_linha_1, input_linha_2, termo_pesquisa=input_linha_3)


# Executa o teste efetivamente, chamando a função principal do desáfio
mock_test(busca_eficiente_livros)
