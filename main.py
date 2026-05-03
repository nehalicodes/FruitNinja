import pygame
from camera.hand_tracking import HandTracker
from game.game_loop import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fruit Ninja - Camera Edition")

    hand_tracker = HandTracker()
    game = Game(screen, hand_tracker)

    try:
        game.run()
    finally:
        hand_tracker.release()
        pygame.quit()

if __name__ == "__main__":
    main()
