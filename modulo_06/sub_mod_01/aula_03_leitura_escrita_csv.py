import csv

caminho = "./modulo_06/repositorio"
arquivo = "pessoas.csv"
origem_arquivo = f"{caminho}/{arquivo}"

list_cabecalho = ["nome", "idade", "cidade", "peso_aproximado"]
list_linha_dado_1 = ["john", 24, "san diego", "80,45"]
list_linha_dado_2 = ["Jeff", 36, "pequim", "55,67"]
list_linha_dado_3 = ["carl", 78, "green cable", ",98"]

dados = [
    list_cabecalho,
    list_linha_dado_1,
    list_linha_dado_2,
    list_linha_dado_3,
]

print("Iniciando escrita de arquivo csv")
# newLine =
# None -> Desativa tradução do carácter de quebra de linha, deixando a encargo
# a interpretação do caracter de quebra de linha, baseado no sistema operacional na camada
# na qual esta sendo executado o arquivo python
# ""|'' -> Desativa a tradução, seguindo o  comportamento padrão  de uso e interpretação do caractere '/n'
# independente do sistema operacional
with open(origem_arquivo, "w", newline=None) as arquivo_csv:
    print("Obtendo/Criando writter do mod csv")

    # Conforme padrão RFC 4180 o parametro  lineterminator tem como valor padrão o valor "\r\n"
    # ou seja, o caracter de quebra de linha padrão segue o comportamento de sistemas operacionais windows [CRLF]

    # O parametro delimiter permite definir o caracter delimitador de campos/colunas e seu valor padrão conforme
    # padrão  global é a ","
    # Em um cenário onde fosse necessario gerar arquivos com "especificações brasileiras", ou seja, números reais tendo
    # e usando separador fracionario a "," é possivel manter o comportamento padrão, onde o valores numericos/reais
    # serao  transcritos como strings,  ou seja, dentro de "" (aspas duplas), permitindo que a leitura do arquivo seja de forma
    # transparente, sem gerar problemas ou necessidade de acordos funcionais
    writter_csv = csv.writer(arquivo_csv)

    print("Registrando dados no arquivo csv")
    writter_csv.writerows(dados)

print("Terminado escrita de arquivo csv")

with open(origem_arquivo, "r") as arquivo_csv:
    print("lendo gravação")
    # o arquivo foi gerado  conforme padrão internacional,  onde a "última linha" não é uma linha em braco
    # Ao escrever no console o conteúdo e devido a "utlima linha" ser como esperado um caracter de quebra de linha "/n"
    # a função print() "renderiza"/escreve no console uma lnha em branco
    print(arquivo_csv.read())
    print("terminado leitura após gravação")
