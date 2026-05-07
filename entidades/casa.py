import pygame
from render.renderizacao import desenhar_poligono, scanline, bresenham, setPixel
from ui.relogio import desenhar_pixel_grande

def pontos_textura_telhado(tela, pontos_telhado):
    # encontra topo
    ponto_topo = pontos_telhado[0]
    for ponto in pontos_telhado:
        if ponto[1] < ponto_topo[1]:
            ponto_topo = ponto

    # encontra base esquerda/direita do triangulo (não topo)
    pontos_base = []
    for ponto in pontos_telhado:
        if ponto != ponto_topo:
            pontos_base.append(ponto)

    if len(pontos_base) < 2:
        return None, None, None

    ponto_base_esquerda = pontos_base[0]
    for ponto in pontos_base:
        if ponto[0] < ponto_base_esquerda[0]:
            ponto_base_esquerda = ponto

    ponto_base_direita = pontos_base[0]
    for ponto in pontos_base:
        if ponto[0] > ponto_base_direita[0]:
            ponto_base_direita = ponto

    x_topo, y_topo = ponto_topo
    x_base_esquerda, y_base_esquerda = ponto_base_esquerda
    x_base_direita, y_base_direita = ponto_base_direita

    # a base esquerda e direita estão na mesma altura Y
    y_base = y_base_esquerda

    # cores
    #COR_DIV =(142,46,1)
    #SOMBRA = (182, 88, 20)
    SOMBRA = (174, 79, 19)
    #SOMBRA2 = (142,46,1)
    LUZ = (201, 110, 22)
    LUZ2 = (204, 122, 42)
    LUZ3 = (201, 125, 54)
    COR_ENTRE = (196, 115, 41)

     # linhas horizontais do topo até a base
    for i, y in enumerate(range(int(y_topo), int(y_base), 2)):
        # t indica o progresso: 0 = topo, 1 = base
        t = (y - y_topo) / (y_base - y_topo)

        # X da borda esquerda e direita nesta altura y
        x_esq = int(x_topo + t * (x_base_esquerda - x_topo))
        x_dir = int(x_topo + t * (x_base_direita - x_topo))

        if x_esq > x_dir:
            x_esq, x_dir = x_dir, x_esq

        if i % 5 == 0:
            cor_linha = LUZ2
        elif i % 5 == 1:
            cor_linha = LUZ
        elif i % 5 == 2:
            cor_linha = COR_ENTRE
        elif i % 5 == 3:
            cor_linha = LUZ3
        else:
            cor_linha = SOMBRA

        # preenchimento da faixa horizontal com setPixel
        for x in range(x_esq, x_dir + 2):
            for dy in range(2):  # para dar uma "espessura" à linha
                setPixel(tela, x, y + dy, cor_linha)

def textura_parede(tela,x,y,altura,largura,textura_offset_x=None,textura_offset_y=None):
    if textura_offset_x is None or textura_offset_y is None:
        casa_mundo_x = 50
        casa_mundo_y = 100
        textura_offset_x = casa_mundo_x - x
        textura_offset_y = casa_mundo_y - y

    #RGB
    cor_ripa_escura =(201,117,131) 
    cor_ripa_clara = (219,132,146)
    cor_detalhes_ripa1 = (204,114,129)
    cor_ripa_escura_sombra = (179, 104, 111)
    cor_ripa_clara_sombra = (191, 117, 125)
    altura_sombra = 15

    for yy in range(y, y + altura_sombra):
        for xx in range(x, x + largura):
            setPixel(tela, xx, yy, cor_ripa_clara_sombra)

    #Esse for adiciona os detalhes nas ripas, alternado entre um tom mais claro e um mais escuro
    for xx in range (x, x+ largura, 8):
        for yy in range (y, y + altura):
            na_sombra = yy < y + altura_sombra

            if na_sombra:
                 c_clara = cor_ripa_clara_sombra
                 c_escura = cor_ripa_escura_sombra
            else:
                 c_clara = cor_ripa_clara
                 c_escura = cor_ripa_escura

            setPixel(tela, xx, yy, c_clara)
            setPixel(tela, xx + 1, yy, c_escura)
            setPixel(tela, xx + 2, yy, c_escura)
            setPixel(tela, xx + 3, yy, c_clara)


# Ja os ifs dentro do for foram adicionados para gerar um detalhe "natural" da madeira. Pode ser melhorado

            #
            detalhe_x = xx + textura_offset_x
            detalhe_y = yy + textura_offset_y

            if (detalhe_x * 3 + detalhe_y * 5) % 97 == 0:
                if yy + 4 < y + altura and xx + 4 < x + largura:
                    setPixel(tela, xx + 3, yy+1, cor_detalhes_ripa1)
                    setPixel(tela, xx + 4, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 2, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 3, yy+3, cor_detalhes_ripa1)
                    setPixel(tela, xx + 4, yy+4, cor_detalhes_ripa1)

            if (detalhe_x * 3 + detalhe_y *7 ) % 11 == 0:
                if yy + 3 < y + altura and xx + 5 < x + largura:
                    setPixel(tela, xx + 5, yy+1, cor_detalhes_ripa1)
                    setPixel(tela, xx + 5, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 5, yy+3, cor_detalhes_ripa1)


def textura_janela(tela, x, y, largura, altura):
    #RGB
    cor_ripa_janela  = (156,90, 60)
    cor_borda_ripa_janela = (115, 38, 5)
    cor_vidro = (200, 200, 255)
    cor_ponto_reflexo=(255, 255, 255)

    #quantos pixels cada parte da janela ocupa
    espessura_ripa = 4
     #preenche/pinta o vidro da janela de azul,mas deixa espaço para as ripas/moldura
    for yy in range(y+espessura_ripa, y + altura - espessura_ripa):
        for xx in range(x+espessura_ripa, x + largura - espessura_ripa):
            setPixel(tela, xx, yy, cor_vidro)

    # Ripa do meio (vertical e horizontal) - Dados usados para usar o bresenham
    # e desenhar a textura da ripa no meio 
    meio_esq = x + espessura_ripa #começa 5 pixels depois da borda esquerda
    meio_dir = x + largura - espessura_ripa - 1 #termina 5 pixels antes da borda direita
    meio_cima = y + espessura_ripa #começa 5 pixels abaixo da borda superior
    meio_base = y + altura - espessura_ripa - 1 #termina 5 pixels antes da borda inferior
    
    meio_x = (meio_esq + meio_dir) // 2  # meio_x é a posição X da ripa vertical do meio (centro)
    meio_y = (meio_cima + meio_base) // 2 # meio_y é a posição Y da ripa horizontal do meio (centro)

    # aumentei a largura da ripa para 4 pixels
    # pois quando coloquei menos ficou desproporcional
    for y_desloc in range(-1, 4):
        bresenham(tela, meio_esq, meio_y + y_desloc, meio_dir, meio_y + y_desloc, cor_ripa_janela)
        bresenham(tela, meio_x + y_desloc, meio_cima, meio_x + y_desloc, meio_base, cor_ripa_janela)
       

    
    #construção da moldura (bordas superior, inferior, esquerda, direita)
    for xx in range(x, x + largura):
        for dy in range(espessura_ripa):
            setPixel(tela, xx, y + dy, cor_ripa_janela)  # topo
            setPixel(tela, xx, y + altura - 1 - dy, cor_ripa_janela)  # baixo

    for yy in range(y, y + altura):
        for dx in range(espessura_ripa):
            setPixel(tela, x + dx, yy, cor_ripa_janela)  # esquerda
            setPixel(tela, x + largura - 1 - dx, yy, cor_ripa_janela)  # direita

# Aqui acrescentei a borda escura por fora da moldura
    for xx in range(x, x + largura):
        setPixel(tela, xx, y, cor_borda_ripa_janela)
        setPixel(tela, xx, y + altura - 1, cor_borda_ripa_janela)

    for yy in range(y, y + altura):
        setPixel(tela, x, yy, cor_borda_ripa_janela)
        setPixel(tela, x + largura - 1, yy, cor_borda_ripa_janela)

    # adicionei um 'reflexo' no canto superior esquerdo do vidro
    # que tem 4px de largura e 4px de altura, para ficar mais visível
    for dy in range(4):
        for dx in range(8):
            setPixel(tela, x + espessura_ripa + dx, y + espessura_ripa + dy, cor_ponto_reflexo)


def textura_porta(tela, x, y, largura, altura): 
    #RGB
    PORTA1 =(143, 66, 33)
    PORTA2 =(123, 58, 29)
    GUARNICAO = (113,56,28)
    MACANETA = (180, 180,180)


    espessura_moldura = 4
    largura_ripa = 5

    for xx in range(x, x + largura, largura_ripa):
        for yy in range(y, y + altura):
            deslocamento = xx - x

            if deslocamento % (largura_ripa * 2) == 0:
                cor_base = PORTA1
                cor_detalhe = PORTA2
            else:
                cor_base =PORTA2
                cor_detalhe = PORTA1

            for dx in range(largura_ripa):
                if xx + dx < x + largura:
                    cor_atual = cor_base if dx < largura_ripa - 2 else cor_detalhe
                    setPixel(tela, xx + dx, yy, cor_atual)

    for xx in range(x, x + largura):
        for dy in range(espessura_moldura):
            setPixel(tela, xx, y + dy, GUARNICAO)
            setPixel(tela, xx, y + altura - 1 - dy, GUARNICAO)

    for yy in range(y, y + altura):
        for dx in range(espessura_moldura):
            setPixel(tela, x + dx, yy, GUARNICAO)
            setPixel(tela, x + largura - 1 - dx, yy, GUARNICAO)

    for xx in range(x, x + largura):
        setPixel(tela, xx, y, GUARNICAO)

    for yy in range(y, y + altura):
        setPixel(tela, x, yy, GUARNICAO)

    macaneta_x = x + largura - 12
    macaneta_y = y + altura // 2
    for dy in range(-1, 3):
        for dx in range(-1, 3):
            setPixel(tela, macaneta_x + dx, macaneta_y + dy, MACANETA)

    for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
        setPixel(tela, macaneta_x + dx, macaneta_y + dy, GUARNICAO)

def desenhar_casa(tela, base_x, base_y):

    # PAREDES
    casa = [
        (base_x, base_y),
        (base_x+260, base_y),      
        (base_x+260, base_y+120),  
        (base_x, base_y+120)
]

    # TELHADO [VER PIXEL BEM AQUI]
    telhado = [
    (base_x-20, base_y),
    (base_x+280, base_y),      
    (base_x+130, base_y-80)    
]
    
    # bordas
    desenhar_poligono(tela, casa, (202,117,131))
    desenhar_poligono(tela, telhado, (121,34,0))

    scanline(tela, casa, (230, 140, 140))   
    scanline(tela, telhado, (160, 80, 0))   
    pontos_textura_telhado(tela, telhado)
    # PORTA
    porta = [
    (base_x+170, base_y+40),   
    (base_x+210, base_y+40),
    (base_x+210, base_y+120),
    (base_x+170, base_y+120)
]   
    
    textura_parede(tela, base_x, base_y, 120, 260)
    desenhar_poligono(tela, porta, (113,56,28))
    scanline(tela, porta, (120, 60, 0))
    textura_porta(tela, base_x+170, base_y+40, 40, 80)
    pontos_textura_telhado(tela, telhado)

    # JANELINHA
    janela = [
    (base_x+30, base_y+30),
    (base_x+90, base_y+30),
    (base_x+90, base_y+70),
    (base_x+30, base_y+70)
]

    desenhar_poligono(tela, janela, (115, 38, 5))
    scanline(tela, janela, (240, 210, 150))

# cruzinha da janela 
# parte horizontal (meio)
    bresenham(
    tela,
    base_x+30, base_y+50,
    base_x+90, base_y+50,
    (115, 38, 5)
)
 

# parte vertical (meio)
    bresenham(
    tela,
    base_x+60, base_y+30,
    base_x+60, base_y+70,
    (115, 38, 5)
)
    textura_janela(tela, base_x+30, base_y+30, 60, 40)