from render.renderizacao import (
    circulo_preenchido,
    circulo,
    bresenham,
    desenhar_poligono,
    scanline,
)
from render.transformacoes import (
    translacao,
    rotacao,
    multiplica_matrizes,
    aplicar_transformacao,
)

ROSA = (255,230,234)
ROXO = (75,0,130)

def desenhar_retangulo_preenchido(tela, x1, y1, x2, y2, cor):
    pontos = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    desenhar_poligono(tela, pontos, cor)
    scanline(tela, pontos, cor)

def rotacionar_pontos_no_centro(pontos, centro, angulo):
    cx, cy = centro
    m = multiplica_matrizes(
        translacao(cx, cy),
        multiplica_matrizes(rotacao(angulo), translacao(-cx, -cy))
    )

    return [
        tuple(round(v) for v in aplicar_transformacao(m, x, y))
        for x, y in pontos
    ]

def desenhar_temporizador(tela, centro, raio, angulo_ponteiro=0.0):
    cx, cy = centro

    # Aro + fundo
    circulo_preenchido(tela, ROXO, centro, raio)
    circulo_preenchido(tela, ROSA, centro, raio - 6)
    circulo(tela, ROXO, centro, raio)
    circulo(tela, ROXO, centro, raio - 5)

    # Pino superior: um retangulo vertical conectado no relogio + um horizontal no topo
    largura_haste = max(4, raio // 8)
    altura_haste = max(10, raio // 4)
    x1_haste = cx - largura_haste // 2
    x2_haste = x1_haste + largura_haste
    y1_haste = cy - raio - altura_haste
    y2_haste = cy - raio + 2
    desenhar_retangulo_preenchido(tela, x1_haste, y1_haste, x2_haste, y2_haste, ROXO)

    largura_topo = max(10, raio // 3)
    altura_topo = max(3, raio // 10)
    x1_topo = cx - largura_topo // 2
    x2_topo = x1_topo + largura_topo
    y1_topo = y1_haste - altura_topo
    y2_topo = y1_haste
    desenhar_retangulo_preenchido(tela, x1_topo, y1_topo, x2_topo, y2_topo, ROXO)

    # Marcacoes de hora (12, 3, 6, 9)
    m_ext = raio - 10
    m_int = raio - 16
    bresenham(tela, cx, cy - m_int, cx, cy - m_ext, ROXO)
    bresenham(tela, cx + m_int, cy, cx + m_ext, cy, ROXO)
    bresenham(tela, cx, cy + m_int, cx, cy + m_ext, ROXO)
    bresenham(tela, cx - m_int, cy, cx - m_ext, cy, ROXO)

    # Ponteiro como retangulo vertical
    largura_ponteiro = max(3, raio // 14)
    y_topo_ponteiro = cy - (raio - 12)
    x1_ponteiro = cx - largura_ponteiro // 2 - 1
    x2_ponteiro = x1_ponteiro + largura_ponteiro - 1
    y1_ponteiro = y_topo_ponteiro
    y2_ponteiro = cy + 1
    pontos_ponteiro = [
        (x1_ponteiro, y1_ponteiro),
        (x2_ponteiro, y1_ponteiro),
        (x2_ponteiro, y2_ponteiro),
        (x1_ponteiro, y2_ponteiro),
    ]
    pontos_ponteiro = rotacionar_pontos_no_centro(pontos_ponteiro, centro, angulo_ponteiro)
    desenhar_poligono(tela, pontos_ponteiro, ROXO)
    scanline(tela, pontos_ponteiro, ROXO)

    # Pivo central
    circulo_preenchido(tela, ROXO, centro, max(3, raio // 10))
    