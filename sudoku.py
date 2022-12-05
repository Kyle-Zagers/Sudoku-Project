import sys
from constants import *
from board import Board
import pygame


def start_screen(screen):
    pygame.display.set_caption("Sudoku")

    # Initialize title font
    start_title_font = pygame.font.Font(None, 90)
    start_title2_font = pygame.font.Font(None, 66)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", False, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 175))
    screen.blit(title_surface, title_rectangle)

    title_surface2 = start_title2_font.render("Select Game Mode:", False, LINE_COLOR)
    title_rectangle2 = title_surface2.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(title_surface2, title_rectangle2)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", False, (255, 255, 255))
    medium_text = button_font.render("Medium", False, (255, 255, 255))
    hard_text = button_font.render("Hard", False, (255, 255, 255))

    # Initialize the buttons' background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangles

    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(center=((3 * WIDTH) // 4, HEIGHT // 2 + 100))

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


def won_exit_screen(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 90)
    start_title2_font = pygame.font.Font(None, 66)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Game Won!", False, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 175))
    screen.blit(title_surface, title_rectangle)

    won_text = button_font.render("Exit", False, (255, 255, 255))
    won_surface = pygame.Surface((won_text.get_size()[0] + 20, won_text.get_size()[1] + 20))
    won_surface.fill(LINE_COLOR)
    won_surface.blit(won_text, (10, 10))
    won_rectangle = won_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 100))
    screen.blit(won_surface, won_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if won_rectangle.collidepoint(event.pos):
                    sys.exit()

def loss_exit_screen(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 90)
    start_title2_font = pygame.font.Font(None, 66)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("You Lost :(", False, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 175))
    screen.blit(title_surface, title_rectangle)

    loss_text = button_font.render("Restart", False, (255, 255, 255))
    loss_surface = pygame.Surface((loss_text.get_size()[0] + 20, loss_text.get_size()[1] + 20))
    loss_surface.fill(LINE_COLOR)
    loss_surface.blit(loss_text, (10, 10))
    loss_rectangle = loss_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 100))
    screen.blit(loss_surface, loss_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if loss_rectangle.collidepoint(event.pos):
                    sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    mode = start_screen(screen)
    screen.fill((0, 150, 200))
    print(mode)

    board = Board(WIDTH, HEIGHT, screen, mode)
    board.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("reset")
                    # for resetting the game when "r" pressed.