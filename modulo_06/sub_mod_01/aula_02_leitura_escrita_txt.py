# Obtem o caracter de quebra de linha padrão  da camada do sistema
# operacional -  Se faz necessário, pois em ambiente Windows se utiliza como padrão [CRLF], Linux usa [LF], etc ...
from os import linesep

DELIMITADOR_ESCOPOS_IO_CONSOLE = str("*" * 50)
DELIMITADOR_ESCOPOS_IO_ESCRITA_CONTEUDO = str("|" * 50)


def escrevendo_arquivo_txt(caminho_origem, arquivos):
    print("Iniciando processamento | escrevendo_arquivo_txt()")
    for arquivo in arquivos:
        print(f"\tProcessando: {arquivo}")
        arquivo_em_processamento = f"{caminho_origem}/{arquivo}"
        with open(arquivo_em_processamento, "w") as destino:
            destino.write(f"Escrevendo um linha em '{arquivo}'")

        print(f"\tProcessado: {arquivo}")

    print("Terminado processamento | escrevendo_arquivo_txt()")


def adicionando_conteudo_arquivo_txt(caminho_origem, arquivos):
    print("Iniciando processamento | adicionando_conteudo_arquivo_txt()")
    caracter_quebra_linha = linesep
    for arquivo in arquivos:
        print(f"\tProcessando: {arquivo}")
        arquivo_em_processamento = f"{caminho_origem}/{arquivo}"
        # Comportamento padrão da opção "a" do parametro {mode} é apenas adicionar o conteúdo ao final  do arquivo
        # Caso seja necessario criar uma nova linha, a string/valor deve especificar o caracter de quebra de linha
        with open(arquivo_em_processamento, "a") as destino:
            destino.write(
                f"{caracter_quebra_linha}Adicionando novo conteudo ao arquivo '{arquivo}'"
            )
        print(f"\tProcessado: {arquivo}")

    print("Terminado processamento | adicionando_conteudo_arquivo_txt()")


def lendo_todo_conteudo_arquivo_txt(caminho_origem, arquivos):
    print("Iniciando  processamento | lendo_todo_conteudo_arquivo_txt()")
    for arquivo in arquivos:
        arquivo_em_processamento = f"{caminho_origem}/{arquivo}"
        print(f"\tLendo arquivo: '{arquivo}'")
        print(f"\tConteudo:")
        with open(arquivo_em_processamento, "r") as origem:
            conteudo = origem.read()
            print(DELIMITADOR_ESCOPOS_IO_ESCRITA_CONTEUDO)
            print(f"{conteudo}'")
            print(DELIMITADOR_ESCOPOS_IO_ESCRITA_CONTEUDO)
        print(f"\tLido arquivo: '{arquivo}'")
    print("Terminado processamento | lendo_todo_conteudo_arquivo_txt()")


def lendo_linha_a_linha_conteudo_arquivo_txt(caminho_origem, arquivos):
    print("Iniciando  processamento | lendo_linha_a_linha_conteudo_arquivo_txt()")
    for arquivo in arquivos:
        arquivo_em_processamento = f"{caminho_origem}/{arquivo}"
        print(f"\tLendo arquivo: '{arquivo}'")
        print(f"\tConteudo:")
        with open(arquivo_em_processamento, "r") as origem:
            print(DELIMITADOR_ESCOPOS_IO_ESCRITA_CONTEUDO)
            for linha in origem.readlines():
                conteudo = linha.strip()
                print(f"{conteudo}")
            print(DELIMITADOR_ESCOPOS_IO_ESCRITA_CONTEUDO)
        print(f"\tLido arquivo: '{arquivo}'")
    print("Terminado processamento | lendo_linha_a_linha_conteudo_arquivo_txt()")


caminho_origem = "/home/philipp/src/python/dio/bootcamp/accenture_analise_automacao_dados/modulo_06/repositorio"
arquivos = ["aula_02_leitura_escrita.txt"]

escrevendo_arquivo_txt(caminho_origem, arquivos)

print(f"\n{DELIMITADOR_ESCOPOS_IO_CONSOLE}")
adicionando_conteudo_arquivo_txt(caminho_origem, arquivos)

print(f"\n{DELIMITADOR_ESCOPOS_IO_CONSOLE}")
lendo_todo_conteudo_arquivo_txt(caminho_origem, arquivos)

print(f"\n{DELIMITADOR_ESCOPOS_IO_CONSOLE}")
lendo_linha_a_linha_conteudo_arquivo_txt(caminho_origem, arquivos)
