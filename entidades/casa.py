import pygame
from render.renderizacao import desenhar_poligono, scanline, bresenham

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