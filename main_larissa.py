import pygame
import sys
from bonequinha import desenhar_boneca
from transformacoes import (identidade, translacao, multiplica_matrizes, aplicar_transformacao)
from casa import desenhar_casa
from relogio import desenhar_modal, desenhar_relogio, desenhar_texto, desenhar_fundo_relogio
from renderizacao import setPixel

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
tempo_total = 60  
tempo_inicial = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tempo_atual = pygame.time.get_ticks()
    tempo_passado = (tempo_atual - tempo_inicial) // 1000
    tempo_restante = max(0, tempo_total - tempo_passado)
    game_over = tempo_restante == 0

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

    # a imagem verde duplicada aqui pra melhorar o tamanho da tela
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
    
    escala_relogio = 5

    largura = 5 * (escala_relogio * 4)
    altura = 5 * escala_relogio

    pos_x = LARGURA - largura - 20
    pos_y = 20

    desenhar_fundo_relogio(
        tela,
        pos_x - 5,
        pos_y - 5,
        largura + 10,
        altura + 10,
        (0, 0, 0)
    )

    for i in range(largura + 10):
        setPixel(tela, pos_x - 5 + i, pos_y - 5, (255,255,255))
        setPixel(tela, pos_x - 5 + i, pos_y + altura + 4, (255,255,255))

    for j in range(altura + 10):
        setPixel(tela, pos_x - 5, pos_y - 5 + j, (255,255,255))
        setPixel(tela, pos_x + largura + 4, pos_y - 5 + j, (255,255,255))

    desenhar_relogio(
        tela,
        tempo_restante,
        pos_x,
        pos_y,
        escala=escala_relogio,
        cor=(255,255,255)
    )    
    if game_over:
        desenhar_modal(
            tela, 300, 150, 400, 200, (255,255,255), (0,0,0)         
        )

        desenhar_texto(
            tela, "GAME OVER", 330, 220, escala=6, cor=(255,255,255)
        )

    pygame.display.flip()
    clock.tick(60)