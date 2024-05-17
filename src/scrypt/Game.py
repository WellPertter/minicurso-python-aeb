import pygame
from Background import Background

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None

    def __init__(self, size, fullscreen):

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height)) # tamanho da screen
        self.screen_size = self.screen.get_size()

        #pygame.mouse.set_visible(0) # desabilita o mouse
        pygame.display.set_caption('Fuga Espacial')


    def handle_events(self):
        # Trata o evento e toma a ação necessária.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False


    def elements_update(self, dt):
        self.background.update(dt) # atualiza os elementos

    
    def elements_draw(self):
        self.background.draw(self.screen) # desenha os elementos

    def loop(self):
        # Laço principal 

        #Variável para movimento de plano de fundo/background
        valocidade_background = 5

        #movimento da margem esquerda
        movL_x = 0 
        movL_y = 0

        #movimento da margem esquerda
        movR_x = 740 
        movR_y = 0

        self.background = Background() #Criar objeto backgroud

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

            
            self.handle_events() # trata os eventos

            self.elements_update(dt) #atualizar os elementos

            #Atualizar a tela 
            pygame.display.update()
            clock.tick(2000) 
