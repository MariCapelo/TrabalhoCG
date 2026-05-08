# O Último Ônibus 

**O Último Ônibus** é um jogo 2D estilo arcade desenvolvido como projeto prático de Computação Gráfica. O desafio central é ajudar uma menina atrasada para sua aula a atravessar um labirinto o mais rápido possível para conseguir pegar o último ônibus que lhe levará a tempo para aula.

---

## Objetivo

- Chegar ao ônibus antes que ele parta  
- Navegar pelo labirinto otimizando o tempo  

---

## Controles

- `W / ↑` → mover para cima  
- `S / ↓` → mover para baixo  
- `A / ←` → mover para esquerda  
- `D / →` → mover para direita  
- `R` → voltar ao menu  

---

## Conceitos de Computação Gráfica Utilizados

O desenvolvimento aplicou os seguintes pilares da disciplina:

### Rasterização
- **Set Pixel** para pixel art e texturas
- Algoritmo de **Bresenham** para traçado de retas  

### Preenchimento
- Algoritmo **Scanline**  

### Transformações Geométricas
- **Translação:** movimentação fluida do personagem  
- **Rotação (Matriz):** animação do ponteiro do temporizador em sentido horário  
- **Escala:** ampliação dos botões quando selecionados no menu  

### Janela e Viewport
- Sistema de câmera baseado em coordenadas de mundo (World Coordinates)  

### Textura
- Aplicação de imagens como fundo e labirinto  

### Animação
- Ciclo de movimento do personagem  
- Animação de piscar  
- **Temporizador visual** com ponteiro rotacionando em sentido horário (utilizando matriz de rotação)

### Interação
- Entrada via teclado  
- Menu interativo  

---

## Arquitetura do Projeto

O código foi modularizado em camadas:

### Módulos Principais

#### `entidades/`
Contém as entidades (gameobjects) do jogo:
- **`bonequinha.py`** - Desenho e animação da personagem principal (ciclo de caminhada, piscar)
- **`casa.py`** - Renderização da casa (ponto de partida)
- **`onibus.py`** - Desenho do ônibus (objetivo final do jogo)
- **`temporizador.py`** - Relógio visual com ponteiro rotacionado via matriz de transformação

#### `render/`
Implementação de algoritmos gráficos fundamentais:
- **`renderizacao.py`** - Primitivas de desenho (setPixel, Bresenham, Scanline, círculo, polígono)
- **`transformacoes.py`** - Matrizes de transformação geométrica (translação, escala, rotação, composição)

#### `ui/`
Interface visual e HUD do jogo:
- **`menu.py`** - Menu inicial com botões interativos (START/SAIR) com escala dinâmica
- **`dicionario.py`** - Renderização de texto na tela
- **`relogio.py`** - HUD exibindo tempo restante durante o jogo
- **`gameover.py`** - Tela exibida quando o tempo acaba
- **`youwin.py`** - Tela exibida ao alcançar o ônibus com sucesso

#### `main.py`
Loop principal do jogo com:
- Gerenciamento de estados (menu, jogo, vitória, derrota)
- Detecção de colisão com labirinto
- Controle de entrada (teclado)
- Renderização em ordem (câmera, fundo, entidades, HUD)
- Sistema de áudio (efeitos de passos)

#### Diretórios de Assets
- **`sprites/`** - Imagens PNG (fundo, labirinto, pista)
- **`sons/`** - Arquivos de áudio MP3 (passos, vitória, derrota)

---

## Como Executar

### Pré-requisitos
- Python 3.x  
- Pygame  
- UV (gerenciador de pacotes) ou pip

### Instalação
```bash
uv run main.py
```

ou com pip:

```bash
pip install pygame
python main.py
```

## Figma do Trabalho
https://www.figma.com/design/0TdbGbX6k0UgBBwjbYdmao/CompGráfica?node-id=107-2&t=wcfi7iez113P90pE-0

## Sites usados no trabalho 
https://www.pixilart.com
https://pixabay.com/pt/sound-effects/

## Equipe
Larissa Kelly
Leticia Carneiro
Marina Campelo
