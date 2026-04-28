import pygame
import sys
from resumo import desenhar_boneca

pygame.init()
LARGURA, ALTURA = 700, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))

cores_paleta = {
    'BRANCO': (255, 255, 255), 'PRETO': (0, 0, 0), 'LARANJA': (255, 120, 0),
    'PELE': (214, 193, 140), 'PELE_SOMBRA': (190, 150, 120), 'ROSA': (190, 0, 150),
    'ROSA_CLARO': (220, 0, 180), 'AZUL': (20, 170, 255), 'FUNDO': (220, 220, 220)
}

x_c, y_c, escala = 350, 350, 8
clock = pygame.time.Clock()
contador_anim, timer_pisca = 0, 0

status = {'passo': 0, 'piscando': False, 'olhar': 0}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    movendo = False
    status['olhar'] = 0

    if teclas[pygame.K_LEFT]:  x_c -= 5; movendo = True; status['olhar'] = -1
    if teclas[pygame.K_RIGHT]: x_c += 5; movendo = True; status['olhar'] = 1
    if teclas[pygame.K_UP]:    y_c -= 5; movendo = True
    if teclas[pygame.K_DOWN]:  y_c += 5; movendo = True
    
    if teclas[pygame.K_p]: escala += 1
    if teclas[pygame.K_m] and escala > 2: escala -= 1

    if movendo:
        contador_anim += 1
        if contador_anim > 10:
            status['passo'] = 1 - status['passo']
            contador_anim = 0
    else: status['passo'] = 0

    timer_pisca += 1
    if timer_pisca > 150:
        status['piscando'] = True
        if timer_pisca > 162:
            status['piscando'] = False
            timer_pisca = 0

    tela.fill(cores_paleta['FUNDO'])
    
    desenhar_boneca(tela, x_c, y_c, escala, cores_paleta, status)
    
    pygame.display.flip()
    clock.tick(60)