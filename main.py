from src.board import Board
from src import constants
from src.game import Game

import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
#screen.fill(constants.BACKGROUND_COLOR)
clock = pygame.time.Clock()

# Game Instance (logic)
game = Game()

# Board Instance
board = Board(constants.WIDTH, constants.HEIGHT, game)

# Add title
pygame.display.set_caption("Ultimate TIC-TAC-TOE")

# Assume 1v1 with friend
player = 1


# To run the window, use the loop
while True:
    # pygame.QUIT event means the user clicked X to close the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Render
        # Draw the board and figures
        #board.draw(screen)
        # Update the display
        #pygame.display.update()

        # If the mouse is clicked it will switch to
        if event.type == pygame.MOUSEBUTTONDOWN:
            # How to access the coordinate to link the console board to the GUI
            # MOUSEBUTTONDOWN -> Return position
            # https://www.pygame.org/docs/ref/event.html#pygame.event.get
            mouseX, mouseY = event.pos

            # Are we gonna use conditionals to have a boundary within the board?
            # Still using the coordinate return by the MOUSEBUTTONDOWN, then use // to get the floor division
            clicked_row = int(mouseY // board.cell_size)
            clicked_col = int(mouseX // board.cell_size)
            # Why column is in X? -> Remember in pygame, x increases to the right, so we need to make it column
            # Why row is in Y? -> Same logic to x, y increases downwards making it y as row

            print(f"Row: {clicked_row} | Column: {clicked_col}") 

            if game.space_is_available(clicked_row, clicked_col):
                game.mark_move(clicked_row, clicked_col, player)
                if player == 1:
                    game.check_win(player)
                    player = 2
                else:
                    game.check_win(player)
                    player = 1

    screen.fill(constants.BACKGROUND_COLOR)
    board.draw(screen)
    board.draw_figures(screen)
    board.draw_win_line(screen)
    pygame.display.update()



    # Control frame rate
    clock.tick(60)