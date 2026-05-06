def identidade():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]


def translacao(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]


def escala(sx, sy):
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]


def rotacao(theta):
    import math
    c = math.cos(theta)
    s = math.sin(theta)

    return [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ]


def multiplica_matrizes(a, b):
    resultado = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado


def cria_transformacao():
    return identidade()


def aplicar_transformacao(m, x, y):
    x_novo = m[0][0] * x + m[0][1] * y + m[0][2]
    y_novo = m[1][0] * x + m[1][1] * y + m[1][2]

    return x_novo, y_novo
