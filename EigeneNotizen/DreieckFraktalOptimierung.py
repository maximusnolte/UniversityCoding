import pygame
import random
import time
import math

def fast_fractal(iterations, size=400):
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Sierpinski (FAST)")

    screen.fill((255, 255, 255))

    # Punkte des Dreiecks
    h = size * math.sqrt(3) / 2
    A = (400, 400 - h/2)
    B = (400 - size/2, 400 + h/2)
    C = (400 + size/2, 400 + h/2)
    corners = [A, B, C]

    # Startpunkt
    x, y = 500, 500

    start = time.time()

    # Pixelarray für maximale Speed
    px = pygame.PixelArray(screen)

    for _ in range(iterations):
        tx, ty = random.choice(corners)
        x = (x + tx) / 2
        y = (y + ty) / 2
        px[int(x)][int(y)] = (0, 0, 255)

    del px  # Pixelarray freigeben, sonst locked

    print("Finished in:", time.time() - start, "seconds")

    pygame.display.flip()

    # Fenster offen halten
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
if __name__ == '__main__':
    fast_fractal(100000,800) #ab 50.000 iterationen keine nennenswerte Qualitätsverbesserung