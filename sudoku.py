import sys
from sudoku_generator import *
from board import Board
import pygame


def start_screen(width, height, screen):
    bg_color = (0, 150, 200)
    line_color = (245, 152, 66)
    pygame.display.set_caption("Sudoku")

    # Initialize title font
    start_title_font = pygame.font.Font(None, 90)
    start_title2_font = pygame.font.Font(None, 66)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(bg_color)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, line_color)
    title_rectangle = title_surface.get_rect(
        center=(width // 2, height // 2 - 175))
    screen.blit(title_surface, title_rectangle)

    title_surface2 = start_title2_font.render("Select Game Mode:", 0, line_color)
    title_rectangle2 = title_surface2.get_rect(
        center=(width // 2, height // 2))
    screen.blit(title_surface2, title_rectangle2)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize the buttons' background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(line_color)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(line_color)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(line_color)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangles

    easy_rectangle = easy_surface.get_rect(center=(width // 4, height // 2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(width // 2, height // 2 + 100))
    hard_rectangle = hard_surface.get_rect(center=((3 * width) // 4, height // 2 + 100))

    # Draw buttons

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                if medium_rectangle.collidepoint(event.pos):
                    return "medium"
                if hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    width = 675
    height = 750
    screen = pygame.display.set_mode([width, height])
    mode = start_screen(width, height, screen)
    screen.fill((0, 150, 200))
    print(mode)

    boardy = Board(width, height, screen, mode)
    boardy.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
