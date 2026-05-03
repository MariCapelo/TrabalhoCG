from ui.dicionario import desenhar_texto
from render.renderizacao import setPixel

def desenhar_modal(tela, x, y, largura, altura, cor_borda, cor_fundo):
    for i in range(largura):
        for j in range(altura):
            setPixel(tela, x + i, y + j, cor_fundo)

    for i in range(largura):
        setPixel(tela, x + i, y, cor_borda)
        setPixel(tela, x + i, y + altura - 1, cor_borda)

    for j in range(altura):
        setPixel(tela, x, y + j, cor_borda)
        setPixel(tela, x + largura - 1, y + j, cor_borda)

def desenhar_tela_game_over(tela):
    desenhar_modal(tela, 300, 150, 400, 200, (255,255,255), (0,0,0))

    desenhar_texto(tela, "GAME OVER", 330, 220, escala=6,cor=(255,255,255))
