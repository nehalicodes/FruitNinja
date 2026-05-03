import pygame
import random
from .fruit import Fruit
from .blade import Blade

class Game:
    def __init__(self, screen, fruit_images, bg_image):
        self.screen = screen
        self.fruit_images = fruit_images
        self.bg = bg_image
        self.fruits = []
        self.blade = Blade()
        self.score = 0
        self.spawn_timer = 0

    def spawn_fruit(self):
        fruit = Fruit(self.fruit_images, self.screen.get_width(), self.screen.get_height())
        self.fruits.append(fruit)

    def update(self, fingertip):
        # update blade
        self.blade.update(fingertip)

        # spawn fruits
        self.spawn_timer += 1
        if self.spawn_timer > 40:
            self.spawn_fruit()
            self.spawn_timer = 0

        # update fruits
        for fruit in self.fruits:
            fruit.update()

        # collision detection
        if fingertip:
            fx, fy = fingertip
            for fruit in self.fruits:
                rect = fruit.image.get_rect(center=(fruit.x, fruit.y))
                if rect.collidepoint(fx, fy) and fruit.alive:
                    fruit.alive = False
                    self.score += 1

        # remove dead/offscreen fruits
        self.fruits = [f for f in self.fruits if f.alive and not f.is_offscreen(self.screen.get_height())]

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        for fruit in self.fruits:
            fruit.draw(self.screen)

        self.blade.draw(self.screen)

        # score
        font = pygame.font.Font(None, 48)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (20, 20))
