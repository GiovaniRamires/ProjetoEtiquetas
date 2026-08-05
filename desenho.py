# desenho.py

from reportlab.lib import colors
from config import *


# =============================================================================
# HELPERS
# =============================================================================

def nome_curto(nome):
    """
    Reduz nomes muito grandes.

    Exemplo:
    João Pedro da Silva Santos
    ↓
    João Pedro
    """

    if not nome:
        return ""

    partes = nome.strip().split()

    if len(partes) <= 2:
        return nome

    preposicoes = {
        "de",
        "da",
        "do",
        "dos",
        "das",
        "e"
    }

    resultado = [partes[0]]

    i = 1

    while i < len(partes):
        resultado.append(partes[i])

        if partes[i].lower() not in preposicoes:
            break

        i += 1

    return " ".join(resultado)


def tamanho_fonte(nome):
    """
    Diminui automaticamente a fonte
    conforme o tamanho do nome.
    """

    nome = nome_curto(nome)

    tamanho = len(nome)

    if tamanho <= 12:
        return 8.5

    if tamanho <= 18:
        return 8

    if tamanho <= 24:
        return 7.5

    if tamanho <= 30:
        return 7

    return 6.5


def rounded_fill(canvas, x, y, largura, altura, raio,
                 cor_fundo,
                 cor_borda=None,
                 largura_borda=0.5):

    canvas.setFillColor(cor_fundo)

    if cor_borda:

        canvas.setStrokeColor(cor_borda)
        canvas.setLineWidth(largura_borda)

        canvas.roundRect(
            x,
            y,
            largura,
            altura,
            raio,
            stroke=1,
            fill=1
        )

    else:

        canvas.roundRect(
            x,
            y,
            largura,
            altura,
            raio,
            stroke=0,
            fill=1
        )


def top_rounded(canvas, x, y, largura, altura, raio, cor):

    canvas.setFillColor(cor)

    canvas.roundRect(
        x,
        y,
        largura,
        altura,
        raio,
        stroke=0,
        fill=1
    )

    canvas.rect(
        x,
        y,
        largura,
        raio,
        stroke=0,
        fill=1
    )


# =============================================================================
# ETIQUETA
# =============================================================================

def draw_label(canvas, x, y, etiqueta):

    body_top = y + LABEL_HEIGHT - HEADER_HEIGHT
    body_height = body_top - y - 5

    # Fundo

    rounded_fill(
        canvas,
        x,
        y,
        LABEL_WIDTH,
        LABEL_HEIGHT,
        LABEL_RADIUS,
        colors.white,
        COR_BORDA,
        ESPESSURA_BORDA
    )

    # Cabeçalho

    top_rounded(
        canvas,
        x,
        y + LABEL_HEIGHT - HEADER_HEIGHT,
        LABEL_WIDTH,
        HEADER_HEIGHT,
        LABEL_RADIUS,
        COR_CABECALHO
    )

    # Número

    canvas.setFillColor(colors.white)

    canvas.setFont(
        FONT_TITULO,
        FONTE_NUMERO
    )

    canvas.drawString(
        x + PADDING,
        y + LABEL_HEIGHT - HEADER_HEIGHT + 5,
        etiqueta["num"]
    )

    # Escola

    canvas.setFont(
        FONT_TITULO,
        FONTE_ESCOLA
    )

    canvas.drawCentredString(
        x + LABEL_WIDTH / 2,
        y + LABEL_HEIGHT - HEADER_HEIGHT + 7.5,
        NOME_ESCOLA
    )

    # Computador

    canvas.setFont(
        FONT_TITULO,
        FONTE_COMP
    )

    canvas.drawRightString(
        x + LABEL_WIDTH - PADDING,
        y + LABEL_HEIGHT - 15,
        etiqueta["tipo"]
    )

    # ==========================================================
    # Badges
    # ==========================================================

    row_height = body_height / 4

    badge_width = (
        LABEL_WIDTH
        - (2 * PADDING)
        - BADGE_SPACING
    ) / 2

    series = [

        ("6", "6ºA", "6ºB", "6A", "6B"),

        ("7", "7ºA", "7ºB", "7A", "7B"),

        ("8", "8ºA", "8ºB", "8A", "8B"),

        ("9", "9ºA", "9ºB", "9A", "9B"),

    ]

    for linha, (serie, lbl_a, lbl_b, key_a, key_b) in enumerate(series):

        fundo, fonte = SERIES[serie]

        ry = body_top - (linha + 1) * row_height + 2

        badge_height = row_height - 4

        for coluna, (texto, chave) in enumerate(
                [(lbl_a, key_a), (lbl_b, key_b)]):

            bx = (
                x
                + PADDING
                + coluna * (badge_width + BADGE_SPACING)
            )

            nome = nome_curto(
                etiqueta["alunos"].get(chave, "")
            )

            rounded_fill(
                canvas,
                bx,
                ry,
                badge_width,
                badge_height,
                BADGE_RADIUS,
                fundo,
                COR_BADGE,
                ESPESSURA_BADGE
            )

            # Turma

            canvas.setFillColor(fonte)

            canvas.setFont(
                FONT_TITULO,
                FONTE_TURMA
            )

            canvas.drawCentredString(
                bx + badge_width / 2,
                ry + badge_height * 0.60,
                texto
            )

            # Nome

            canvas.setFont(
                FONT_NORMAL,
                tamanho_fonte(nome)
            )

            canvas.drawCentredString(
                bx + badge_width / 2,
                ry + badge_height * 0.18,
                nome
            )