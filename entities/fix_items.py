from pygame.math import Vector2


class text:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=pos)
        self.dragging = False
        self.offset = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def start_drag(self, mouse_pos):
        self.dragging = True
        self.offset = (self.rect.x - mouse_pos[0], self.rect.y - mouse_pos[1])

    def drag(self, mouse_pos):
        if self.dragging:
            self.rect.topleft = (mouse_pos[0] + self.offset[0], mouse_pos[1] + self.offset[1])

    def stop_drag(self):
        self.dragging = False