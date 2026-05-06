import pygame
import sys

from entidades.bonequinha import desenhar_boneca
from render.transformacoes import (identidade, translacao, multiplica_matrizes, aplicar_transformacao)
from entidades.casa import desenhar_casa
from ui.relogio import desenhar_hud
from ui.menu import desenhar_menu, desenhar_overlay_escuro
from ui.gameover import desenhar_tela_game_over
from ui.youwin import desenhar_tela_vitoria

pygame.init()

def criar_hitbox_boneca(x, y, escala):
    return pygame.Rect(int(x - 8 * escala), int(y - 18 * escala), int(16 * escala), int(25 * escala))


def colide_com_mapa(mascara_colisao, mascara_hitbox, hitbox, origem_x, origem_y):
    offset = (hitbox.left - origem_x, hitbox.top - origem_y)
    return mascara_colisao.overlap(mascara_hitbox, offset) is not None

# Configurações da tela
LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Configurações de mundo 
MAP_LARGURA, MAP_ALTURA = 1000, 2000

# Carregamento de sprites, colisões e criação de sombras
fundo = pygame.image.load('./sprites/fundo3.png').convert()
labirintoUp = pygame.image.load('./sprites/sprite-LabUp.png').convert_alpha()
LabirintoDown = pygame.image.load('./sprites/sprite-LabDown.png').convert_alpha()
mapa_colisao = pygame.image.load('./sprites/colisao_labirinto3.png').convert_alpha()

# Posição inicial da bonequinha esua escala de tamanho 
x_c, y_c = 240, 205
escala = 3
mascara_colisao = pygame.mask.from_surface(mapa_colisao)
mascara_hitbox_boneca = pygame.Mask((16 * escala, 25 * escala), fill=True)

# Posiçao inicial do labirinto
labUp_x = (MAP_LARGURA - labirintoUp.get_width()) // 2
labUp_y = (MAP_ALTURA - labirintoUp.get_height()) // 2
labdown_x = (MAP_LARGURA - LabirintoDown.get_width()) // 2
labdown_y = (MAP_ALTURA - LabirintoDown.get_height()) // 2

clock = pygame.time.Clock()

# Variaveis de animação e estado
status = {'passo': 0, 'piscando': False, 'olhar': 1, 'alternar': 0}
contador_anim = 0
timer_pisca = 0
alternar = 0 

# Tempo total do jogo em segundos
tempo_total = 70
tempo_inicial = pygame.time.get_ticks()
tempo_game_over = 0  
tempo_vitoria = 0

# Variaveis de Menu
estado = "menu"
opcao_menu = 0  

while True:
    # Loop controlador de eventos e lógica de jogo 
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
                        x_c, y_c = 240, 205
                    elif opcao_menu == 1:
                        pygame.quit()
                        sys.exit()

        if estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    estado = "menu"

    # Logica do Menu ---------------------------------------------------------------------------------------------
    if estado == "menu":
        tela.blit(pygame.transform.scale(fundo, (LARGURA, ALTURA)), (0, 0))
        desenhar_overlay_escuro(tela, LARGURA, ALTURA, intensidade=3)
        desenhar_menu(tela, LARGURA, ALTURA, opcao_menu)

    # Lógica do Jogo ---------------------------------------------------------------------------------------------
    elif estado == "jogo":

        # Cálculo do tempo restante e condições de vitória/derrota
        tempo_atual = pygame.time.get_ticks()
        tempo_passado = (tempo_atual - tempo_inicial) // 1000
        tempo_restante = max(0, tempo_total - tempo_passado)
        game_over = tempo_restante == 0

        # vitória baseada na posição no mapa - ajeitar
        vitoria = y_c >  MAP_ALTURA - 100  

        # Lógica para contorlar po movimento da menina baseado em teclas precionadas e Translação
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

        proximo_x, proximo_y = aplicar_transformacao(m, x_c, y_c)

        # Fazer a verificação se a menina nao vai colidir com um pixel de colisao do mapa 
        proximo_x = max(8 * escala, min(proximo_x, MAP_LARGURA - 8 * escala))
        proximo_y = max(18 * escala, min(proximo_y, MAP_ALTURA - 7 * escala))

        hitbox_proxima = criar_hitbox_boneca(proximo_x, proximo_y, escala)

        if not colide_com_mapa(mascara_colisao, mascara_hitbox_boneca, hitbox_proxima, labUp_x, labUp_y):
            x_c, y_c = proximo_x, proximo_y

        # Limitar a posição da bonequinha dentro dos limites do mapa
        x_c = max(8 * escala, min(x_c, MAP_LARGURA - 8 * escala))
        y_c = max(18 * escala, min(y_c, MAP_ALTURA - 7 * escala))

        # Cálculo da posição da câmera para centralizar na bonequinha
        camera_x = x_c - LARGURA // 2
        camera_y = y_c - ALTURA // 2

        camera_x = max(0, min(camera_x, MAP_LARGURA - LARGURA))
        camera_y = max(0, min(camera_y, MAP_ALTURA - ALTURA))

        # Lógica de animação da bonequinha, piscar e alternar passos
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

        # Desenhando fundo em toda a extenção do mapa usando a posição da câmera para criar um efeito de scroll
        for x in range(0, MAP_LARGURA, fundo.get_width()):
            for y in range(0, MAP_ALTURA, fundo.get_height()):
                tela.blit(fundo, (x - camera_x, y - camera_y))

        # Desenhando a casa
        desenhar_casa(tela, 50 - camera_x, 100 - camera_y)


        # Para criar o efeito de profundidade, o labirinto é dividido em duas partes:
        # a parte inferior (LabirintoDown) é desenhada antes da bonequinha, 
        # e a parte superior (labirintoUp) é desenhada depois.
        
        tela.blit(LabirintoDown, (labdown_x - camera_x, labdown_y - camera_y))
        desenhar_boneca(
            tela,
            x_c - camera_x,
            y_c - camera_y,
            escala,
            status
        )
        tela.blit(labirintoUp, (labUp_x - camera_x, labUp_y - camera_y))

        # Controlador do tempo restante e exibição da HUD
        desenhar_hud(tela, tempo_restante, LARGURA)

        # Condições de vitoria e derrota 
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