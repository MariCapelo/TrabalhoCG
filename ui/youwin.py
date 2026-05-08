import pygame
from render.renderizacao import circulo_preenchido, desenhar_poligono, scanline
from ui.dicionario import desenhar_texto

def largura_texto(texto, escala):
    return len(texto) * escala * 4


def centralizar_texto(tela, texto, y, largura_tela, escala, cor):
    largura = largura_texto(texto, escala)
    x = (largura_tela - largura) // 2
    desenhar_texto(tela, texto, x, y, escala, cor)


def desenhar_tela_vitoria(tela, largura, altura, tempo_vitoria):

    alpha = min(180, tempo_vitoria * 3)

    overlay = pygame.Surface((largura, altura))
    overlay.set_alpha(alpha)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    if alpha < 80:
        return
    x = largura // 2 - 220
    y = altura // 2 - 120
    
    PONTOS_MODAL_DOWN = [(250, 25), (750,25), (750, 475), (250, 475)]
    PONTOS_MODAL_UP = [(270, 45), (730,45), (730, 455), (270, 455)]

    desenhar_poligono(tela, PONTOS_MODAL_DOWN, (130,29,218))
    scanline(tela, PONTOS_MODAL_DOWN, (130,29,218))
    desenhar_poligono(tela, PONTOS_MODAL_UP, (255,255,255))
    scanline(tela, PONTOS_MODAL_UP, (255,255,255))
    
    circulo_preenchido(tela, (130,29,218), (250, 25), 20)
    circulo_preenchido(tela, (130,29,218), (750, 25), 20)
    circulo_preenchido(tela, (130,29,218), (250, 475), 20)
    circulo_preenchido(tela, (130,29,218), (750, 475), 20)
    
    centralizar_texto(tela, ":)", altura//2 - 120, largura, 10, (130,29,218))
    
    centralizar_texto(tela, "PEGOU O ONIBUS!", altura//2 - 15, largura, 5, (130,29,218))
    centralizar_texto(tela, "NO FIM SUA", altura//2 + 40, largura, 3, (66,159,43))
    centralizar_texto(tela, "A CORRERIA VALEU APENA", altura//2 + 70, largura, 3, (66,159,43))

    piscar = (pygame.time.get_ticks() // 400) % 2

    if piscar == 0:
        centralizar_texto(
            tela,
            "PRESS R TO MENU",
            altura//2 + 150,
            largura,
            3,
            (70,70,70)
        )