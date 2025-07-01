class StateManager:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def switch_to(self, new_state):
        self.current_state = new_state

    def handle_events(self, player, events):
        self.current_state.handle_events(player, events)

    def update(self):
        self.current_state.update()

    def draw(self, screen):
        self.current_state.draw(screen)
    
    