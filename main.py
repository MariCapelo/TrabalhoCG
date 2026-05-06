import pygame
import sys
from entidades.bonequinha import desenhar_boneca
from render.transformacoes import (identidade, translacao, multiplica_matrizes, aplicar_transformacao)
from entidades.casa import desenhar_casa
from entidades.sombra_labirinto import criar_sombra_labirinto, desenhar_sombra_labirinto
from ui.relogio import desenhar_hud
from ui.menu import desenhar_menu, desenhar_overlay_escuro
from ui.gameover import desenhar_tela_game_over
from ui.youwin import desenhar_tela_vitoria
from entidades.onibus import desenhar_onibus 

pygame.init()


def criar_hitbox_boneca(x, y, escala):
    return pygame.Rect(int(x - 8 * escala), int(y - 18 * escala), int(16 * escala), int(25 * escala))


def colide_com_mapa(mascara_colisao, mascara_hitbox, hitbox, origem_x, origem_y):
    offset = (hitbox.left - origem_x, hitbox.top - origem_y)
    return mascara_colisao.overlap(mascara_hitbox, offset) is not None

# Configurações da tela
# ================= CONFIG =================
LARGURA, ALTURA = 1000, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Configurações de mundo 
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
        
        tela.blit(labirintoUp, (labUp_x - camera_x, labUp_y - camera_y))

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