import pygame
import sys
from bonequinha import desenhar_boneca
from transformacoes import (identidade, translacao, multiplica_matrizes, aplicar_transformacao)
from casa import desenhar_casa

pygame.init()

# Configurações de tela/veiwport
LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Configurações de mundo (mapa grande)
MAP_LARGURA, MAP_ALTURA = 1000, 2000

# Carregando imagem de fundo
fundo = pygame.image.load('./fundo3.png').convert()

# Posição inicial da menina no mundo e sua escala (saindo da casa)
x_c, y_c = 240, 205
escala = 3

# Variáveis de estado para animação
status = {'passo': 0, 'piscando': False, 'olhar': 1, 'alternar': 0}
contador_anim = 0
timer_pisca = 0

# Função para detectar coordenadas a parti do clique do mouse ao clicar na tela
def identificar_coordenadas_mapa():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:  # Verifica se o botão esquerdo do mouse foi clicado
        print(f"Coordenadas do clique: ({mouse_x}, {mouse_y})")
    

clock = pygame.time.Clock()

while True:
    identificar_coordenadas_mapa()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Aplicar transformações de movimento com base nas teclas pressionadas
    # Até linha 64 
    movendo = False
    m = identidade()

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        m = multiplica_matrizes(translacao(-3, 0), m)
        movendo = True
        status['olhar'] = -1

    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        m = multiplica_matrizes(translacao(3, 0), m)
        movendo = True
        status['olhar'] = 1

    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        m = multiplica_matrizes(translacao(0, -3), m)
        movendo = True

    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        m = multiplica_matrizes(translacao(0, 3), m)
        movendo = True

    x_c, y_c = aplicar_transformacao(m, x_c, y_c)
    
    # Limitar a posição da menina ao mapa
    x_c = max(0, min(x_c, MAP_LARGURA))
    y_c = max(0, min(y_c, MAP_ALTURA))
    
    # Cálculo da câmera (offset)
    camera_x = x_c - LARGURA // 2
    camera_y = y_c - ALTURA // 2

    # Evitar mostrar fora do mapa
    camera_x = max(0, min(camera_x, MAP_LARGURA - LARGURA))
    camera_y = max(0, min(camera_y, MAP_ALTURA - ALTURA))
    
    # Condição para alternar entre os passos da animação de caminhada
    if movendo:
        contador_anim += 1
        if contador_anim > 10:
            status['passo'] = 1
            status['alternar'] += 1
            contador_anim = 0
    else:
        status['passo'] = 0
        status['alternar'] = 0

    # Animação de piscar a cada 150 frames
    timer_pisca += 1
    if timer_pisca > 150:
        status['piscando'] = True
        if timer_pisca > 162:
            status['piscando'] = False
            timer_pisca = 0
    tela.fill((0, 0, 0))

    # Fundo do mundo: desenha em coordenadas de mapa e aplica offset da camera
    for x in range(0, MAP_LARGURA, fundo.get_width()):
        for y in range(0, MAP_ALTURA, fundo.get_height()):
            tela.blit(fundo, (x - camera_x, y - camera_y))


    desenhar_casa(tela)

    desenhar_boneca(
        tela,
        x_c - camera_x,
        y_c - camera_y,
        escala,
        {
            'BRANCO': (255,255,255),
            'PRETO': (0,0,0),
            'LARANJA': (255,120,0),
            'PELE': (214,193,140),
            'PELE_SOMBRA': (190,150,120),
            'ROSA': (190,0,150),
            'ROSA_CLARO': (220,0,180),
            'AZUL': (20,170,255),
            'FUNDO': (220,220,220)
        },
        status
    )

    pygame.display.flip()
    clock.tick(60)