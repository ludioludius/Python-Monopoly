import Board


class Go:
    bonus_value = 200

    def __init__(self, name, slot_id):
        self.slot_id = slot_id
        self.name = name

    def land_action(self, game_board):

        if game_board.determine_turn() == 1:
            x = input("player 1 gets 200 dollars; press enter to continue")
            game_board.player1.cash = game_board.player1.cash + 200
        if game_board.determine_turn() == 2:
            x = input("player 2 gets 200 dollars; press enter to continue")
            game_board.player2.cash = game_board.player2.cash + 200


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

