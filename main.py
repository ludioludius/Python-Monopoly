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

# State flags that determine which players turn it is
game_board.player1.turn = True
game_board.player2.turn = False

# Flags that detect double rolls
first_double_roll_flag = False
second_double_roll_flag = False


# moves the player passed in by updating player.position and logs move details in player class
def roll_and_move(player):
    roll1 = randrange(1, 6, 1)
    roll2 = randrange(1, 6, 1)
    roll = roll1 + roll2
    player.roll = roll
    player.position = (player.position + roll) % 40
    player.position_memory.append(player.position)
    player.roll_memory.append((roll1, roll2))
    player.check_pass_go()

    if roll1 == roll2:
        print(player.name, "rolled a double:", (roll1, roll2), "and landed on", game_board.slots[player.position].name)
        return True
    else:
        print(player.name, "rolled:", (roll1, roll2), "and landed on", game_board.slots[player.position].name)
    return False

# Method that all classes implement that dictates what can be done when landed on that slot
def display_option():
    if game_board.player1.turn:
        game_board.slots[game_board.player1.position].land_action(game_board)
    else:
        game_board.slots[game_board.player2.position].land_action(game_board)

# Flips player turn state
def change_turn():
    game_board.player1.turn = not game_board.player1.turn
    game_board.player2.turn = not game_board.player2.turn


def pre_roll_summary():
    if game_board.player1.turn:
        print(game_board.player1.name, "has $", game_board.player1.cash)
        print(game_board.player1.name, "owns the following slots: \n")
        game_board.player1.list_owned_slots()
    else:
        print(game_board.player2.name, "has $", game_board.player2.cash)
        print(game_board.player2.name, "owns the following slots: \n")
        game_board.player2.list_owned_slots()


def jail_options_helper_1(player):

    cont = True
    while cont:
        print("You are in Jail", player.jail_turn_counter, "enter 1 to attempt to roll a double,"
                                                           "enter 2 to pay $50 and be free:")
        x = input()
        if x == 1:
            cont = False
            roll1 = randrange(1, 6, 1)
            roll2 = randrange(1, 6, 1)
            if roll1 == roll2:
                player.update_position(roll1 + roll2)
                player.un_jail()
        elif x == 2:
            cont = False
            player.withdraw(50)
            roll1 = randrange(1, 6, 1)
            roll2 = randrange(1, 6, 1)
            player.update_position(roll1 + roll2)

def jail_options_helper_2(player):
    cont = True
    while cont:
        print("You are in Jail", player.jail_turn_counter, "enter 1 to attempt to roll a double:")
        x = input()
        if x == 1:
            cont = False
            roll1 = randrange(1, 6, 1)
            roll2 = randrange(1, 6, 1)
            if roll1 == roll2:
                player.update_position(roll1 + roll2)
                player.un_jail()
            else:
                player.withdraw(50)
                player.update_position(roll1 + roll2)
                player.un_jail()

def return_goojf_to_deck(deck):
    if deck == "community":
        game_board.slot2.community_chest_card_ids.insert(0, 4)
    if deck == "chance":
        game_board.slot2.chance_card_ids.insert(0, 8)





# If it is players turn, but player is in jail
# gives player variable options depending on how long player has been in jail
# TODO: allow player to use get out of jail free card(non-zero goojf attribute in player) DONE
def jail_options(player):
    player.jail_turn_counter += 1

    # Buying and selling gofg cards not implemented yet

    # TODO: return goojf card to the deck
    if player.num_of_community_GOOJF_cards >= 1:
        x = int(input("would you like to use your Get out Of Jail Free card(community): Enter 1 to use, enter 2 otherwise"))
        if x == 1:
            player.unjail()
            player.num_of_community_GOOJF_cards -= 1
            return_goojf_to_deck("community")
    elif player.num_of_chance_GOOJF_cards >= 1:
        x = int(input("would you like to use your Get out Of Jail Free card(chance): Enter 1 to use, enter 2 otherwise"))
        if x == 1:
            player.unjail()
            player.num_of_chance_GOOJF_cards -= 1
            return_goojf_to_deck("chance")
    elif player.jail_turn_counter == 1:
        jail_options_helper_1(player)
    elif game_board.player1.jail_turn_counter == 2:
        jail_options_helper_1(player)
    elif game_board.player1.jail_turn_counter == 3:
        jail_options_helper_2(player) # offer try rolling a double



# Main Game Loop
running = True
while running:

    # TODO: add bankrupcy check to end game loop/ implement money cant go below zero constraing on methods that spend money
    # TODO: add pre-move menu to view summary and make options // CHECK GAME RULES
    # TODO: implement check pass go function //DONE
    # TODO: implement full dice roll functionality //ALMOST DONE WAITING ON FULL BOARD FUNCTIONALITY


    player = game_board.get_current_player()

    # TODO: Needs to change turns depending on what happens in the jail menu  DONE
    if player.is_in_jail:
        jail_options(player)
        if player.is_in_jail:
            change_turn()
        # BUG detected: not changing turns if player still in jail


    # handles double roll functionality:
    # 1 double roll -> get another roll
    # 2nd double roll -> get onother roll
    # 3rd roll -> if double go to jail
    if first_double_roll_flag and (not second_double_roll_flag):
        second_double_roll_flag = roll_and_move(player)  # 1st extra move
        first_double_roll_flag = second_double_roll_flag  # resets to baseline if second roll isnt double
    elif first_double_roll_flag and second_double_roll_flag:
        # check double roll/ conditional move to jail
        roll1 = randrange(1, 6, 1)
        roll2 = randrange(1, 6, 1)
        if roll1 == roll2:
            player.jail()  # set player position to jail, initialize player jail state
            first_double_roll_flag = False
            second_double_roll_flag = False
        else:
            player.update_position(roll1 + roll2)
            print(player.name, "rolled:", (roll1, roll2), "and landed on", game_board.slots[player.position].name)
            first_double_roll_flag = False
            second_double_roll_flag = False
    else:
        first_double_roll_flag = roll_and_move(player)
        # BUG detected and solved (didnt consider edge case)
        # Bug documentation:
        # if you double roll and the postion you land on gets you to jail,
        # first double roll flag remain true and turn isnt changed when curr player is jailed

    display_option()

    # Bug edge case handling
    if player.is_in_jail:
        first_double_roll_flag = False
        second_double_roll_flag = False


    # code to end game if bankrupcy detected
    if game_board.player1.is_bankrupt:
        print(game_board.player1.name, " is bankrupt", game_board.player2.name, "wins")
        break
    elif game_board.player2.is_bankrupt:
        print(game_board.player2.name, " is bankrupt", game_board.player1.name, "wins")
        break

    if game_board.player1.cash < 0:
        winner = game_board.player2.name
        running = False
    elif game_board.player2.cash < 0:
        winner = game_board.player1.name
        running = False

    if (not first_double_roll_flag) and (not second_double_roll_flag):
        change_turn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((255, 3, 55))
    pygame.display.update()

print(winner.name, "wins")
