import pygame
from pygame import Vector2
import sys

class PlayMode:
    def handle_events(self, player, events):
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.velocity += Vector2(-1.5, 0)
                if event.key == pygame.K_d:
                    player.velocity += Vector2(1.5, 0)
                if event.key == pygame.K_w:
                    player.velocity += Vector2(0, -1.5)
                if event.key == pygame.K_s:
                    player.velocity += Vector2(0, 1.5)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.velocity += Vector2(1.5, 0)
                if event.key == pygame.K_d:
                    player.velocity += Vector2(-1.5, 0)
                if event.key == pygame.K_w:
                    player.velocity += Vector2(0, 1.5)
                if event.key == pygame.K_s:
                    player.velocity += Vector2(0, -1.5)

    def update(self):
        pass

    def draw(self, screen):
        pass


