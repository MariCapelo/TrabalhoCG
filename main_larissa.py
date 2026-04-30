import pygame
import sys
from bonequinha import desenhar_boneca
from transformacoes import (identidade, translacao, multiplica_matrizes, aplicar_transformacao)
from casa import desenhar_casa

pygame.init()

LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

fundo = pygame.image.load('./fundo3.png').convert()

x_c, y_c = 400, 300
escala = 4

clock = pygame.time.Clock()

status = {'passo': 0, 'piscando': False, 'olhar': 0}

contador_anim = 0
timer_pisca = 0
alternar = 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    movendo = False
    status['olhar'] = 0

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

    if movendo:
        contador_anim += 1
        if contador_anim > 10:
            status['passo'] = 1
            alternar += 1
            contador_anim = 0
    else:
        status['passo'] = 0
        alternar = 0

    timer_pisca += 1
    if timer_pisca > 150:
        status['piscando'] = True
        if timer_pisca > 162:
            status['piscando'] = False
            timer_pisca = 0
    tela.fill((0, 0, 0))

    # a imagem verde duplicada aqui
    for x in range(0, LARGURA, fundo.get_width()):
        for y in range(0, ALTURA, fundo.get_height()):
            tela.blit(fundo, (x, y))

    desenhar_casa(tela)

    desenhar_boneca(
        tela,
        x_c,
        y_c,
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
        status,
        alternar
    )

    pygame.display.flip()
    clock.tick(60)