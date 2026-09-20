import json

caminho = "modulo_06/repositorio"
arquivo = "pessoa.json"
origem = f"{caminho}/{arquivo}"

p1 = {"nome": "anna", "idade": 33, "cidade": "ilheus", "peso": 63.63}
p2 = {"nome": "anna", "idade": 33, "cidade": "ilheus", "peso": 63.63}
dados = [p1, p2]

with open(origem, "w") as arquivo_json:
    json.dump(dados, arquivo_json)

with open(origem, "r") as arquivo_json:
    print(json.load(arquivo_json))
