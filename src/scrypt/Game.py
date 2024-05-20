import pygame, time, random, os
from Background import Background
from Player import Player
from Hazard import Hazard
from Soundtrack import Soundtrack

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None
    hazard = []
    render_text_bateulateral = None
    render_text_perdeu = None
    soundtrack = None

    #movimento do player
    #RIGHT = pygame.K_RIGHT
    #LEFT = pygame.K_LEFT
    mudar_x = 0.0

    def __init__(self, size, fullscreen):

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height)) # tamanho da screen
        self.screen_size = self.screen.get_size()

        #pygame.mouse.set_visible(0) # desabilita o mouse
        pygame.display.set_caption('Fuga Espacial')

        #define as fontes
        my_font = pygame.font.Font("../Fonts/Fonte4.ttf", 100)

        # Mensagens para o jogador
        self.render_text_bateulateral = my_font.render("VOCÊ BATEU!", 0, (255, 255, 255))
        self.render_text_perdeu = my_font.render("GAME OVER!", 0, (255, 0, 0))


    def handle_events(self):
        # Trata o evento e toma a ação necessária.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            # se clicar em qualquer tecla, entra no if
            if event.type == pygame.KEYDOWN: 

                #se clicar na seta da esquerda, anda 3 para a esquerda no eixo x
                if event.key == pygame.K_LEFT:
                    self.mudar_x = -3

                #se clicar na seta da direita, anda 3 para a direita no eixo x
                if event.key == pygame.K_RIGHT:
                    self.mudar_x = 3

            # se soltar qualquer tecla, não faz nada
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.mudar_x = 0

    def elements_update(self, dt):
        self.background.update(dt) # atualiza os elementos

    
    def elements_draw(self):
        self.background.draw(self.screen) # desenha os elementos

    def loop(self):
        # Laço principal 

        score = 0
        h_passou = 0

        #Variável para movimento de plano de fundo/background
        valocidade_background = 5
        velocidade_hazard = 10

        hzrd = 0
        h_x = random.randrange(125, 660)
        h_y = -550

        # Info Hazard
        h_width = 100
        h_height = 110

        #Criar os Hazards
        self.hazard.append(Hazard("../images/satelite.png", h_x, h_y))
        self.hazard.append(Hazard("../images/nave.png", h_x, h_y))
        self.hazard.append(Hazard("../images/cometaVermelho.png", h_x, h_y))
        self.hazard.append(Hazard("../images/meteoros.png", h_x, h_y))
        self.hazard.append(Hazard("../images/buracoNegro.png", h_x, h_y))

        # Som ( possivelmente está com erro no meu computador - José Arthur)
        self.soundtrack = Soundtrack('../sounds/song.wav')
        self.soundtrack.play()

        #movimento da margem esquerda
        movL_x = 0 
        movL_y = 0

        #movimento da margem esquerda
        movR_x = 740 
        movR_y = 0

        self.background = Background() #Criar objeto backgroud

        #Posição do Player
        x = (self.width - 56) / 2
        y = self.height - 125

        #Criar o player
        self.player = Player(x, y)

        clock = pygame.time.Clock()
        dt = 16

        self.elements_draw() # desenhar os elementos

        while self.run:
            clock.tick(1000 / dt) # número máximo de FPS

            # adiciona movimento ao background
            self.background.move(self.screen, self.height, movL_x, movL_y, movR_x, movR_y)

            # atualiza as posições de movL_y e movR_y
            movL_y = movL_y + valocidade_background
            movR_y = movR_y + valocidade_background

            # se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > 600 and movR_y > 600:
                movL_y -= 600
                movR_y -= 600

            # Movimentação do Player
            #Altera a coordenada x da nave de acordo com as mudanças no event_handle() para ela se mover
            x = x + self.mudar_x

            #Desenha o Player    
            self.player.draw(self.screen, x, y)

            # Mostrar Score
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > 760 - 92 or x < 40 + 5:
                #som de colisão (computador está com problema no som- josé arthur)
                self.soundtrack.set("../sounds/jump2.wav")
                self.soundtrack.play()

                self.screen.blit(self.render_text_bateulateral, (80, 200))
                pygame.display.update() # atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            h_y = h_y + velocidade_hazard / 4
            self.hazard[hzrd].draw(self.screen, h_x, h_y)
            h_y = h_y + velocidade_hazard

            # definindo onde o harzard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if h_y > self.height:
                h_y = 0 - h_height
                h_x = random.randrange(125, 650 - h_height)
                hzrd = random.randint(0, 4 )
                # determinando quantos hazard passaram e a pontuação
                h_passou = h_passou + 1
                score = h_passou * 10
            
            self.handle_events() # trata os eventos

            self.elements_update(dt) #atualizar os elementos

            #Atualizar a tela 
            pygame.display.update()
            clock.tick(2000) 
    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, 35)
        passou = font.render("Passou: " + str(h_passou), True, (255, 255, 128))
        score = font.render("Score: " + str(score), True, (253, 231, 32))
        screen.blit(passou, (0, 50))
        screen.blit(score, (0, 100))
    


        


        
