import pygame
import sys

from entidades.bonequinha import desenhar_boneca
from render.transformacoes import (
    identidade, translacao, multiplica_matrizes, aplicar_transformacao
)
from entidades.casa import desenhar_casa
from ui.relogio import desenhar_hud
from ui.menu import desenhar_menu, desenhar_overlay_escuro
from ui.gameover import desenhar_tela_game_over
from ui.youwin import desenhar_tela_vitoria

pygame.init()

LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

MAP_LARGURA, MAP_ALTURA = 1000, 2000

fundo = pygame.image.load('./assets/fundo3.png').convert()
labirinto = pygame.image.load('./assets/labirinto3.png').convert_alpha()

x_c, y_c = 240, 205
escala = 3

clock = pygame.time.Clock()

status = {'passo': 0, 'piscando': False, 'olhar': 1, 'alternar': 0}
contador_anim = 0
timer_pisca = 0
alternar = 0 

tempo_total = 20
tempo_inicial = pygame.time.get_ticks()
tempo_game_over = 0  
tempo_vitoria = 0

estado = "menu"
opcao_menu = 0  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if estado == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opcao_menu = (opcao_menu - 1) % 2
                if event.key == pygame.K_DOWN:
                    opcao_menu = (opcao_menu + 1) % 2
                if event.key == pygame.K_RETURN:
                    if opcao_menu == 0:
                        estado = "jogo"
                        tempo_inicial = pygame.time.get_ticks()
                    elif opcao_menu == 1:
                        pygame.quit()
                        sys.exit()

        if estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    estado = "menu"

    if estado == "menu":
        tela.blit(pygame.transform.scale(fundo, (LARGURA, ALTURA)), (0, 0))
        desenhar_overlay_escuro(tela, LARGURA, ALTURA, intensidade=3)
        desenhar_menu(tela, LARGURA, ALTURA, opcao_menu)

    elif estado == "jogo":

        tempo_atual = pygame.time.get_ticks()
        tempo_passado = (tempo_atual - tempo_inicial) // 1000
        tempo_restante = max(0, tempo_total - tempo_passado)
        game_over = tempo_restante == 0

        # vitória baseada na posição no mapa - ajeitar
        vitoria = y_c < 100  

        teclas = pygame.key.get_pressed()

        movendo = False
        m = identidade()

        if not game_over and not vitoria:

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

        x_c = max(0, min(x_c, MAP_LARGURA))
        y_c = max(0, min(y_c, MAP_ALTURA))

        camera_x = x_c - LARGURA // 2
        camera_y = y_c - ALTURA // 2

        camera_x = max(0, min(camera_x, MAP_LARGURA - LARGURA))
        camera_y = max(0, min(camera_y, MAP_ALTURA - ALTURA))

        if movendo:
            contador_anim += 1
            if contador_anim > 10:
                status['passo'] = 1
                status['alternar'] += 1
                contador_anim = 0
        else:
            status['passo'] = 0

        timer_pisca += 1
        if timer_pisca > 150:
            status['piscando'] = True
            if timer_pisca > 162:
                status['piscando'] = False
                timer_pisca = 0

        tela.fill((0, 0, 0))

        for x in range(0, MAP_LARGURA, fundo.get_width()):
            for y in range(0, MAP_ALTURA, fundo.get_height()):
                tela.blit(fundo, (x - camera_x, y - camera_y))

        desenhar_casa(tela, 50 - camera_x, 100 - camera_y)

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

        lab_x = (MAP_LARGURA - labirinto.get_width()) // 2
        lab_y = (MAP_ALTURA - labirinto.get_height()) // 2
        tela.blit(labirinto, (lab_x - camera_x, lab_y - camera_y))


        desenhar_hud(tela, tempo_restante, LARGURA)

        if vitoria:
            tempo_vitoria += 1
            desenhar_tela_vitoria(tela, LARGURA, ALTURA, tempo_vitoria)
        else:
            tempo_vitoria = 0

        if game_over and not vitoria:
            tempo_game_over += 1
            desenhar_tela_game_over(tela, LARGURA, ALTURA, tempo_game_over)
        else:
            tempo_game_over = 0

    pygame.display.flip()
    clock.tick(60)