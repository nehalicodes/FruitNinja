import random

class Fruit:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset()

    def reset(self):
        self.x = random.randint(50, self.screen_width - 50)
        self.y = self.screen_height + 50
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-18, -22)
        self.radius = 30
        self.color = (255, 0, 0)  # red

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.6  # gravity

        # if fruit falls off screen, respawn
        if self.y - self.radius > self.screen_height + 100:
            self.reset()

    def draw(self, screen, pygame):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
