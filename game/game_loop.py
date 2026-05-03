import math
import pygame
from .fruit import Fruit

class Game:
    def __init__(self, screen, hand_tracker):
        self.screen = screen
        self.hand_tracker = hand_tracker
        self.width, self.height = screen.get_size()
        self.clock = pygame.time.Clock()
        self.running = True

        self.fruits = [Fruit(self.width, self.height) for _ in range(3)]
        self.score = 0

    def run(self):
        while self.running:
            # --- handle events ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # --- update camera / fingertip ---
            self.hand_tracker.update()
            fingertip = self.hand_tracker.get_fingertip()

            # --- update game objects ---
            self.screen.fill((20, 20, 20))

            for fruit in self.fruits:
                fruit.update()
                fruit.draw(self.screen, pygame)

                if fingertip:
                    fx, fy = fingertip
                    dist = math.hypot(fruit.x - fx, fruit.y - fy)
                    if dist < fruit.radius:
                        fruit.reset()
                        self.score += 1

            # draw fingertip as green circle (mapped directly for now)
            if fingertip:
                pygame.draw.circle(self.screen, (0, 255, 0), fingertip, 10)

            # draw score
            self._draw_score()

            pygame.display.flip()
            self.clock.tick(60)

    def _draw_score(self):
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
