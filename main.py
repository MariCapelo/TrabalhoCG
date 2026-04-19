import pygame 
from pygame.locals import *
from sys import exit
from Poligonos import circulo, linha

def main():
    pygame.init()
    altura = 768
    largura = 1024
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Joguinho')

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        tela.fill((254, 250, 224))
        circulo(tela, (0, 0, 0), (largura // 2, altura // 2 + (altura // 4)), 50)
        linha(tela, 0, 0, largura, altura, (0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
