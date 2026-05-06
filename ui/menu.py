from render.renderizacao import setPixel
from ui.dicionario import desenhar_texto

def desenhar_overlay_escuro(tela, largura, altura, intensidade=3):
    for x in range(largura):
        for y in range(altura):
            if (x + y) % intensidade == 0:
                setPixel(tela, x, y, (0,0,0))

def desenhar_menu(tela, largura, altura, opcao_selecionada):
    desenhar_texto(tela, "THE LAST BUS", largura//2 - 195, 105, 7, (0,0,0))
    desenhar_texto(tela, "THE LAST BUS", largura//2 - 200, 100, 7, (255,255,255))
    cor_start = (255,255,255)
    cor_sair = (255,255,255)

    if opcao_selecionada == 0:
        cor_start = (255,0,0)
    else:
        cor_sair = (255,0,0)

    desenhar_texto(tela, "START", largura//2 - 80, 260, 6, cor_start)
    desenhar_texto(tela, "SAIR", largura//2 - 60, 330, 6, cor_sair)
    desenhar_texto(tela, "PRESS ENTER", largura//2 - 100,400,escala=3,cor=(200,200,200)
    )

    if opcao_selecionada == 0:
        desenhar_texto(tela, ">", largura//2 - 120, 260, 6, (255,255,255))
    else:
        desenhar_texto(tela, ">", largura//2 - 100, 330, 6, (255,255,255))

def desenhar_caixa(tela, x, y, largura, altura):
    for i in range(largura):
        for j in range(altura):
            if (i + j) % 2 == 0:  
                setPixel(tela, x + i, y + j, (50,50,50))