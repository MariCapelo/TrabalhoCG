import pygame
from render.renderizacao import desenhar_poligono, scanline, circulo_preenchido
from ui.dicionario import desenhar_texto

_SPRITE_MENINA_CHORANDO = None


def obter_sprite_menina_chorando():
    global _SPRITE_MENINA_CHORANDO
    if _SPRITE_MENINA_CHORANDO is None:
        try:
            _SPRITE_MENINA_CHORANDO = pygame.image.load("./sprites/menina-chorando.png").convert_alpha()
        except pygame.error:
            _SPRITE_MENINA_CHORANDO = None
    return _SPRITE_MENINA_CHORANDO

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
    
    sprite_menina = obter_sprite_menina_chorando()
    if sprite_menina is not None:
        sprite_escala = pygame.transform.scale(sprite_menina, (230, 150))
        tela.blit(sprite_escala, (378, 50))

    centralizar_texto(tela, "GAME OVER!", altura//2 - 15, largura, 5, (130,29,218))
    centralizar_texto(tela, "PARECE QUE VOCE", altura//2 + 40, largura, 3, (255,80,80))
    centralizar_texto(tela, "VAI LEVAR FALTA HOJE", altura//2 + 70, largura, 3, (255,80,80))

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