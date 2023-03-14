from Player import Player
from NonOwnableTypes import *
from OwnableTypes import *


class Board:
    # attributes:
    # - slots
    # - player1
    # - player2

    slot0 = Go("Go", 0)
    slot1 = BrownProperty("Mediterranean Avenue", 60, 30, 2, 10, 30, 90, 160, 250, 1)
    slot2 = CommunityChest("Community Chest", 2)
    slot3 = BrownProperty("Baltic Avenue", 60, 30, 4, 20, 60, 180, 320, 450, 3)
    slot4 = Tax("Income Tax", 200, 4)
    slot5 = Railroad("Reading Railroad", 5)
    slot6 = LightBlueProperty("Oriental Avenue", 100, 50, 6, 30, 90, 270, 400, 550, 6)
    slot7 = Chance("Chance Card", 7)
    slot8 = LightBlueProperty("Vermont Avenue", 100, 50, 6, 30, 90, 270, 400, 550, 8)
    slot9 = LightBlueProperty("Connecticut Avenue", 120, 60, 8, 40, 100, 300, 450, 600, 9)
    slot10 = Nothing("Jail", 10)
    slot11 = PinkProperty("St.Charles Place", 140, 70, 10, 50, 150, 450, 625, 750, 11)
    slot12 = Utility("Electric Company", 12)
    slot13 = PinkProperty("States Avenue", 140, 70, 10, 50, 150, 450, 625, 750, 13)
    slot14 = PinkProperty("Virgina Avenue", 160, 80, 12, 60, 180, 500, 700, 900, 14)
    slot15 = Railroad("Pennsylvania Railroad", 15)
    slot16 = OrangeProperty("ST. James Place", 180, 90, 14, 70, 200, 550, 750, 950, 16)
    slot17 = CommunityChest("Community Chest", 17)
    slot18 = OrangeProperty("Tennessee Avenue", 180, 90, 14, 70, 200, 550, 750, 950, 18)
    slot19 = OrangeProperty("New York Avenue", 200, 100, 16, 80, 220, 600, 800, 1000, 19)
    slot20 = Nothing("Free Parking", 20)
    slot21 = RedProperty("Kentucky Avenue", 220, 110, 18, 90, 250, 700, 875, 1050, 21)
    slot22 = Chance("Chance", 22)
    slot23 = RedProperty("Indiana Avenue", 220, 110, 18, 90, 250, 700, 875, 1050, 23)
    slot24 = RedProperty("Illinois Avenue", 240, 120, 20, 100, 300, 750, 925, 1100, 24)
    slot25 = Railroad("B&O Railroad", 25)
    slot26 = YellowProperty("Atlantic Avenue", 260, 130, 22, 110, 330, 800, 975, 1150, 26)
    slot27 = YellowProperty("Ventnor Avenue", 260, 130, 22, 110, 330, 800, 975, 1150, 27)
    slot28 = Utility("Water Works", 28)
    slot29 = YellowProperty("Marvin Gardens", 280, 140, 24, 120, 360, 850, 1025, 1200, 29)
    slot30 = GoToJail("Go To Jail", 30)
    slot31 = GreenProperty("Pacific Avenue", 300, 150, 26, 130, 390, 900, 1100, 1275, 31)
    slot32 = GreenProperty("North Carolina Avenue", 300, 150, 26, 130, 390, 900, 1100, 1275, 32)
    slot33 = CommunityChest("Community Chest", 33)
    slot34 = GreenProperty("Pennsylvania Avenue", 320, 160, 28, 150, 450, 1000, 1200, 1400, 34)
    slot35 = Railroad("Short Line", 35)
    slot36 = Chance("Chance", 36)
    slot37 = BlueProperty("Park Place", 350, 175, 35, 175, 500, 1100, 1300, 1500, 37)
    slot38 = Tax("Luxury Tax", 100, 38)
    slot39 = BlueProperty("Boardwalk", 400, 200, 50, 200, 600, 1400, 1700, 2000, 39)

    slots = [slot0, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13,
             slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, slot26,
             slot27, slot28, slot29, slot30, slot31, slot32, slot33, slot34, slot35, slot36, slot37, slot38, slot39]

    def __init__(self):
        name1 = input("Enter player 1 name: ")
        self.player1 = Player(1, name1)
        name2 = input("Enter player 2 name: ")
        self.player2 = Player(2, name2)

    def determine_turn(self):

        if self.player1.turn:
            return 1
        if self.player2.turn:
            return 2

    def get_current_player(self):
        if self.player1.turn:
            return self.player1
        if self.player2.turn:
            return self.player2

    def get_other_player(self):
        if self.player1.turn:
            return self.player2
        if self.player2.turn:
            return self.player1

    # TODO: Slot ownership and slot state and player cash value summary function
    #TODO: start auctionianing at zero

    # includes bankrupcy setting, need to include mortgaging capability
    def auction(self, auction_property):
        bid_value = auction_property.purchase_value

        ongoing = True
        player1_winning = False
        player2_winning = False
        player1_increased_bid = False
        player2_increased_bid = False
        while ongoing:
            # player 2 bidding
            if self.determine_turn() == 1:
                print("current bid value:", bid_value)
                player2_input = input("Player 2 Enter New Bid:")
                int(player2_input)
                if int(player2_input) > bid_value:
                    bid_value = int(player2_input)
                    player2_winning = True
                    player1_winning = False
                    print("current bid value:", bid_value)
                    player1_input = input("Player 1 Enter New Bid:")
                    int(player1_input)
                    if int(player1_input) > bid_value:
                        bid_value = int(player1_input)
                        player1_winning = True
                        player2_winning = False
                        player1_increased_bid = True
                        # bidding continues, code loops
                    else:
                        ongoing = False
                        print("Player 2 wins the auction and will purchase the property for", bid_value)
                        if self.player2.cash >= bid_value:
                            self.player2.cash = self.player2.cash - bid_value
                            auction_property.owner = 2  # potential bug to talk about
                        else:
                            self.player2.cash = self.player2.cash - bid_value
                            self.player2.is_bankrupt = True

                else:  # player 1 either buys the property or not depending on if player 1 increased the bid
                    ongoing = False
                    if player1_increased_bid:
                        # set owner to player 1
                        if self.player1.cash >= bid_value:
                            self.player1.cash = self.player1.cash - bid_value  # potential bug to talk about
                            auction_property.owner = 1
                        else:
                            self.player1.cash = self.player1.cash - bid_value
                            self.player2.is_bankrupt = True

            else:
                print("current bid value:", bid_value)
                player1_input = input("Player 1 Enter New Bid:")
                int(player1_input)
                if int(player1_input) > bid_value:
                    bid_value = int(player1_input)
                    player1_winning = True
                    player2_winning = False
                    print("current bid value:", bid_value)
                    player2_input = input("Player 2 Enter New Bid:")
                    int(player2_input)
                    if int(player2_input) > bid_value:
                        bid_value = int(player2_input)
                        player2_winning = True
                        player1_winning = False
                        player2_increased_bid = True
                        # bidding continues, code loops
                    else:
                        ongoing = False
                        print("Player 1 wins the auction and will purchase the property for", bid_value)
                        if self.player1.cash >= bid_value:
                            self.player1.cash = self.player1.cash - bid_value
                            auction_property.owner = 1  # potential bug to talk about
                        else:
                            self.player1.cash = self.player1.cash - bid_value
                            self.player1.is_bankrupt = True

                else:  # player 2 either buys the property or not depending on if player 1 increased the bid
                    ongoing = False
                    if player2_increased_bid:
                        # set owner to player 2

                        if self.player2.cash >= bid_value:
                            self.player2.cash = self.player2.cash - bid_value  # potential bug to talk about
                            auction_property.owner = 2
                        else:
                            self.player2.cash = self.player2.cash - bid_value
                            self.player2.is_bankrupt = True
