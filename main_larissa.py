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

def colisao_boneca(x,y,escala):
    esquerda= int(x - 8 * escala)
    direita= int(x + 8 * escala)
    topo= int(y - 18 * escala)
    baixo= int(y + 7 * escala)
    return esquerda, direita, topo, baixo

def colisao_casa_retangulo(x,y):
    casa_esquerda = 50
    casa_direita = 310
    casa_topo = 100
    casa_baixo = 150
    return casa_esquerda <= x <= casa_direita and casa_topo <= y <= casa_baixo


def colisao_casa_triangulo(x,y):
   # telhado = [
    #(base_x-20, base_y) = (30,100)
    #(base_x+280, base_y),  = (330,100)    
    #(base_x+130, base_y-80)  = (180,20)

    xa, ya = 30, 100
    xb, yb = 330, 100
    xc, yc = 180, 20

    denominador = ((yb - yc) * (xa - xc) + (xc - xb) * (ya - yc))
    if denominador == 0:
        return False
    
    #P = a + b + c= 1
    a = ((yb - yc) * (x - xc) + (xc - xb) * (y - yc)) / denominador
    b = ((yc - ya) * (x - xc) + (xa - xc) * (y - yc)) / denominador
    c = 1 - a - b
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1



def colisao_casa(x,y,escala):
    esquerda, direita, topo, baixo = colisao_boneca(x,y,escala)
    pontos_de_colisao=[(esquerda, topo), (direita, topo), (esquerda, baixo), (direita, baixo)]

    for px,py in pontos_de_colisao:
        if colisao_casa_retangulo(px,py) or colisao_casa_triangulo(px,py):
            return True

    return False


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

#verificar se tem colisão antes de atualizar a posição da boneca
    novo_x, novo_y = aplicar_transformacao(m, x_c, y_c)
    if not colisao_casa(novo_x, novo_y, escala):
        x_c, y_c = novo_x, novo_y

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