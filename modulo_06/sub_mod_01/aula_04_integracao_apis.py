import json
import logging
import logging.handlers
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import requests as rq
from requests import ReadTimeout


# Funcao para abstrair o controle de teste para avaliar cenário de erro durante execucao
def exec_erro_simulado():
    # e = rq.exceptions.InvalidURL()
    e = Exception(f"Erro '{Exception}' lançado de forma proposital")
    raise e


# CODIGO PRINCIPAL

caminho_base = "modulo_06/repositorio"
nome_arquivo_base = "api_IBGE_distritos_filtrados"
arquivo_log = f"{caminho_base}/{nome_arquivo_base}.log"
arquivo_destino = f"{caminho_base}/{nome_arquivo_base}.json"

lg = logging.getLogger(__name__)

tz = timezone.utc
dt = datetime.now(tz)
td = timedelta

# Personalizando o comportamento do modulo logging de acordo com o "ambiente" de execucao do codigo
env = str.lower(os.environ.get(key="Environment", default=""))
match env:
    case "local":
        # As constantes de nivel do modulo logging, permitem definir a partir de qual nivel sera registrado o log
        lg.setLevel(level=logging.DEBUG)
        # Definicao do formato do log a ser registrado no(s) destino(s) = de acordo com os handlers definidos
        # Ha a possibilidade de se definir um handler customizado, para definir o comportamento de como realizar registro em
        # um repositorio de banco de dados
        placeholders_formatter = [
            "%(asctime)s",
            "%(levelname)-8s",
            "%(environment)s",
            "%(lineno)d",
            "%(message)s",
        ]
        # junta a definicao do formato  do log
        log_formater = str.join("\t|", placeholders_formatter)
        fmt = logging.Formatter(log_formater)
        # Por padrao o Formatter dod logging usa o horario  local da maquina/host que estiver executando o codigo
        # Com a instrucao abaixo, estou especificando para que ele trabalha com fuso horario UTC
        fmt.converter = time.gmtime

        # definicao o(s) tipo(s) de  dentino(s) de registro do log
        hd_console = logging.StreamHandler(sys.stdout)
        hd_file = logging.handlers.TimedRotatingFileHandler(
            filename=arquivo_log,
            when="m",
            interval=1,
            backupCount=2,
            encoding="utf8",
            utc=True,
        )

        # Para cada tipo de destino ha a possibilidade de definir formatos de registro diferentes
        # Aqui estou usando o mesmo,  sendo que este formato tem sua espcificidade de acordo com o ambiente
        # mas nao varia de acrodo com o destino; Poderia variar
        hd_console.setFormatter(fmt)
        hd_file.setFormatter(fmt)

        # Efetivando quais os handlers o modulo logging deve usar para gravar o log
        lg.addHandler(hd_console)
        lg.addHandler(hd_file)

    case "dev":
        lg.setLevel(level=logging.DEBUG)
        placeholders_formatter = [
            "%(asctime)s",
            "%(levelname)-8s",
            "%(environment)s",
            "%(message)s",
        ]
        log_formater = "\t|".join(placeholders_formatter)
        fmt = logging.Formatter(log_formater)
        fmt.converter = time.gmtime
        hd_file = logging.handlers.RotatingFileHandler(
            filename=arquivo_log, backupCount=2, maxBytes=2_000_000, encoding="utf8"
        )
        hd_file.setFormatter(fmt)
        lg.addHandler(hd_file)

    case "qa":
        lg.setLevel(level=logging.INFO)
        placeholders_formatter = [
            "%(asctime)s",
            "%(levelname)-8s",
            "%(environment)s",
            "%(message)s",
        ]
        log_formater = "\t|".join(placeholders_formatter)
        fmt = logging.Formatter(log_formater)
        fmt.converter = time.gmtime
        fmt.default_time_format = "%Y-%m-%d %H:%M:%S%z %Z"
        hd_file = logging.handlers.RotatingFileHandler(
            filename=arquivo_log, backupCount=2, maxBytes=2_000_000, encoding="utf8"
        )
        hd_file.setFormatter(fmt)
        lg.addHandler(hd_file)

    case "prd":
        lg.setLevel(level=logging.ERROR)
        placeholders_formatter = [
            "%(asctime)s",
            "%(levelname)-8s",
            "%(environment)s",
            "%(message)s",
        ]
        log_formater = "\t|".join(placeholders_formatter)
        fmt = logging.Formatter(log_formater)
        fmt.converter = time.gmtime
        fmt.default_time_format = "%Y-%m-%d %H:%M:%S%z %Z"
        hd_file = logging.handlers.RotatingFileHandler(
            filename=arquivo_log, backupCount=2, maxBytes=2_000_000, encoding="utf8"
        )
        hd_file.setFormatter(fmt)
        lg.addHandler(hd_file)

    case _:
        # Se variavel de ambiente nao for esperada, vai ser aplicado  o comportamento padrao do ambiente local
        env = "local"
        lg.setLevel(level=logging.DEBUG)
        placeholders_formatter = [
            "%(asctime)s",
            "%(levelname)-8s",
            "%(environment)s",
            "%(message)s",
        ]
        log_formater = str.join("\t|", placeholders_formatter)
        fmt = logging.Formatter(log_formater)
        fmt.converter = time.gmtime
        hd_console = logging.StreamHandler(sys.stdout)
        hd_file = logging.handlers.TimedRotatingFileHandler(
            filename=arquivo_log,
            when="m",
            interval=1,
            backupCount=2,
            encoding="utf8",
            utc=True,
        )

        hd_console.setFormatter(fmt)
        hd_file.setFormatter(fmt)

        lg.addHandler(hd_console)
        lg.addHandler(hd_file)


tempo_inicio_execucao = dt.now(tz)
tempo_limite_execucao = tempo_inicio_execucao + timedelta(minutes=4)


lg.info(
    f"tempo_inicio_execucao =\tlocal: '{dt.now()}'\t|\tUTC: '{tempo_inicio_execucao}'",
    extra={"environment": env},
)

lg.info(
    f"tempo_limite_execucao =\tlocal: '{dt.now() + timedelta(minutes=4)}\t|\tUTC: '{tempo_limite_execucao}'",
    extra={"environment": env},
)

# uso do modulo request para requisicoes HTTP
api = rq
tempo_limite_requisicao = 1  # Segundos
response = None
url_base = "https://servicodados.ibge.gov.br/api/v1"
url_base_fake = "https://servicodados.ibge.gov.br/api1/v1"
endpoint = "localidades/distritos?orderBy=nome"
url_target = f"{url_base}/{endpoint}"

# Simulando um cenario de retry quando houve falha no que quero realmente fazer
# No bloco abaixo, tratei as possibilidades de erro, onde de acordo com o erro, continuo tentando, ate que o tempo limite seja atingido
# caso  o erro/exception seja de um tipo critico ou um totalmente nao esperado  pelo  codigo, encerro o loop,  imediatatmente
while dt.now(tz) < tempo_limite_execucao:
    try:
        # Bloco nao faz parte da logica principal, mas, permite simular um cenario para avaliacao do codigo
        if env == "local":
            lg.info("Aguardando...", extra={"environment": env})
            time.sleep(12)

        lg.info("Execução", extra={"environment": env})

        # Quando quero simular um erro,  descomento a linha abaixo e ajusto a funcao para o tipo de erro que quero avaliar
        # exec_erro_simulado()

        response = api.get(url_target, timeout=tempo_limite_requisicao)
        response_content = response.text
        response_dict: list[dict] = json.loads(response_content)

        filter_criteria = "São Paulo"
        response_filtered = [
            match for match in response_dict if filter_criteria in match.get("nome")
        ]

        lg.info(
            f"response_filtered: ==> Items: {len(response_filtered)}",
            extra={"environment": env},
        )

        if response_filtered:
            with open(
                arquivo_destino,
                "w",
                encoding="UTF-8",
            ) as repositorio_target:
                json.dump(response_filtered, repositorio_target, ensure_ascii=False)

            break

        else:
            lg.info("Execucao nao identicou nenhum retorno que possuia 'São Paulo'")
            break

    except rq.exceptions.InvalidURL as riu:
        msg_error = f"{type(riu)}\t|\t{riu}"
        lg.error(
            msg_error,
            extra={"environment": env},
        )
        sys.exit()

    except rq.exceptions.ReadTimeout as rto:
        msg_error = f"{rto}"
        lg.info(
            msg_error,
            extra={"environment": env},
        )

    except Exception as e:
        msg_error = f"{e}"
        lg.critical(
            msg_error,
            extra={"environment": env},
        )
        sys.exit()
