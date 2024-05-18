import pygame, time, random

class Hazard: 
    # Essa classe define Ameaça ao Jogador

    image = None
    x = None
    y = None

    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (130, 130))
        self.image = hazard_fig
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))