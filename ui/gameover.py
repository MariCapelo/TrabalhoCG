import pygame
from render.renderizacao import setPixel
from ui.dicionario import desenhar_texto

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

def largura_texto(texto, escala):
    return len(texto) * escala * 4

def centralizar_texto(tela, texto, y, largura_tela, escala, cor):
    largura = largura_texto(texto, escala)
    x = (largura_tela - largura) // 2

    desenhar_texto(tela, texto, x, y, escala, cor)

def desenhar_tela_game_over(tela, largura, altura, tempo_game_over):

    alpha = min(180, tempo_game_over * 3)

    overlay = pygame.Surface((largura, altura))
    overlay.set_alpha(alpha)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    if alpha < 80:
        return
    x = largura // 2 - 220
    y = altura // 2 - 120

    desenhar_modal(tela, x+6, y+6, 440, 240, (0,0,0), (0,0,0))
    desenhar_modal(tela, x, y, 440, 240, (255,255,255), (20,20,20))

    centralizar_texto(tela, "GAME OVER", altura//2 - 80, largura, 6, (255,255,255))
    centralizar_texto(tela, "YOU MISSED", altura//2 - 10, largura, 4, (255,80,80))
    centralizar_texto(tela, "THE BUS", altura//2 + 40, largura, 5, (255,80,80))

    piscar = (pygame.time.get_ticks() // 400) % 2

    if piscar == 0:
        centralizar_texto(
            tela,
            "PRESS R TO MENU",
            altura//2 + 100,
            largura,
            3,
            (200,200,200)
        )