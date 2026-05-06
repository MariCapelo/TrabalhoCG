# The Last Bus

**The Last Bus** é um jogo 2D estilo arcade desenvolvido como projeto prático de Computação Gráfica. O desafio central é atravessar um labirinto e alcançar o ônibus antes que o tempo se esgote.

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
- Algoritmo de **Bresenham** para traçado de retas  

### Preenchimento
- Algoritmo **Scanline**  

### Transformações Geométricas
- **Translação:** movimentação fluida do personagem  

### Janela e Viewport
- Sistema de câmera baseado em coordenadas de mundo (World Coordinates)  

### Textura
- Aplicação de imagens como fundo e labirinto  

### Animação
- Ciclo de movimento do personagem  
- Animação de piscar  

### Interação
- Entrada via teclado  
- Menu interativo  

---

## Arquitetura do Projeto

O código foi modularizado em camadas:

| Módulo | Descrição |
| :--- | :--- |
| `entidades/` | Personagem, como casa, menininha e ônibus |
| `render/` | Algoritmos gráficos (Bresenham, scanline, etc.) |
| `ui/` | Interface (menu, HUD, telas de vitória e derrota) |
| `assets/` | Imagens utilizadas no jogo |
| `main.py` | Loop principal e controle do jogo |

---

## Como Executar

### Pré-requisitos
- Python 3.x  
- Pygame  

### Instalação
```bash
pip install pygame
```

###Execução
```bash
python main.py
```

## Equipe
Larissa Kelly
Leticia Carneiro
Marina Campelo
