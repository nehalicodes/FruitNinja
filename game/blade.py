import pygame
from collections import deque

class Blade:
    def __init__(self, max_length=12):
        self.points = deque(maxlen=max_length)

    def update(self, fingertip):
        if fingertip:
            self.points.append(fingertip)

    def draw(self, screen):
        if len(self.points) > 1:
            pygame.draw.lines(screen, (0, 255, 255), False, self.points, 4)
