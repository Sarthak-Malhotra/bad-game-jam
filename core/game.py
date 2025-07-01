import pygame
from pygame.math import Vector2
from core.settings import FPS
from core.state_manager import StateManager
from modes.play_mode import PlayMode
from entities.player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player([],Vector2(10,10))
        self.clock = pygame.time.Clock()
        self.state_manager = StateManager(PlayMode())
        

    def run(self):
        while True:
            events = pygame.event.get()
            self.state_manager.handle_events(self.player, events)
            print(self.player.position)
            self.state_manager.update()
            self.state_manager.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)


