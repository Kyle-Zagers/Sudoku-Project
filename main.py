import sys

import pygame


def start_screen(WIDTH, HEIGHT):
    pygame.init()

    BG_COLOR = (255, 255, 245)
    LINE_COLOR = (245, 152, 66)
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    # Initialize title font
    start_title_font = pygame.font.Font(None, 90)
    start_title2_font = pygame.font.Font(None, 66)
    button_font = pygame.font.Font(None, 50)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 175))
    screen.blit(title_surface, title_rectangle)

    title_surface2 = start_title2_font.render("Select Game Mode:", 0, LINE_COLOR)
    title_rectangle2 = title_surface2.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(title_surface2, title_rectangle2)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    # start_surface.fill(LINE_COLOR)
    # start_surface.blit(start_text, (10, 10))
    #
    # quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    # quit_surface.fill(LINE_COLOR)
    # quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle

    easy_rectangle = easy_surface.get_rect(center=(WIDTH//4, HEIGHT//2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    hard_rectangle = hard_surface.get_rect(center=((3*WIDTH)//4, HEIGHT//2 + 100))

    # start_rectangle = start_surface.get_rect(
    #     center=(WIDTH // 2, HEIGHT // 2 + 50))
    # quit_rectangle = quit_surface.get_rect(
    #     center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # screen.blit(start_surface, start_rectangle)
    # screen.blit(quit_surface, quit_rectangle)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                if medium_rectangle.collidepoint(event.pos):
                    return "medium"
                if hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()


    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if start_rectangle.collidepoint(event.pos):
    #                 # Checks if mouse is on start button
    #                 return  # If the mouse is on the start button, we can return to main
    #             elif quit_rectangle.collidepoint(event.pos):
    #                 # If the mouse is on the quit button, exit the program
    #                 sys.exit()
    #     pygame.display.update()


if __name__ == "__main__":
    start_screen(675, 750)

