import pygame
from camera.hand_tracking import HandTracker
from game.game_loop import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def load_and_scale(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, size)

# load images
fruit_images = [
    load_and_scale("assets/images/apple.png", (80, 80)),
    load_and_scale("assets/images/banana.png", (120, 60)),
    load_and_scale("assets/images/orange.png", (80, 80)),
]

bg = load_and_scale("assets/images/background.png", (800, 600)).convert()

tracker = HandTracker()
game = Game(screen, fruit_images, bg)

running = True
while running:
    frame = tracker.update()
    fingertip = tracker.get_fingertip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update(fingertip)
    game.draw()

    pygame.display.flip()
    clock.tick(60)

tracker.release()
pygame.quit()
