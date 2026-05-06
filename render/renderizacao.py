import pygame

def setPixel(superficie, x, y, cor):
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)

def bresenham(superficie, x0, y0, x1, y1, cor):
    steep = abs(y1 - y0) > abs(x1 - x0)

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    ystep = 1
    if dy < 0:
        ystep = -1
        dy = -dy

    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x0
    y = y0

    while x <= x1:
        if steep:
            setPixel(superficie, y, x, cor)
        else:
            setPixel(superficie, x, y, cor)

        if d <= 0:
            d += incE
        else:
            d += incNE
            y += ystep

        x += 1

def desenhar_poligono(tela, pontos, cor):
    for i in range(len(pontos)):
        x0, y0 = pontos[i]
        x1, y1 = pontos[(i + 1) % len(pontos)]
        bresenham(tela, x0, y0, x1, y1, cor)

def scanline(tela, pontos, cor):
    y_min = min(p[1] for p in pontos)
    y_max = max(p[1] for p in pontos)

    for y in range(y_min, y_max + 1):
        inter = []

        for i in range(len(pontos)):
            x1, y1 = pontos[i]
            x2, y2 = pontos[(i + 1) % len(pontos)]

            if y1 == y2:
                continue

            if min(y1, y2) <= y < max(y1, y2):
                x = int(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
                inter.append(x)

        inter.sort()

        for i in range(0, len(inter), 2):
            if i + 1 < len(inter):
                for x in range(inter[i], inter[i+1]):
                    setPixel(tela, x, y, cor)
