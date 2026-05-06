import pygame


def criar_sombra_labirinto(sprite):
    camadas = [
        (0, 8, 190),
        (0, 14, 210),
        (0, 20, 228),
    ]
    mascara = pygame.mask.from_surface(sprite)
    sombras = []

    for desloc_x, desloc_y, fator in camadas:
        camada = mascara.to_surface(
            setcolor=(fator, fator, fator, 255),
            unsetcolor=(255, 255, 255, 255)
        ).convert()
        sombras.append((camada, desloc_x, desloc_y))

    return sombras


def desenhar_sombra_labirinto(tela, sombras, x, y):
    for camada, desloc_x, desloc_y in sombras:
        tela.blit(camada, (x + desloc_x, y + desloc_y), special_flags=pygame.BLEND_RGB_MULT)