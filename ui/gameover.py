from renderizacao import setPixel

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

    desenhar_texto(
        tela,
        "GAME OVER",
        330,
        220,
        escala=6,
        cor=(255,255,255)
    )
