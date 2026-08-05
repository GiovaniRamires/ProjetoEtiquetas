# gerar_etiquetas.py

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from config import *
from leitor import carregar_etiquetas
from desenho import draw_label


def gerar_pdf():
    """
    Gera o PDF contendo todas as etiquetas.
    """

    print("=" * 50)
    print("GERADOR DE ETIQUETAS")
    print("=" * 50)

    # Lê os arquivos Excel
    etiquetas = carregar_etiquetas(PASTA_MAPOES)

    if len(etiquetas) == 0:
        print("Nenhuma etiqueta foi encontrada.")
        return

    print(f"\nTotal de computadores: {len(etiquetas)}")

    # Cria o PDF
    pdf = canvas.Canvas(
        ARQUIVO_SAIDA,
        pagesize=A4
    )

    for indice, etiqueta in enumerate(etiquetas):

        posicao = indice % ETIQUETAS_POR_PAGINA

        # Nova página
        if posicao == 0 and indice > 0:
            pdf.showPage()

        coluna = posicao % COLUNAS
        linha = posicao // COLUNAS

        x = (
            MARGEM_X
            + coluna * (LABEL_WIDTH + ESPACO_X)
        )

        y = (
            PH
            - MARGEM_Y
            - (linha + 1) * LABEL_HEIGHT
            - linha * ESPACO_Y
        )

        draw_label(
            pdf,
            x,
            y,
            etiqueta
        )

    pdf.save()

    print("\nPDF gerado com sucesso!")
    print(f"Arquivo: {ARQUIVO_SAIDA}")


def main():

    try:

        gerar_pdf()

    except FileNotFoundError as erro:

        print("\nERRO")
        print(erro)

    except PermissionError:

        print("\nNão foi possível salvar o PDF.")
        print("Feche o arquivo caso ele esteja aberto.")

    except Exception as erro:

        print("\nOcorreu um erro inesperado:")
        print(erro)


if __name__ == "__main__":
    main()