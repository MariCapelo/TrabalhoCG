import pygame
pygame.init()

# Tela (viewport)
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Mundo (mapa grande)
MAP_WIDTH, MAP_HEIGHT = 600, 2000

# Jogador
player_x, player_y = 300, 100
player_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Limitar jogador ao mapa
    player_x = max(0, min(player_x, MAP_WIDTH))
    player_y = max(0, min(player_y, MAP_HEIGHT))

    # 📷 CÂMERA (offset)
    camera_x = player_x - WIDTH // 2
    camera_y = player_y - HEIGHT // 2

    # Evitar mostrar fora do mapa
    camera_x = max(0, min(camera_x, MAP_WIDTH - WIDTH))
    camera_y = max(0, min(camera_y, MAP_HEIGHT - HEIGHT))

    # Desenho
    screen.fill((30, 30, 30))

    # Exemplo: desenhar "labirinto" simples (linhas)
    for y in range(0, MAP_HEIGHT, 100):
        pygame.draw.line(
            screen,
            (100, 100, 100),
            (0 - camera_x, y - camera_y),
            (MAP_WIDTH - camera_x, y - camera_y),
            2
        )

    # Jogador (círculo)
    pygame.draw.circle(
        screen,
        (255, 0, 0),
        (int(player_x - camera_x), int(player_y - camera_y)),
        10
    )

    pygame.display.flip()

pygame.quit()