import pygame





class Image(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.image.load(path)


