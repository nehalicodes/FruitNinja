import pygame
import random
import math

class Fruit:
    def __init__(self, images, screen_width, screen_height):
        self.image = random.choice(images)
        self.original_image = self.image
        self.x = random.randint(50, screen_width - 50)
        self.y = screen_height + 50  # spawn below screen
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-15, -15)
        self.gravity = 0.20
        self.angle = 0
        self.rotation_speed = random.uniform(-5, 5)
        self.alive = True

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.angle += self.rotation_speed

        # rotate image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self, screen):
        rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, rect)

    def is_offscreen(self, height):
        return self.y > height + 100
