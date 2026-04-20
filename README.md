# Como rodar o código?
## Passo 1: Instale o UV
-> *Se voce possuir o uv pode pular essa etapa e ir para o passo 2.*

O uv é um gerenciador de pacotes como o pip. Caso voce não possua o uv instalado pode instalar por meio desse [link](https://docs.astral.sh/uv/getting-started/installation/).

Não esqueça de verificar se a instalaçao foi bem sucedida usando o comando (para usuários windows):
```
uv --version
```
Ele deve retornar a versão do uv se a instalação for bem sucedida.

## Passo 2: Criando venv
Após a instalação do uv, entre na pasta do projeto e crie o ambiente virtual:
```
uv venv
```
Ative o ambiente virtual:
```
.venv/Scripts/activate
```
**Importante** -> verifique se a versão do python usada no ambiente virtual é a mesma do projeto (3.12.9)
## Passo 3: Instalando dependencias
Com o ambiente virtual criado, rode o comando:
```
uv sync
```
Por meio do `uv.lock`, esse comando irá instalar no seu ambiente virtual todas as dependecias necessárias para rodar os scripts do projeto. No caso desse projeto, apenas o `Pygame` é necessário.

## Passo 4: Rodando script 
Para rodar o jogo basta digitar:
```
uv run main.py
```

## Para mais informações 
- [Uv Features](https://docs.astral.sh/uv/getting-started/features/)
- [Pygame](https://www.pygame.org/docs/)

