import math
import pygame

def setPixel(superficie, x, y, cor):
    if 0 <= x and 0 <= y :
        superficie.set_at((x, y), cor)


def quatro_pontos(superficie, centro_x, centro_y, x, y, cor):
    setPixel(superficie, centro_x + x, centro_y + y, cor)
    setPixel(superficie, centro_x - x, centro_y + y, cor)
    setPixel(superficie, centro_x + x, centro_y - y, cor)
    setPixel(superficie, centro_x - x, centro_y - y, cor)


def circulo(superficie, cor, centro, raio):
    centro_x, centro_y = centro
    for x in range(raio + 1):
        y = round(math.sqrt(raio * raio - x * x))
        quatro_pontos(superficie, centro_x, centro_y, x, y, cor)

    for y in range(raio + 1):
        x = round(math.sqrt(raio * raio - y * y))
        quatro_pontos(superficie, centro_x, centro_y, x, y, cor)


def linha(tela, x_init, y_init, x_final, y_final, cor):
    dx = x_final - x_init
    dy = y_final - y_init

    if abs(dx) > abs(dy):
        if x_init > x_final:
            x_init, y_init, x_final, y_final = x_final, y_final, x_init, y_init
            dx = -dx
            dy = -dy

        m = dy / dx
        for x in range(x_init, x_final + 1):
            y = round(y_init + m * (x - x_init))
            setPixel(tela, x, y, cor)

    else:
        if y_init > y_final:
            x_init, y_init, x_final, y_final = x_final, y_final, x_init, y_init
            dx = -dx
            dy = -dy

        m_inv = dx / dy
        for y in range(y_init, y_final + 1):
            x = round(x_init + m_inv * (y - y_init))
            setPixel(tela, x, y, cor)