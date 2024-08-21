import pygame
def scaleimg(img, scale):
    img = pygame.image.load(img)
    size = round(img.get_width() * scale), round(img.get_height() * scale)
    return pygame.transform.scale(img, size)