import pygame
from pygame import Vector2
import sys

class PlayMode:
    def handle_events(self, player, events):
        for event in events:
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_a:
                    print("A is pressed")
                    player.move(player.position - Vector2(1,0))

    def update(self):
        pass

    def draw(self, screen):
        pass
