from renderizacao import setPixel

DIGITOS = {
    '0': ["111","101","101","101","111"],
    '1': ["010","110","010","010","111"],
    '2': ["111","001","111","100","111"],
    '3': ["111","001","111","001","111"],
    '4': ["101","101","111","001","001"],
    '5': ["111","100","111","001","111"],
    '6': ["111","100","111","101","111"],
    '7': ["111","001","010","010","010"],
    '8': ["111","101","111","101","111"],
    '9': ["111","101","111","001","111"],
    ':': ["0","1","0","1","0"]
}

def desenhar_pixel_grande(tela, x, y, escala, cor):
    for i in range(escala):
        for j in range(escala):
            setPixel(tela, x + i, y + j, cor)

def desenhar_digito(tela, digito, x, y, escala, cor):
    matriz = DIGITOS[digito]

    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            if matriz[lin][col] == "1":
                desenhar_pixel_grande(
                    tela,
                    x + col * escala,
                    y + lin * escala,
                    escala,
                    cor
                )

def desenhar_relogio(tela, tempo_restante, x, y, escala=5, cor=(255,255,255)):
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60

    texto = f"{minutos:02}:{segundos:02}"

    offset = 0
    for char in texto:
        desenhar_digito(tela, char, x + offset, y, escala, cor)

        if char == ":":
            offset += escala * 2
        else:
            offset += escala * 4

def desenhar_fundo_relogio(tela, x, y, largura, altura, cor):
    for i in range(largura):
        for j in range(altura):
            setPixel(tela, x + i, y + j, cor)

def desenhar_hud(tela, tempo_restante, largura_tela):
    escala = 5

    largura = 5 * (escala * 4)
    altura = 5 * escala

    pos_x = largura_tela - largura - 20
    pos_y = 20

    desenhar_fundo_relogio(
        tela,
        pos_x - 5,
        pos_y - 5,
        largura + 10,
        altura + 10,
        (0,0,0)
    )

    # borda
    for i in range(largura + 10):
        setPixel(tela, pos_x - 5 + i, pos_y - 5, (255,255,255))
        setPixel(tela, pos_x - 5 + i, pos_y + altura + 4, (255,255,255))

    for j in range(altura + 10):
        setPixel(tela, pos_x - 5, pos_y - 5 + j, (255,255,255))
        setPixel(tela, pos_x + largura + 4, pos_y - 5 + j, (255,255,255))

    desenhar_relogio(tela, tempo_restante, pos_x, pos_y, escala)