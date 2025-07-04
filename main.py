import pygame
import sys

from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from core.game import Game
from entities.player import Player


def main():
    # Initialize pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Glitchmaze: Broken by Design")
    print("olaa")

    # Start the main game object
    game = Game(screen)
    game.run()

    # Clean up and exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
