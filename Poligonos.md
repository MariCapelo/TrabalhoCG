# Poligonos.py

Este arquivo reúne funções básicas de desenho em Pygame usando pixels individuais. A ideia do módulo é construir formas geométricas a partir de pontos calculados manualmente, em vez de depender apenas das primitivas prontas da biblioteca.

## Como a tela funciona

No Pygame, a origem `(0, 0)` fica no canto superior esquerdo da janela.

- `x` aumenta para a direita
- `y` aumenta para baixo

Isso é importante porque os cálculos matemáticos precisam ser convertidos para esse sistema de coordenadas da tela.

## Funções principais

### `setPixel(superficie, x, y, cor)`

Essa é a função mais básica do módulo. Ela desenha um único pixel na posição `(x, y)` usando a cor informada.

Como ela funciona:

1. Verifica se `x` e `y` não são negativos.
2. Se a posição for válida, usa `superficie.set_at((x, y), cor)` para colorir aquele ponto.

Ela serve como base para todas as outras funções. Em vez de desenhar diretamente na tela em vários lugares do código, o módulo centraliza essa tarefa em uma função única.

### `quatro_pontos(superficie, centro_x, centro_y, x, y, cor)`

Essa função aproveita a simetria do círculo. Quando um ponto `(x, y)` da circunferência é calculado, é possível espelhar esse ponto nos outros quadrantes em relação ao centro.

Como ela funciona:

1. Recebe o centro do círculo: `(centro_x, centro_y)`.
2. Recebe um deslocamento `(x, y)` em relação a esse centro.
3. Desenha quatro versões simétricas desse ponto:
	- `(centro_x + x, centro_y + y)`
	- `(centro_x - x, centro_y + y)`
	- `(centro_x + x, centro_y - y)`
	- `(centro_x - x, centro_y - y)`

Essa abordagem evita repetir cálculo desnecessário e ajuda a montar a circunferência inteira a partir de poucos pontos.

### `circulo(superficie, cor, centro, raio)`

Essa função desenha a circunferência do círculo ponto a ponto com base na equação:

$$x^2 + y^2 = r^2$$

Como ela funciona:

1. Separa o centro em `centro_x` e `centro_y`.
2. Faz um primeiro laço variando `x` de `0` até `raio`.
3. Para cada `x`, calcula `y` com:

$$y = \sqrt{r^2 - x^2}$$

4. Usa `round(...)` para converter o valor calculado para pixel.
5. Chama `quatro_pontos(...)` para desenhar os pontos simétricos.
6. Depois faz um segundo laço variando `y` de `0` até `raio`.
7. Para cada `y`, calcula `x` com a mesma equação reorganizada.
8. Desenha novamente os quatro pontos simétricos.

Esse segundo laço existe para evitar falhas visuais. Se o círculo fosse calculado só variando `x`, algumas partes poderiam ficar com pequenos espaços entre pixels, principalmente nas regiões mais inclinadas da curva.

### `linha(tela, x_init, y_init, x_final, y_final, cor)`

Essa função desenha uma linha reta entre dois pontos usando pixels.

Como ela funciona:

1. Calcula as diferenças horizontais e verticais:

$$dx = x_{final} - x_{init}$$

$$dy = y_{final} - y_{init}$$

2. Compara `abs(dx)` e `abs(dy)` para decidir qual eixo deve ser percorrido.
3. Se a variação horizontal for maior, a linha é desenhada avançando em `x`.
4. Se a variação vertical for maior, a linha é desenhada avançando em `y`.
5. Em cada passo, calcula a outra coordenada usando a inclinação da reta.
6. Usa `setPixel(...)` para marcar cada ponto da linha.

Esse método funciona bem para linhas simples porque evita “buracos” maiores no traçado e adapta o cálculo conforme a inclinação da reta.

## Relação entre as funções

As funções se organizam em camadas:

1. `setPixel` desenha um ponto.
2. `quatro_pontos` usa `setPixel` para espalhar pontos simétricos.
3. `circulo` calcula os pontos matemáticos e delega o desenho para `quatro_pontos`.
4. `linha` também usa `setPixel`, mas para montar uma reta entre dois pontos.

Em resumo, o módulo implementa desenho geométrico manual: primeiro calcula as coordenadas matemáticas, depois transforma essas coordenadas em pixels na tela.




