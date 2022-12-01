import pygame
from sudoku_generator import *
from cell import Cell


class Board:
    cell_size = 75
    square_size = 225
    line_color = (245, 152, 66)
    bold_line_width = 6
    thin_line_width = 2
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
        board_and_answers = generate_sudoku(9, self.removed)
        starting_values = board_and_answers[0]
        self.answers = board_and_answers[1]
        for column in range(9):
            self.cells[column] = {}
            for row in range(9):
                self.cells[column][row] = Cell(f"{starting_values[column][row]}", row, column, screen)

    def draw(self):
        # draw horizontal lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.line_color, (0, self.square_size * i),
                             (self.width, self.square_size * i), self.bold_line_width)

            for i in range(1, 9):
                pygame.draw.line(self.screen, self.line_color, (0, self.cell_size * i),
                                 (self.width, self.cell_size * i), self.thin_line_width)
        # draw vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.line_color, (self.square_size * i, 0),
                             (self.square_size * i, self.height), self.bold_line_width)

        for i in range(1, 9):
            pygame.draw.line(self.screen, self.line_color, (self.cell_size * i, 0),
                             (self.cell_size * i, self.height), self.thin_line_width)

        pygame.draw.line(self.screen, (0, 125, 200), (0, self.square_size+56 * i),
                         (self.width, self.square_size+56 * i), self.bold_line_width)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw(self.screen)

