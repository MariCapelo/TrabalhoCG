def set_pixel_bloco(superficie, x, y, largura, altura, cor):
    largura_tela, altura_tela = superficie.get_size()
    for i in range(int(x), int(x + largura)):
        for j in range(int(y), int(y + altura)):
            if 0 <= i < largura_tela and 0 <= j < altura_tela:
                superficie.set_at((i, j), cor)

def desenhar_circulo_bloco(tela, cx, cy, raio, cor):
    largura_tela, altura_tela = tela.get_size()
    for x in range(int(cx - raio), int(cx + raio)):
        for y in range(int(cy - raio), int(cy + raio)):
            if 0 <= x < largura_tela and 0 <= y < altura_tela:
                dx = x - cx
                dy = y - cy
                if dx*dx + dy*dy <= raio*raio:
                    tela.set_at((x, y), cor)

def desenhar_onibus(tela, x, y, e):
    AMARELO = (255, 210, 0)
    AMARELO_ESC = (200, 160, 0)
    JANELA = (50, 130, 200)
    REFLEXO = (180, 220, 255)
    PNEU = (10, 10, 10)
    CALOTA = (150, 150, 150)
    PARA_CHOQUE = (30, 30, 30)
    FAROL = (255, 255, 200)
    LANTERNA = (220, 20, 20)
    PRETO = (0, 0, 0)

    set_pixel_bloco(tela, x - 75*e, y + 15*e, 155*e, 5*e, (25, 25, 25))

    set_pixel_bloco(tela, x - 80*e, y - 18*e, 160*e, 32*e, AMARELO)
    set_pixel_bloco(tela, x - 80*e, y - 20*e, 160*e, 4*e, AMARELO_ESC)

    set_pixel_bloco(tela, x + 58*e, y - 16*e, 18*e, 18*e, JANELA)
    set_pixel_bloco(tela, x + 68*e, y - 16*e, 5*e, 6*e, REFLEXO)

    largura_porta = 28 * e
    set_pixel_bloco(tela, x - (largura_porta/2), y - 16*e, largura_porta, 30*e, AMARELO_ESC)
    set_pixel_bloco(tela, x - 0.5*e, y - 16*e, 1*e, 30*e, PRETO)
    set_pixel_bloco(tela, x - 11*e, y - 14*e, 9*e, 12*e, JANELA)
    set_pixel_bloco(tela, x + 2*e, y - 14*e, 9*e, 12*e, JANELA)

    for i in range(3):
        jx = x - 72*e + (i * 17*e)
        set_pixel_bloco(tela, jx, y - 12*e, 14*e, 10*e, JANELA)
        set_pixel_bloco(tela, jx + 2*e, y - 12*e, 3*e, 3*e, REFLEXO)

    for i in range(2):
        jx = x + 18*e + (i * 18*e)
        set_pixel_bloco(tela, jx, y - 12*e, 15*e, 10*e, JANELA)
        set_pixel_bloco(tela, jx + 2*e, y - 12*e, 3*e, 3*e, REFLEXO)

    set_pixel_bloco(tela, x + 77*e, y + 8*e, 7*e, 7*e, PARA_CHOQUE)
    set_pixel_bloco(tela, x - 83*e, y + 8*e, 6*e, 7*e, PARA_CHOQUE)
    set_pixel_bloco(tela, x + 78*e, y + 0*e, 4*e, 6*e, FAROL)
    set_pixel_bloco(tela, x - 82*e, y + 0*e, 3*e, 6*e, LANTERNA)

    raio_pneu = 8 * e
    raio_calota = 4 * e
    desenhar_circulo_bloco(tela, x - 45*e, y + 15*e, raio_pneu, PNEU)
    desenhar_circulo_bloco(tela, x - 45*e, y + 15*e, raio_calota, CALOTA)
    desenhar_circulo_bloco(tela, x + 40*e, y + 15*e, raio_pneu, PNEU)
    desenhar_circulo_bloco(tela, x + 40*e, y + 15*e, raio_calota, CALOTA)

    