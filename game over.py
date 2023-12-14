import pygame
import os
import sys



FPS = 60
speed = 200
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 300
    last = width
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 255))
    image = load_image("gameover.png")
    x, y = -600, 0
    screen.blit(image, (x,y))
    pygame.display.flip()
    almost_done = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if speed / FPS < last:
            last -= speed / FPS
            x += speed / FPS
            almost_done = True
        elif almost_done:
            x += last
            almost_done = False

        screen.fill((0, 0, 255))
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
