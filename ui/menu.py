import math
import pygame
from render.renderizacao import setPixel, desenhar_poligono, scanline
from ui.dicionario import desenhar_texto
from render.transformacoes import (
    translacao,
    escala as escala_matriz,
    multiplica_matrizes,
    aplicar_transformacao,
)
from entidades.temporizador import desenhar_temporizador

CAIXINHA1_PONTOS = [(375, 250), (625, 250), (625, 300), (375, 300)]
CAIXINHA2_PONTOS = [(375, 350), (625, 350), (625, 400), (375, 400)]

CAIXINHA_SOMBRA1_PONTOS = [(370, 245), (630, 245), (630, 315), (370, 315)]
CAIXINHA_SOMBRA2_PONTOS = [(370, 345), (630, 345), (630, 415), (370, 415)]


def escalar_poligono_no_centro(pontos, sx, sy):
    cx = sum(x for x, _ in pontos) / len(pontos)
    cy = sum(y for _, y in pontos) / len(pontos)

    m = multiplica_matrizes(
        translacao(cx, cy),
        multiplica_matrizes(escala_matriz(sx, sy), translacao(-cx, -cy))
    )

    return [
        tuple(round(valor) for valor in aplicar_transformacao(m, x, y))
        for x, y in pontos
    ]


def desenhar_overlay_escuro(tela, largura, altura, intensidade=3):
    for x in range(largura):
        for y in range(altura):
            if (x + y) % intensidade == 0:
                setPixel(tela, x, y, (0,0,0))

def desenhar_menu(tela, largura, altura, opcao_selecionada):
    desenhar_texto(tela, "PEGUE O ONIBUS", largura//2 - 285, 105, 10, (75,0,130))
    desenhar_texto(tela, "PEGUE O ONIBUS", largura//2 - 280, 100, 10, (255,105,180))
    tempo_segundos = pygame.time.get_ticks() / 1000.0
    voltas_por_segundo = 1 / 12
    angulo_ponteiro = 2 * math.pi * voltas_por_segundo * tempo_segundos
    desenhar_temporizador(tela, (largura//2 + 330, 132), 40, angulo_ponteiro)
    cor_start_palavra= (75,0,130)
    cor_start_caixa = (255,255,255)
    cor_sair_palavra = (75,0,130)
    cor_sair_caixa = (255,255,255)

    if opcao_selecionada == 0:
        cor_start_palavra = (255,255,255)
        cor_start_caixa = (255,105,180)
    else:
        cor_sair_palavra = (255,255,255)
        cor_sair_caixa = (255,105,180)

    escala_selecionado = 1.15

    pontos_start = CAIXINHA1_PONTOS
    pontos_sombra_start = CAIXINHA_SOMBRA1_PONTOS
    pontos_sair = CAIXINHA2_PONTOS
    pontos_sombra_sair = CAIXINHA_SOMBRA2_PONTOS

    if opcao_selecionada == 0:
        pontos_start = escalar_poligono_no_centro(CAIXINHA1_PONTOS, escala_selecionado, escala_selecionado)
        pontos_sombra_start = escalar_poligono_no_centro(CAIXINHA_SOMBRA1_PONTOS, escala_selecionado, escala_selecionado)
    else:
        pontos_sair = escalar_poligono_no_centro(CAIXINHA2_PONTOS, escala_selecionado, escala_selecionado)
        pontos_sombra_sair = escalar_poligono_no_centro(CAIXINHA_SOMBRA2_PONTOS, escala_selecionado, escala_selecionado)


    desenhar_poligono(tela, pontos_sombra_start, (75,0,130))
    scanline(tela, pontos_sombra_start, (75,0,130))
    desenhar_poligono(tela, pontos_start, cor_start_caixa)
    scanline(tela, pontos_start, cor_start_caixa)
    desenhar_poligono(tela, pontos_sombra_sair, (75,0,130))
    scanline(tela, pontos_sombra_sair, (75,0,130))
    desenhar_poligono(tela, pontos_sair, cor_sair_caixa)
    scanline(tela, pontos_sair, cor_sair_caixa)

    escala_start = 7 if opcao_selecionada == 0 else 6
    escala_sair = 7 if opcao_selecionada == 1 else 6

    centro_start_x = sum(x for x, _ in pontos_start) / len(pontos_start)
    centro_start_y = sum(y for _, y in pontos_start) / len(pontos_start)
    centro_sair_x = sum(x for x, _ in pontos_sair) / len(pontos_sair)
    centro_sair_y = sum(y for _, y in pontos_sair) / len(pontos_sair)

    largura_start = len("START") * 4 * escala_start
    altura_start = 5 * escala_start
    largura_sair = len("SAIR") * 4 * escala_sair
    altura_sair = 5 * escala_sair

    desenhar_texto(
        tela,
        "START",
        int(centro_start_x - largura_start / 2),
        int(centro_start_y - altura_start / 2),
        escala_start,
        cor_start_palavra,
    )
    desenhar_texto(
        tela,
        "SAIR",
        int(centro_sair_x - largura_sair / 2),
        int(centro_sair_y - altura_sair / 2),
        escala_sair,
        cor_sair_palavra,
    )


  
    desenhar_texto(tela, "APERTE ENTER", largura//2 - 100,450,escala=4,cor=(220,220,220))
    