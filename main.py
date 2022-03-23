
import pygame
from pygame.locals import *
from sys import exit
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group
from pygame import event
from random import randint


pygame.init()
musica_tema = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

largura = 1000
altura = 600
tamanhoDaTela = 1000, 600

jogadores = 20
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
            center=(randint(0, 950), randint(0, 550)
                    ))
        self.jogo = 0
        self.direction = 1
        self.speed_x = 5
        self.speed_y = 4

    def playGame(self):
        self.jogo = 1

    def update(self):
        if(self.jogo == 1):

            if(self.rect.left <= 20 or self.rect.right >= 1000):
                self.direction *= -1
                self.speed_x = randint(0, 5) * self.direction
            if self.rect.top <= 50 or self.rect.bottom >= 600:
                self.direction *= -1
                self.speed_y = randint(0, 5) * self.direction

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y


atleta1 = Atleta()
atleta2 = Atleta()
atleta3 = Atleta()
atleta4 = Atleta()
atleta5 = Atleta()
atleta6 = Atleta()
atleta7 = Atleta()
atleta8 = Atleta()
atleta9 = Atleta()
atleta10 = Atleta()
atleta11 = Atleta()
atleta12 = Atleta()
atleta13 = Atleta()
atleta14 = Atleta()
atleta15 = Atleta()
atleta16 = Atleta()
atleta17 = Atleta()
atleta18 = Atleta()
atleta19 = Atleta()
atleta20 = Atleta()
grupo_atletas = Group()
grupo_atletas.add(atleta1)
grupo_atletas.add(atleta2)
grupo_atletas.add(atleta3)
grupo_atletas.add(atleta4)
grupo_atletas.add(atleta4)
grupo_atletas.add(atleta5)
grupo_atletas.add(atleta6)
grupo_atletas.add(atleta7)
grupo_atletas.add(atleta8)
grupo_atletas.add(atleta9)
grupo_atletas.add(atleta10)
grupo_atletas.add(atleta11)
grupo_atletas.add(atleta12)
grupo_atletas.add(atleta13)
grupo_atletas.add(atleta14)
grupo_atletas.add(atleta15)
grupo_atletas.add(atleta16)
grupo_atletas.add(atleta17)
grupo_atletas.add(atleta18)
grupo_atletas.add(atleta19)
grupo_atletas.add(atleta20)

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
                atleta1.playGame()
                atleta2.playGame()
                atleta3.playGame()
                atleta4.playGame()
                atleta5.playGame()
                atleta6.playGame()
                atleta7.playGame()
                atleta8.playGame()
                atleta9.playGame()
                atleta10.playGame()
                atleta11.playGame()
                atleta12.playGame()
                atleta13.playGame()
                atleta14.playGame()
                atleta15.playGame()
                atleta16.playGame()
                atleta17.playGame()
                atleta18.playGame()
                atleta19.playGame()
                atleta20.playGame()

    # Espaco deo siplay
    tela.blit(fundo, (0, 0))
    tela.blit(texto_formatado, (390, 20))

    grupo_atletas.draw(tela)
    grupo_atletas.update()
    pygame.display.update()
