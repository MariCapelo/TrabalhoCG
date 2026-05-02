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

LETRAS = {
    'G': ["111","100","101","101","111"],
    'A': ["111","101","111","101","101"],
    'M': ["101","111","111","101","101"],
    'E': ["111","100","111","100","111"],
    'O': ["111","101","101","101","111"],
    'V': ["101","101","101","101","010"],
    'R': ["110","101","110","101","101"],
    ' ': ["000","000","000","000","000"]
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

def desenhar_texto(tela, texto, x, y, escala, cor):
    offset = 0

    for char in texto:
        matriz = LETRAS[char]

        for lin in range(len(matriz)):
            for col in range(len(matriz[lin])):
                if matriz[lin][col] == "1":
                    for i in range(escala):
                        for j in range(escala):
                            setPixel(
                                tela,
                                x + offset + col*escala + i,
                                y + lin*escala + j,
                                cor
                            )

        offset += escala * 4

def desenhar_modal_game_over(tela, x, y, largura, altura, cor_borda, cor_fundo):
    for i in range(largura):
        for j in range(altura):
            setPixel(tela, x + i, y + j, cor_fundo)

    for i in range(largura):
        setPixel(tela, x + i, y, cor_borda)
        setPixel(tela, x + i, y + altura - 1, cor_borda)

    for j in range(altura):
        setPixel(tela, x, y + j, cor_borda)
        setPixel(tela, x + largura - 1, y + j, cor_borda)