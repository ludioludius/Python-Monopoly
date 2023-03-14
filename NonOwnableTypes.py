import Board
import random

def offer_purchase(game_board, slot_num):
    print(game_board.slots[slot_num].slot_id, game_board.slots[slot_num].name)
    x = input("Property available for purchase; you may purchase this property")
    if x == "purchase":
        if game_board.get_current_player().cash >= game_board.slots[slot_num].purchase_value:
            game_board.slots[slot_num].owner = game_board.determine_turn()  # sets property owner
            game_board.get_current_player().utilities_owned.append(game_board.slots[slot_num])
            print("you bought this property")
        else:
            print("you dont have enough cash")  # need to implement mortgaging functionality

def fine_player_utility(game_board):
    roll1 = random.randrange(1, 6, 1)
    roll2 = random.randrange(1, 6, 1)
    fine_amount = (roll2 + roll1) * 10
    print("You were fined: $", fine_amount)
    game_board.get_current_player().withdraw(fine_amount)

def fine_player_railroad(game_board):
    num_rails_owned = len(game_board.get_other_player().rails_owned)

    if num_rails_owned == 1:
        rent = 25
    elif num_rails_owned == 2:
        rent = 50
    elif num_rails_owned == 3:
        rent = 100
    else:
        rent = 200
    rent = rent * 2
    print("You must pay $", rent, "double the normal rent")
    game_board.get_current_player().withdraw(rent)


class Go:
    bonus_value = 200

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):

        if game_board.determine_turn() == 1:
            x = input("player 1 gets 200 dollars; press enter to continue")
        if game_board.determine_turn() == 2:
            x = input("player 2 gets 200 dollars; press enter to continue")


class Tax:

    def __init__(self, name, tax_value, slot_id):
        self.name = name
        self.slot_id = slot_id
        self.tax_value = tax_value

    def land_action(self, game_board):
        if self.name == "Income Tax":
            if game_board.determine_turn() == 1:
                x = input("player 1 lost 200 dollars to income tax; press enter to continue")
                game_board.player1.cash = game_board.player1.cash - 200
            if game_board.determine_turn() == 2:
                x = input("player 2 lost 200 dollars to income tax; press enter to continue")
                game_board.player2.cash = game_board.player2.cash - 200
        elif self.name == "Luxury Tax":
            if game_board.determine_turn() == 1:
                x = input("player 1 lost 100 dollars to luxury tax; press enter to continue")
                game_board.player1.cash = game_board.player1.cash - 100
            if game_board.determine_turn() == 2:
                x = input("player 2 lost 100 dollars to luxury tax; press enter to continue")
                game_board.player2.cash = game_board.player2.cash - 100


class Nothing:

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):
        x = input("Not yet implemented; press enter to continue")


class GoToJail:

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):
        x = input("You must go to Jail; press enter to continue")
        # implement send to jail method in player class
        game_board.get_current_player().jail()


def draw_card(game_board, num):
    if num == 0:
        print("Advance to go and collect $200")
        game_board.get_current_player().position = 0
        game_board.get_current_player().deposit(200)
    elif num == 1:
        print("Bank error in your favor. Collect $200")
        game_board.get_current_player().deposit(200)
    elif num == 2:
        print("Doctor’s fee. Pay $50")
        game_board.get_current_player().withdraw(50)
    elif num == 3:
        print("From sale of stock you get $50")
        game_board.get_current_player().deposit(50)
    elif num == 4:
        print("Get Out Of Jail Free")
        game_board.get_current_player().num_of_community_GOOJF_cards += 1
    elif num == 5:
        print("Go to Jail. Go directly to jail, do not pass Go, do not collect $200")
        game_board.get_current_player().jail()
    elif num == 6:
        print("Grand Opera Night. Collect $50 from every player for opening night seats.")
        game_board.get_other_player().withdraw(50)
        game_board.get_current_player().deposit(50)
    elif num == 7:
        print("Holiday fund matures. Receive $100")
        game_board.get_current_player().deposit(100)
    elif num == 8:
        print("Income tax refund. Collect $20")
        game_board.get_current_player().deposit(20)
    elif num == 9:
        print("It is your birthday. Collect $10 from every player")
        game_board.get_other_player().withdraw(10)
        game_board.get_current_player().deposit(10)
    elif num == 10:
        print("Life insurance matures. Collect $100")
        game_board.get_current_player().deposit(100)
    elif num == 11:
        print("Pay hospital fees of $100")
        game_board.get_current_player().withdraw(100)
    elif num == 12:
        print("Pay school fees of $50")
        game_board.get_current_player().withdraw(50)
    elif num == 13:
        print("Receive $25 consultancy fee")
        game_board.get_current_player().deposit(25)
    elif num == 14:
        print("You are assessed for street repair. $40 per house. $115 per hotel")
        # TODO needs new method in player class
    elif num == 15:
        print("You have won second prize in a beauty contest. Collect $10")
        game_board.get_current_player().deposit(10)
    elif num == 16:
        print("You inherit $100")
        game_board.get_current_player().deposit(100)


class CommunityChest:
    # array of length 16 with randomized community card ids (Deck of cards)
    community_chest_card_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    random.shuffle(community_chest_card_ids)

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):
        num = self.community_chest_card_ids.pop(len(self.community_chest_card_ids) - 1)
        draw_card(game_board, num)
        if num != 4:  # not a goojf card
            self.community_chest_card_ids.insert(0, num)
        else:
            game_board.get_current_player().num_of_community_GOOJF_cards += 1

def draw_card_chance(game_board, num):
    if num == 0:
        print("Advance to go and collect $200")
        game_board.get_current_player().move(0)
        game_board.get_current_player().check_pass_go()
    elif num == 1:
        print("Advance to Illinois Ave. If you pass Go, collect $200.")
        game_board.get_current_player().move(24)
        game_board.get_current_player().check_pass_go()
    elif num == 2:
        print("Advance to St. Charles Place. If you pass Go, collect $200.")
        game_board.get_current_player().move(11)
        game_board.get_current_player().check_pass_go()
    elif num == 3:
        # Advance to the nearest utility
        curr_pos = game_board.get_current_player().position
        if curr_pos == 22 or curr_pos == 36:
            # Should probably refactor this to make it neater
            game_board.get_current_player().move(28)
            if game_board.determine_turn() == game_board.slot28.owner:
                print("you landed on your Utility")
            elif game_board.slot28.owner == 0:
                offer_purchase(game_board, 28)
            else:
                fine_player_utility(game_board)
        elif curr_pos == 7:
            game_board.get_current_player().move(12)
            if game_board.determine_turn() == game_board.slot12.owner:
                print("you landed on your Utility")
            elif game_board.slot12.owner == 0:
                offer_purchase(game_board, 12)
            else:
                fine_player_utility(game_board)
        else:
            print("ERROR IN CODE")
    elif num == 4:
        # Advance to the nearest railroad
        curr_pos = game_board.get_current_player().position
        # Should probably refactor this to make it neater
        if curr_pos == 7:
            game_board.get_current_player().move(5)
            if game_board.determine_turn() == game_board.slot5.owner:
                print("you landed on your Railroad")
            elif game_board.slot5.owner == 0:
                offer_purchase(game_board, 5)
            else:
                fine_player_railroad(game_board)
        elif curr_pos == 22:
            game_board.get_current_player().move(25)
            if game_board.determine_turn() == game_board.slot25.owner:
                print("you landed on your Railroad")
            elif game_board.slot25.owner == 0:
                offer_purchase(game_board, 25)
            else:
                fine_player_railroad(game_board)
        elif curr_pos == 36:
            game_board.get_current_player().move(35)
            if game_board.determine_turn() == game_board.slot35.owner:
                print("you landed on your Railroad")
            elif game_board.slot35.owner == 0:
                offer_purchase(game_board, 35)
            else:
                fine_player_railroad(game_board)
        else:
            print("ERROR IN CODE")
    elif num == 5:
        print("Bank pays you a dividend of $50")
        game_board.get_current_player().deposit(50)
    elif num == 6:
        print("Get Out Of Jail Free")
        game_board.get_current_player().num_of_chance_GOOJF_cards += 1
    elif num == 7:
        curr_pos = game_board.get_current_player().position
        curr_pos = curr_pos - 3
        game_board.slots[curr_pos].land_action()
    elif num == 8:
        print("Go to Jail. Go directly to jail, do not pass Go, do not collect $200")
        game_board.get_current_player().jail()
    elif num == 9:
        print("NOT IMPLEMENTD YET")
        # needs new method to calculate total property owned
    elif num == 10:
        print("Advance to Reading Railroad")
        game_board.get_current_player().move(5)
        game_board.get_current_player().check_pass_go() # always passes go
        game_board.slots[5].land_action()
    elif num == 11:
        print("Advance to Boardwalk")
        game_board.get_current_player().move(39)
        game_board.get_current_player().check_pass_go() # never passes go
        game_board.slots[39].land_action()
    elif num == 12:
        print("You have been elected chairman of the board. Pay each player $50")
        game_board.get_current_player().withdraw(50)
        game_board.get_other_player().deposit(50)
    elif num == 13:
        print("Your building load matters. Reveive $150")
        game_board.get_current_player().deposit(150)

class Chance:
    # array of length 16 with randomized chance card ids (Deck of cards)
    chance_card_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    random.shuffle(chance_card_ids)

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):
        num = self.chance_card_ids.pop(len(self.chance_card_ids) - 1)
        draw_card_chance(game_board, num)
        if num != 8:  # not a goojf card
            self.chance_card_ids.insert(0, num)
        else:
            game_board.get_current_player().num_of_community_GOOJF_cards += 1
