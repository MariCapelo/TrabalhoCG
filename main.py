import pygame
import sys

from entidades.bonequinha import desenhar_boneca
from render.transformacoes import (
    identidade, translacao, multiplica_matrizes, aplicar_transformacao
)
from entidades.casa import desenhar_casa_pixel
from ui.relogio import desenhar_hud
from ui.menu import desenhar_menu, desenhar_overlay_escuro
from ui.gameover import desenhar_tela_game_over
from entidades.onibus import desenhar_onibus_pixel
from render.renderizacao import setPixel

pygame.init()

LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

fundo = pygame.image.load('./assets/fundo3.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

x_c, y_c = 400, 300
escala = 4

clock = pygame.time.Clock()

status = {'passo': 0, 'piscando': False, 'olhar': 0}

contador_anim = 0
timer_pisca = 0
alternar = 0 

tempo_total = 20
tempo_inicial = pygame.time.get_ticks()
tempo_game_over = 0  # 👈 controle do fade

estado = "menu"
opcao_menu = 0  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ================= MENU INPUT =================
        if estado == "menu":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    opcao_menu = (opcao_menu - 1) % 2

                if event.key == pygame.K_DOWN:
                    opcao_menu = (opcao_menu + 1) % 2

                if event.key == pygame.K_RETURN:
                    if opcao_menu == 0:  # START
                        estado = "jogo"
                        tempo_inicial = pygame.time.get_ticks()
                    elif opcao_menu == 1:  # SAIR
                        pygame.quit()
                        sys.exit()

        # ================= GAME OVER INPUT =================
        if estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    estado = "menu"

    # ================= MENU =================
    if estado == "menu":

        tela.blit(fundo, (0, 0))

        desenhar_overlay_escuro(tela, LARGURA, ALTURA, intensidade=3)

        desenhar_menu(tela, LARGURA, ALTURA, opcao_menu)

    # ================= JOGO =================
    elif estado == "jogo":

        tempo_atual = pygame.time.get_ticks()
        tempo_passado = (tempo_atual - tempo_inicial) // 1000
        tempo_restante = max(0, tempo_total - tempo_passado)
        game_over = tempo_restante == 0

        teclas = pygame.key.get_pressed()

        movendo = False
        status['olhar'] = 0

        m = identidade()

        if not game_over:

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

        # animação
        if movendo:
            contador_anim += 1
            if contador_anim > 10:
                status['passo'] = 1
                alternar += 1
                contador_anim = 0
        else:
            status['passo'] = 0
            alternar = 0

        # piscar
        timer_pisca += 1
        if timer_pisca > 150:
            status['piscando'] = True
            if timer_pisca > 162:
                status['piscando'] = False
                timer_pisca = 0

        # fundo
        tela.blit(fundo, (0, 0))
      # desenhar_onibus_pixel(tela, 40, 30)
        desenhar_casa_pixel(tela, 20, 20)
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

        desenhar_hud(tela, tempo_restante, LARGURA)

        # ================= GAME OVER =================
        if game_over:
            tempo_game_over += 1
            desenhar_tela_game_over(tela, LARGURA, ALTURA, tempo_game_over)
        else:
            tempo_game_over = 0

    pygame.display.flip()
    clock.tick(60)