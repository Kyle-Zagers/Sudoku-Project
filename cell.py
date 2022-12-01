import pygame


class Cell:
    cell_size = 75

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self, screen):
        value_font = pygame.font.Font(None, 60)
        value_surf = value_font.render(f'{self.value if ord("1")<=ord(self.value)<=ord("9") else ""}', 0, (255, 255, 255))
        value_rect = value_surf.get_rect(
            center=(self.cell_size // 2 + self.cell_size * self.col, self.cell_size // 2 + self.cell_size * self.row))
        screen.blit(value_surf, value_rect)
        
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return int(self.value)

    def __int__(self):
        return int(self.value)
