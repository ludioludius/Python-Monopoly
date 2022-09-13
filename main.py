from random import randrange

import pygame
import os
from Board import Board

pygame.init()

# creates the screen
screen = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Monopoly")

game_board = Board()
print(game_board.player1.position)

BOARD_IMAGE = pygame.image.load(os.path.join('Assets', 'img_1.png'))
Board = pygame.transform.scale(BOARD_IMAGE, (800, 800))

screen.blit(Board, (0, 0))
pygame.display.update()

# code that draws the board

game_board.player1.turn = True
game_board.player2.turn = False


# moves the player passed in
def roll_and_move(player):
    roll = randrange(2, 12, 1)
    player.roll = roll
    player.position = (player.position + roll) % 40
    print(player.name, "rolled an", roll, "and landed on", game_board.slots[player.position].name)



def display_option():
    if game_board.player1.turn:
        game_board.slots[game_board.player1.position].land_action(game_board)
    else:
        game_board.slots[game_board.player2.position].land_action(game_board)


def change_turn():
    game_board.player1.turn = not game_board.player1.turn
    game_board.player2.turn = not game_board.player2.turn





running = True
while running:

    #TODO: add bankrupcy check to end game loop
    #TODO: add pre-move menu to view summary
    #TODO: implement check pass go function


    # default functions before rolling like player summary and purchases before re-rolling etc/ post_landing_options

    if game_board.determine_turn() == 1:

        roll_and_move(game_board.player1)
        # checkpassgo() method to check if current positon < previous position and not equal 0
    else:
        roll_and_move(game_board.player2)

    display_option()

    change_turn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((255, 3, 55))
    pygame.display.update()
