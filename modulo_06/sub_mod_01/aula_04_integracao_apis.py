import requests
import json

arquivo_destino = f"modulo_06/repositorio/api_IBGE_distritos_filtrados.json"
url_base = "https://servicodados.ibge.gov.br/api/v1"
endpoint = "localidades/distritos?orderBy=nome"
url_target = f"{url_base}/{endpoint}"
response = requests.get(url_target)
response_content = response.text
response_dict: list[dict] = json.loads(response_content)

filter_criteria = "São Paulo"
response_filtered = [
    match for match in response_dict if filter_criteria in match.get("nome")
]

print(f"response_filtered: ==> Count: {len(response_filtered)} | {response_filtered}")

if response_filtered:
    with open(
        arquivo_destino,
        "w",
        encoding="UTF-8",
    ) as repositorio_target:
        json.dump(response_filtered, repositorio_target, ensure_ascii=False)
