import pygame
from render.renderizacao import desenhar_poligono, scanline, bresenham, setPixel
from ui.relogio import desenhar_pixel_grande

def pontos_textura_telhado(tela, pontos_telhado, textura_offset_x=0, textura_offset_y=0):
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
    COR_DIV =(142,46,1)
    #SOMBRA = (182, 88, 20)
    #SOMBRA = (174, 79, 19)
    SOMBRA2 = (142,46,1)
    LUZ = (201, 110, 22)
    LUZ2 = (204, 122, 42)
    LUZ3 = (201, 125, 54)
    COR_ENTRE = (196, 115, 41)
    # desenha linhas horizontais a cada 8 pixels, do topo até a base
    for i, y in enumerate(range(int(y_topo), int(y_base), 2)):

        # t indica o progresso: 0 = no topo, 1 = na base
        t = (y - y_topo) / (y_base - y_topo)

        # interpolação: calcula o X das bordas esquerda e direita nessa altura Y
        x_esq = int(x_topo + t * (x_base_esquerda - x_topo))
        x_dir = int(x_topo + t * (x_base_direita - x_topo))

        if i % 5 == 0:
            cor_linha = LUZ2
        elif i % 5 == 1:
            cor_linha = LUZ
        elif i % 5 == 2:
            cor_linha = COR_ENTRE
        elif i % 5 == 3:
            cor_linha = LUZ3
        else:
           cor_linha = SOMBRA2
    

        # desenha a linha horizontal dentro das bordas do triângulo
        for x in range(x_esq, x_dir, 2):
            desenhar_pixel_grande(tela, x, y, escala=3, cor=cor_linha)

            if i % 10 == 0:
                for dy in range(11):
                    setPixel(tela, x_esq + 52, y - dy, COR_DIV)
                    setPixel(tela, x_esq + 53, y - dy, COR_DIV)

                    setPixel(tela, x_dir - 40, y - dy, COR_DIV)
                    setPixel(tela, x_dir - 41, y - dy, COR_DIV)

            if i==19:
                for dy in range(11):
                    setPixel(tela, x_dir - 60, y - dy, COR_DIV)
                    setPixel(tela, x_dir - 61, y - dy, COR_DIV)
            if i%25==0:
                    for dy in range(11):
                        setPixel(tela, x_dir - 70, y - dy, COR_DIV)
                        setPixel(tela, x_dir - 71, y - dy, COR_DIV)
                    
            if i% 35==0:
                for dy in range(11):
                    setPixel(tela, x_dir - 50, y - dy, COR_DIV)
                    setPixel(tela, x_dir - 51, y - dy, COR_DIV)

                    setPixel(tela, x_esq + 80, y - dy, COR_DIV)
                    setPixel(tela, x_esq + 81, y - dy, COR_DIV)
            if i == 15:
                for dy in range(11):
                    setPixel(tela, x_esq + 39, y - dy, COR_DIV)
                    setPixel(tela, x_esq + 40, y - dy, COR_DIV)
            if i==39:
                for dy in range(11):
                    setPixel(tela, x_esq + 43, y - dy, COR_DIV)
                    setPixel(tela, x_esq + 44, y - dy, COR_DIV)

                    setPixel(tela, x_dir - 60, y - dy, COR_DIV)
                    setPixel(tela, x_dir - 61, y - dy, COR_DIV)

                    setPixel(tela, x_dir - 160, y - dy, COR_DIV)
                    setPixel(tela, x_dir - 161, y - dy, COR_DIV)

def textura_parede(tela,x,y,altura,largura,textura_offset_x=0,textura_offset_y=0):
    #RGB
    cor_ripa_escura =(201,117,131) 
    cor_ripa_clara = (219,132,146)
    cor_detalhes_ripa1 = (204,114,129)
    cor_ripa_escura_sombra = (179, 104, 111)
    cor_ripa_clara_sombra = (191, 117, 125)
    altura_sombra = 15
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
            if (xx * 3 + yy * 5) % 97 == 0:
                if yy + 4 < y + altura and xx + 4 < x + largura:
                    setPixel(tela, xx + 3, yy+1, cor_detalhes_ripa1)
                    setPixel(tela, xx + 4, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 2, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 3, yy+3, cor_detalhes_ripa1)
                    setPixel(tela, xx + 4, yy+4, cor_detalhes_ripa1)

            if (xx * 3 + yy *7 ) % 11 == 0:
                if yy + 3 < y + altura and xx + 5 < x + largura:
                    setPixel(tela, xx + 5, yy+1, cor_detalhes_ripa1)
                    setPixel(tela, xx + 5, yy+2, cor_detalhes_ripa1)
                    setPixel(tela, xx + 5, yy+3, cor_detalhes_ripa1)


def desenhar_casa(tela, base_x, base_y, textura_offset_x=None, textura_offset_y=None):

    # Quando o main nao passa offsets, calcula usando a ancora fixa da casa no mundo.
    if textura_offset_x is None or textura_offset_y is None:
        casa_mundo_x = 50
        casa_mundo_y = 100
        textura_offset_x = casa_mundo_x - base_x
        textura_offset_y = casa_mundo_y - base_y

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
    desenhar_poligono(tela, casa, (255,255,255))
    desenhar_poligono(tela, telhado, (255,255,255))

    scanline(tela, casa, (230, 140, 140))   
    scanline(tela, telhado, (160, 80, 0))   
    pontos_textura_telhado(tela, telhado, textura_offset_x, textura_offset_y)
    # PORTA
    porta = [
    (base_x+170, base_y+40),   
    (base_x+210, base_y+40),
    (base_x+210, base_y+120),
    (base_x+170, base_y+120)
]   
    
    textura_parede(tela, base_x, base_y, 120, 260, textura_offset_x, textura_offset_y)
    desenhar_poligono(tela, porta, (255,255,255))
    scanline(tela, porta, (120, 60, 0))
    pontos_textura_telhado(tela, telhado, textura_offset_x, textura_offset_y)
    # JANELINHA
    janela = [
    (base_x+30, base_y+30),
    (base_x+90, base_y+30),
    (base_x+90, base_y+70),
    (base_x+30, base_y+70)
]

    desenhar_poligono(tela, janela, (255,255,255))
    scanline(tela, janela, (240, 210, 150))

# cruzinha da janela 
# parte horizontal (meio)
    bresenham(
    tela,
    base_x+30, base_y+50,
    base_x+90, base_y+50,
    (255,255,255)
)
 

# parte vertical (meio)
    bresenham(
    tela,
    base_x+60, base_y+30,
    base_x+60, base_y+70,
    (255,255,255)
)