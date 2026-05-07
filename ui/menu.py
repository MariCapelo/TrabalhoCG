from render.renderizacao import setPixel, desenhar_poligono, scanline
from ui.dicionario import desenhar_texto

CAIXINHA1_PONTOS = [(375, 250), (625, 250), (625, 300), (375, 300)]
CAIXINHA2_PONTOS = [(375, 350), (625, 350), (625, 400), (375, 400)]

CAIXINHA_SOMBRA1_PONTOS = [(370, 245), (630, 245), (630, 315), (370, 315)]
CAIXINHA_SOMBRA2_PONTOS = [(370, 345), (630, 345), (630, 415), (370, 415)]


def desenhar_overlay_escuro(tela, largura, altura, intensidade=3):
    for x in range(largura):
        for y in range(altura):
            if (x + y) % intensidade == 0:
                setPixel(tela, x, y, (0,0,0))

def desenhar_menu(tela, largura, altura, opcao_selecionada):
    desenhar_texto(tela, "PEGUE O ONIBUS", largura//2 - 285, 105, 10, (75,0,130))
    desenhar_texto(tela, "PEGUE O ONIBUS", largura//2 - 280, 100, 10, (255,105,180))
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

    desenhar_poligono(tela, CAIXINHA_SOMBRA1_PONTOS, (75,0,130))
    scanline(tela, CAIXINHA_SOMBRA1_PONTOS, (75,0,130))
    desenhar_poligono(tela, CAIXINHA1_PONTOS, cor_start_caixa)
    scanline(tela, CAIXINHA1_PONTOS, cor_start_caixa)
    desenhar_poligono(tela, CAIXINHA_SOMBRA2_PONTOS, (75,0,130))
    scanline(tela, CAIXINHA_SOMBRA2_PONTOS, (75,0,130))
    desenhar_poligono(tela, CAIXINHA2_PONTOS, cor_sair_caixa)
    scanline(tela, CAIXINHA2_PONTOS, cor_sair_caixa)

    desenhar_texto(tela, "START", largura//2 - 60, 260, 6, cor_start_palavra)
    desenhar_texto(tela, "SAIR", largura//2 - 50, 360, 6, cor_sair_palavra)


  
    desenhar_texto(tela, "APERTE ENTER", largura//2 - 100,450,escala=4,cor=(220,220,220))
    