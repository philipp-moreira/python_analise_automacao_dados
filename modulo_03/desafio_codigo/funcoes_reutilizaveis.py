# Encapsula/modulariza o desafio principal
def formatar_nome(nome):
    # Retorna o nome com a primeira letra de cada palavra em maiúsculo
    return " ".join(palavra.capitalize() for palavra in nome.strip().split())


def validar_email(email):
    # TODO: Verifique se o e-mail contém exatamente um '@' e pelo menos um '.' após o '@'
    # Dica: Use métodos de string para contar e dividir.
    if email.count("@") != 1:
        return False

    inicio_valor_dominio = email.index("@")
    dominio = email[inicio_valor_dominio:]

    if dominio.count(".") < 1:
        return False

    return True


def processar_cadastro(entrada):
    # Divide a entrada em nome e email
    if ", " not in entrada:
        return "Entrada inválida - ERRO"
    nome, email = entrada.split(", ", 1)
    nome_formatado = formatar_nome(nome)
    if validar_email(email):
        return f"{nome_formatado} - OK"
    else:
        return f"{nome_formatado} - ERRO"


def funcoes_reutilizaveis(input1):
    """
    3 / 3 - Funções Reutilizáveis Para Cadastro de Clientes em Python
    """
    # Entrada padrão
    # entrada = input()
    entrada = input1
    print(processar_cadastro(entrada))


# Encapsula/modulariza o mecanismo de teste da função  principal
def mock_test(funcao_to_test):

    # Leitura das listas de clientes de cada projeto
    mock_testes_aberto = [
        {"valor_linha1": "ana silva, ana.silva@email.com"},
        {"valor_linha1": "joao, joao@email"},
        {"valor_linha1": "maria clara, maria@email.com"},
        {"valor_linha1": "carlos, carlos@@email.com"},
    ]

    for index, teste in enumerate(mock_testes_aberto):
        input_linha_1 = teste.get("valor_linha1", "")

        print(
            f"Teste {index + 1}/{len(mock_testes_aberto)} : \n\t>>Saída/Retorno:\t",
            end="",
        )
        funcao_to_test(input_linha_1)


# Executa o teste efetivamente, chamando a função principal do desáfio
mock_test(funcoes_reutilizaveis)
