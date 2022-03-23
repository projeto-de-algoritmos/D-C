
import atexit
import pygame
from pygame.locals import *
from sys import exit
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group
from pygame import event
from random import randint
import numpy as np
import math
import statistics

jogadores = 20


def dist(a, b):
    x1 = a.rect.x
    x2 = b.rect.x
    y1 = a.rect.y
    y2 = b.rect.y
    return math.hypot(x1-x2, y1-y2)


def bruto(x):
    n = len(x)
    ponto1 = 0
    ponto2 = 0
    distmin = 10000000000000000000000  # inicializar com distância muito grande
    for i in range(0, n-1):  # comparar todos os pares possíveis
        for j in range(i+1, n-1):
            if dist(x[i], x[j]) <= distmin:
                ponto1 = i
                ponto2 = j
                distmin = dist(x[i], x[j])
                print(ponto1, ponto2, distmin)
    atletas[ponto1].kill()
    atletas.pop(ponto1)
    atletas[ponto2].kill()
    atletas.pop(ponto2)


pygame.init()
musica_tema = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

largura = 1000
altura = 600
tamanhoDaTela = 1000, 600

fonte = pygame.font.SysFont('arial', 40, True, True)


tela = pygame.display.set_mode(tamanhoDaTela)
pygame.display.set_caption('STOP!')
fundo = scale(
    load('images/quadra.png'),
    tamanhoDaTela)
clock = pygame.time.Clock()


class Atleta(Sprite):

    def __init__(self):
        super().__init__()

        self.image = scale(
            load('images/atleta.png'),
            (60, 60))
        self.rect = self.image.get_rect(
            center=(randint(0, 900), randint(0, 500)
                    ))
        self.jogo = 0
        self.direction = 1
        self.speed_x = 5
        self.speed_y = 4

    def playGame(self):
        self.jogo = 1

    def update(self):
        if(self.jogo == 1):
            if(self.rect.left <= 20 or self.rect.right >= 940):
                self.direction *= -1
                self.speed_y = randint(1, 5) * self.direction
                self.speed_x = randint(1, 5) * self.direction
                if self.speed_x == 0 and self.speed_y == 0:
                    self.speed_x = randint(2, 5) * self.direction
                    self.speed_y = randint(2, 5) * self.direction
            if self.rect.top <= 50 or self.rect.bottom >= 540:
                self.direction *= -1
                self.speed_y = randint(1, 5) * self.direction
                self.speed_x = randint(1, 5) * self.direction
                if self.speed_x == 0 and self.speed_y == 0:
                    self.speed_x = randint(2, 5) * self.direction
                    self.speed_y = randint(2, 5) * self.direction

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y


atletas = []
grupo_atletas = Group()
i = 0
while i <= 19:
    atletas.append(Atleta())
    grupo_atletas.add(atletas[i])
    i = i + 1


while True:
    clock.tick(60)
    mensagem = f'Jogadores: {jogadores}'
    texto_formatado = fonte.render(mensagem, False, (0, 0, 255))

    # Espaco dos Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYUP:
            if event.key == K_SPACE:
                k = 0
                while k <= 19:
                    atletas[k].playGame()
                    k += 1
            if event.key == K_TAB:

                bruto(atletas)
                jogadores = jogadores - 2

    # Espaco deo siplay
    tela.blit(fundo, (0, 0))
    tela.blit(texto_formatado, (390, 20))

    grupo_atletas.draw(tela)
    grupo_atletas.update()
    pygame.display.update()
