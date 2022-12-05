import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = None
        self.row = row
        self.col = col
        self.screen = screen
        self.value_rect = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, sketched_value):
        if self.value == "0":
            pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect((self.col * 75)+5, (self.row * 75)+5, CELL_SIZE-10, CELL_SIZE-10))

            self.sketched_value = sketched_value
            value_font = pygame.font.Font(None, 60)
            value_surf = value_font.render(f'{self.sketched_value if ord("1") <= ord(self.sketched_value) <= ord("9") else "      "}',
                                           True, LINE_COLOR)
            self.value_rect = value_surf.get_rect(
                center=(CELL_SIZE // 2 + CELL_SIZE * self.col, CELL_SIZE // 2 + CELL_SIZE * self.row))
            self.screen.blit(value_surf, self.value_rect)
            pygame.display.update()

    def draw(self):
        value_font = pygame.font.Font(None, 60)
        value_surf = value_font.render(f'{self.value if ord("1")<=ord(self.value)<=ord("9") else "      "}', True,
                                       (255, 255, 255))
        self.value_rect = value_surf.get_rect(
            center=(CELL_SIZE // 2 + CELL_SIZE * self.col, CELL_SIZE // 2 + CELL_SIZE * self.row))
        self.screen.blit(value_surf, self.value_rect)
        
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return int(self.value)

    def __int__(self):
        return int(self.value)
