import pygame

class Paredinha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        paredinha = pygame.image.load('imagens/paredinha.png').convert()
        paredinha = pygame.transform.scale2x(paredinha)
        paredinha_rect = paredinha.get_rect(center = (200, 200))

        self.image = paredinha
        self.rect = paredinha_rect


