import os
import re
import pandas as pd


# Turmas esperadas
TURMAS = [
    "6A", "6B",
    "7A", "7B",
    "8A", "8B",
    "9A", "9B"
]


def descobrir_turma(nome_arquivo):
    """
    Descobre a turma pelo nome do arquivo.
    Exemplo:
        MAPAO_6A.xlsx -> 6A
        Mapão 7B.xls -> 7B
    """

    nome = nome_arquivo.upper()

    resultado = re.search(r'([6-9])\s*[º°]?\s*([AB])', nome)

    if resultado:
        return resultado.group(1) + resultado.group(2)

    return None


def ler_alunos_excel(caminho):
    """
    Lê um mapão procurando automaticamente a coluna ALUNO.
    """

    try:

        # Lê a planilha sem considerar cabeçalhos
        df = pd.read_excel(caminho, header=None)

        coluna_aluno = None
        linha_cabecalho = None

        # Procura a célula que contém "ALUNO"
        for i in range(len(df)):
            for j in range(len(df.columns)):

                valor = str(df.iat[i, j]).strip().upper()

                if valor == "ALUNO":
                    linha_cabecalho = i
                    coluna_aluno = j
                    break

            if coluna_aluno is not None:
                break

        if coluna_aluno is None:
            raise Exception("Não foi encontrada uma coluna chamada ALUNO.")

        # Releitura usando a linha correta como cabeçalho
        df = pd.read_excel(caminho, header=linha_cabecalho)

        alunos = (
            df.iloc[:, coluna_aluno]
            .dropna()
            .astype(str)
            .str.strip()
            .str.title()
            .tolist()
        )

        return alunos

    except Exception as erro:
        print(f"Erro lendo {os.path.basename(caminho)}")
        print(erro)
        return []


def carregar_mapoes(pasta="mapoes"):
    """
    Lê todos os mapões da pasta.

    Retorna:

    {
        "6A":[...],
        "6B":[...],
        ...
    }
    """

    dados = {}

    if not os.path.exists(pasta):
        raise FileNotFoundError(
            f"A pasta '{pasta}' não existe."
        )

    arquivos = sorted(os.listdir(pasta))

    for arquivo in arquivos:

        if not arquivo.lower().endswith((".xlsx", ".xls")):
            continue

        turma = descobrir_turma(arquivo)

        if turma is None:
            print(f"Ignorando {arquivo}")
            continue

        caminho = os.path.join(pasta, arquivo)

        alunos = ler_alunos_excel(caminho)

        dados[turma] = alunos

        print(f"{turma}: {len(alunos)} alunos")

    return dados


def montar_etiquetas(dados):
    """
    Converte os alunos para o formato utilizado
    pelo ReportLab.
    """

    quantidade = max(len(lista) for lista in dados.values())

    etiquetas = []

    for i in range(quantidade):

        alunos = {}

        for turma in TURMAS:

            lista = dados.get(turma, [])

            if i < len(lista):
                alunos[turma] = lista[i]
            else:
                alunos[turma] = ""

        etiquetas.append({

            "num": f"{i+1:02}",

            "tipo": f"COMP-{i+1:02}",

            "alunos": alunos

        })

    return etiquetas


def carregar_etiquetas(pasta="mapoes"):
    """
    Função principal.

    Basta chamar:

    etiquetas = carregar_etiquetas()

    """

    dados = carregar_mapoes(pasta)

    etiquetas = montar_etiquetas(dados)

    return etiquetas