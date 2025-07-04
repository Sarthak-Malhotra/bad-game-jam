from pygame.math import Vector2

class Player:
    def __init__(self, inventory, position: Vector2, velocity: Vector2):
        self.inventory = inventory
        self.position = position
        self.velocity = velocity
    
    def move(self, new_position):
        self.position = new_position

       
