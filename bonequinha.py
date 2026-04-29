import pygame

def set_pixel_bloco(superficie, x, y, largura, altura, cor):
    largura_tela, altura_tela = superficie.get_size()
    for i in range(int(x), int(x + largura)):
        for j in range(int(y), int(y + altura)):
            if 0 <= i < largura_tela and 0 <= j < altura_tela:
                superficie.set_at((i, j), cor)

def desenhar_boneca(tela, x, y, e, cores, estado):
    """
    tela: tela no Pygame onde a boneca vai ficar
    x, y: Coordenadas na tela
    e: Tamanhoo das partes da boneca
    cores[cor]: Dicionário da cor
    """
    # ROSTO
    set_pixel_bloco(tela, x - 5*e, y - 14*e, 10*e, 8*e, cores['PELE'])
    set_pixel_bloco(tela, x - 5*e, y - 7*e, 10*e, 1*e, cores['PELE_SOMBRA'])
    set_pixel_bloco(tela, x - 5*e, y - 11*e, 1*e, 5*e, cores['PELE_SOMBRA'])
    set_pixel_bloco(tela, x + 4*e, y - 11*e, 1*e, 5*e, cores['PELE_SOMBRA'])

    # OLHOS (Piscar e Girando os Olhos)
    if estado['piscando']:
        set_pixel_bloco(tela, x - 3*e, y - 11*e, 2*e, 1*e, cores['PELE_SOMBRA'])
        set_pixel_bloco(tela, x + 1*e, y - 11*e, 2*e, 1*e, cores['PELE_SOMBRA'])
    else:
        # Olho Esquerdo
        set_pixel_bloco(tela, x - 3*e, y - 12*e, 2*e, 3*e, cores['BRANCO'])
        set_pixel_bloco(tela, x - 3*e + estado['olhar'], y - 11*e, 1*e, 1*e, cores['PRETO'])
        set_pixel_bloco(tela, x - 3*e + estado['olhar'], y - 10*e, 1*e, 1*e, cores['AZUL'])
        # Olho Direito
        set_pixel_bloco(tela, x + 1*e, y - 12*e, 2*e, 3*e, cores['BRANCO'])
        set_pixel_bloco(tela, x + 1*e + estado['olhar'], y - 11*e, 1*e, 1*e, cores['PRETO'])
        set_pixel_bloco(tela, x + 1*e + estado['olhar'], y - 10*e, 1*e, 1*e, cores['AZUL'])

    # CABELO E PESCOÇO
    set_pixel_bloco(tela, x - 1*e, y - 6*e, 2*e, 1*e, cores['PELE_SOMBRA'])
    set_pixel_bloco(tela, x - 8*e, y - 18*e, 6*e, 5*e, cores['LARANJA'])
    set_pixel_bloco(tela, x + 2*e, y - 18*e, 6*e, 5*e, cores['LARANJA'])
    set_pixel_bloco(tela, x - 4*e, y - 17*e, 8*e, 4*e, cores['LARANJA'])
    set_pixel_bloco(tela, x - 6*e, y - 17*e, 2*e, 8*e, cores['LARANJA'])
    set_pixel_bloco(tela, x + 4*e, y - 17*e, 2*e, 8*e, cores['LARANJA'])

    # CORPO (VESTIDO)
    set_pixel_bloco(tela, x - 4*e, y - 5*e, 8*e, 8*e, cores['ROSA'])
    set_pixel_bloco(tela, x - 2*e, y - 3*e, 4*e, 4*e, cores['ROSA_CLARO'])
    set_pixel_bloco(tela, x - 4*e, y + 3*e, 3*e, 2*e, cores['ROSA'])
    set_pixel_bloco(tela, x + 1*e, y + 3*e, 3*e, 2*e, cores['ROSA'])

    # PERNINHAS (Andando e tal) 
    if estado['passo'] == 0:
        set_pixel_bloco(tela, x - 4*e, y + 5*e, 3*e, 2*e, cores['PELE'])
        set_pixel_bloco(tela, x + 1*e, y + 5*e, 3*e, 2*e, cores['PELE'])
    else:
        set_pixel_bloco(tela, x - 4*e, y + 4*e, 3*e, 2*e, cores['PELE']) 
        set_pixel_bloco(tela, x + 1*e, y + 5*e, 3*e, 2*e, cores['PELE'])

    # BRACINHOS
    offset = (1*e) if estado['passo'] == 1 else 0
    set_pixel_bloco(tela, x - 5*e, y - 3*e + offset, 1*e, 5*e, cores['PELE'])
    set_pixel_bloco(tela, x + 4*e, y - 3*e - offset, 1*e, 5*e, cores['PELE'])
    set_pixel_bloco(tela, x - 6*e, y + 2*e + offset, 2*e, 2*e, cores['PELE'])
    set_pixel_bloco(tela, x + 4*e, y + 2*e - offset, 2*e, 2*e, cores['PELE'])