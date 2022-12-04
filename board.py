import pygame
from constants import *
from sudoku_generator import generate_sudoku
from cell import Cell


class Board:
    cells = {}

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height-75
        self.screen = screen
        self.removed = 0
        match difficulty:
            case "easy":
                self.removed = 30
            case "medium":
                self.removed = 40
            case "hard":
                self.removed = 50
        self.answers = generate_sudoku(9, self.removed)
        for column in range(9):
            self.cells[column] = {}
            for row in range(9):
                self.cells[column][row] = Cell(f"{self.answers[column][row]}", row, column, screen)

    def draw(self):
        # draw horizontal lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (self.width, SQUARE_SIZE * i), BOLD_LINE_WIDTH)

            for i in range(1, 9):
                pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE * i),
                                 (self.width, CELL_SIZE * i), THIN_LINE_WIDTH)
        # draw vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, self.height), BOLD_LINE_WIDTH)

        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE * i, 0),
                             (CELL_SIZE * i, self.height), THIN_LINE_WIDTH)

        pygame.draw.line(self.screen, (0, 125, 200), (0, SQUARE_SIZE + 56 * 8),
                         (self.width, SQUARE_SIZE + 56 * 8), BOLD_LINE_WIDTH)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw(self.screen)
