from pygame.math import Vector2

class Player:
    def __init__(self, inventory, position: Vector2):
        self.inventory = inventory
        self.position = position
    
    def move(self, new_position):
        self.position = new_position

       
