import pygame
from render.renderizacao import desenhar_poligono, scanline, bresenhamsetPixel

#def textura_telhado_telha(tela,telhado):
    #RGB
    #aqui eu vou usar varios tons, pois fiz bem desenhado como imagino a telha
    

def textura_parede(tela,x,y,altura,largura):
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


def textura_janela(tela, x, y, largura, altura):
    #RGB
    cor_ripa_janela  = (156,90, 60)
    cor_borda_ripa_janela = (115, 38, 5)


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
    desenhar_poligono(tela, casa, (255,255,255))
    desenhar_poligono(tela, telhado, (255,255,255))

    scanline(tela, casa, (230, 140, 140))   
    scanline(tela, telhado, (160, 80, 0))   

    # PORTA
    porta = [
    (base_x+170, base_y+40),   
    (base_x+210, base_y+40),
    (base_x+210, base_y+120),
    (base_x+170, base_y+120)
]   
    
    textura_parede(tela, base_x, base_y, 120, 260)
    desenhar_poligono(tela, porta, (255,255,255))
    scanline(tela, porta, (120, 60, 0))     

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
