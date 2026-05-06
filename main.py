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
from entidades.onibus import desenhar_onibus 

pygame.init()

# ================= CONFIG =================
LARGURA, ALTURA = 1000, 500
MAP_LARGURA, MAP_ALTURA = 1000, 2000

tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

fundo = pygame.image.load('./assets/fundo3.png').convert()
labirinto = pygame.image.load('./assets/labirinto3.png').convert_alpha()

def get_posicao_onibus():
    lab_x = (MAP_LARGURA - labirinto.get_width()) // 2
    lab_y = 300

    bus_x = lab_x + labirinto.get_width() // 2 - 60
    bus_y = lab_y + labirinto.get_height() + 200

    return bus_x, bus_y

def reiniciar_jogo():
    return {
        'x_c': 240,
        'y_c': 205,
        'status': {'passo': 0, 'piscando': False, 'olhar': 1},
        'contador_anim': 0,
        'timer_pisca': 0,
        'alternar': 0,
        'tempo_inicial': pygame.time.get_ticks(),
        'tempo_game_over': 0,
        'tempo_vitoria': 0,
        'movendo': False
    }

def processar_eventos(estado, opcao_menu, jogo_data):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if estado == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opcao_menu = (opcao_menu - 1) % 2
                elif event.key == pygame.K_DOWN:
                    opcao_menu = (opcao_menu + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if opcao_menu == 0:
                        return "jogo", opcao_menu, reiniciar_jogo()
                    elif opcao_menu == 1:
                        pygame.quit()
                        sys.exit()

        elif estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "menu", opcao_menu, jogo_data

    return estado, opcao_menu, jogo_data

def atualizar_jogo(data):
    teclas = pygame.key.get_pressed()

    tempo_atual = pygame.time.get_ticks()
    tempo_passado = (tempo_atual - data['tempo_inicial']) // 1000
    tempo_restante = max(0, 20 - tempo_passado)

    game_over = tempo_restante == 0

    bus_x, bus_y = get_posicao_onibus()

    vitoria = (
        abs(data['x_c'] - bus_x) < 60 and
        abs(data['y_c'] - bus_y) < 30
    )

    m = identidade()
    data['movendo'] = False
    data['status']['olhar'] = 0

    if not game_over and not vitoria:
        dx, dy = 0, 0

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            dx = -3
            data['status']['olhar'] = -1

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            dx = 3
            data['status']['olhar'] = 1

        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            dy = -3

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            dy = 3

        if dx != 0 or dy != 0:
            m = multiplica_matrizes(translacao(dx, dy), m)
            data['movendo'] = True

    data['x_c'], data['y_c'] = aplicar_transformacao(m, data['x_c'], data['y_c'])

    data['x_c'] = max(0, min(data['x_c'], MAP_LARGURA))
    data['y_c'] = max(0, min(data['y_c'], MAP_ALTURA))

    if data['movendo']:
        data['contador_anim'] += 1
        if data['contador_anim'] > 10:
            data['status']['passo'] = 1
            data['alternar'] += 1
            data['contador_anim'] = 0
    else:
        data['status']['passo'] = 0
        data['alternar'] = 0

    data['timer_pisca'] += 1
    if data['timer_pisca'] > 150:
        data['status']['piscando'] = True
        if data['timer_pisca'] > 162:
            data['status']['piscando'] = False
            data['timer_pisca'] = 0

    if vitoria:
        data['tempo_vitoria'] += 1

    if game_over and not vitoria:
        data['tempo_game_over'] += 1

    return tempo_restante, vitoria, game_over

def desenhar(estado, opcao_menu, jogo_data, tempo_restante, vitoria, game_over):

    if estado == "menu":
        tela.blit(pygame.transform.scale(fundo, (LARGURA, ALTURA)), (0, 0))
        desenhar_overlay_escuro(tela, LARGURA, ALTURA, intensidade=3)
        desenhar_menu(tela, LARGURA, ALTURA, opcao_menu)

    elif estado == "jogo":

        cam_x = max(0, min(jogo_data['x_c'] - LARGURA // 2, MAP_LARGURA - LARGURA))
        cam_y = max(0, min(jogo_data['y_c'] - ALTURA // 2, MAP_ALTURA - ALTURA))

        tela.fill((0, 0, 0))

        for x in range(0, MAP_LARGURA, fundo.get_width()):
            for y in range(0, MAP_ALTURA, fundo.get_height()):
                tela.blit(fundo, (x - cam_x, y - cam_y))

        lab_x = (MAP_LARGURA - labirinto.get_width()) // 2
        lab_y = 300
        tela.blit(labirinto, (lab_x - cam_x, lab_y - cam_y))

        desenhar_casa(tela, 50 - cam_x, 100 - cam_y)

        bus_x, bus_y = get_posicao_onibus()
        desenhar_onibus(tela, bus_x - cam_x, bus_y - cam_y, 3)

        cores = {
            'BRANCO': (255,255,255),
            'PRETO': (0,0,0),
            'LARANJA': (255,120,0),
            'PELE': (214,193,140),
            'PELE_SOMBRA': (190,150,120),
            'ROSA': (190,0,150),
            'ROSA_CLARO': (220,0,180),
            'AZUL': (20,170,255),
            'FUNDO': (220,220,220)
        }

        desenhar_boneca(
            tela,
            jogo_data['x_c'] - cam_x,
            jogo_data['y_c'] - cam_y,
            3,
            cores,
            jogo_data['status'],
            jogo_data['alternar']
        )

        desenhar_hud(tela, tempo_restante, LARGURA)

        if vitoria:
            desenhar_tela_vitoria(tela, LARGURA, ALTURA, jogo_data['tempo_vitoria'])
        elif game_over:
            desenhar_tela_game_over(tela, LARGURA, ALTURA, jogo_data['tempo_game_over'])

def main():
    estado = "menu"
    opcao_menu = 0
    jogo_data = reiniciar_jogo()

    while True:
        estado, opcao_menu, jogo_data = processar_eventos(estado, opcao_menu, jogo_data)

        tempo_restante, vitoria, game_over = 0, False, False

        if estado == "jogo":
            tempo_restante, vitoria, game_over = atualizar_jogo(jogo_data)

        desenhar(estado, opcao_menu, jogo_data, tempo_restante, vitoria, game_over)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()