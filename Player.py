class Player:

    def __init__(self, num, name):
        self.name = name
        self.player_num = num
        self.position = 0
        self.turn = False
        self.cash = 1500
        self.is_bankrupt = False
        self.roll = 0

        self.rails_owned = []
        self.utilities_owned = []
        self.brown_owned = []
        self.light_blue_owned = []
        self.pink_owned = []
        self.orange_owned = []
        self.red_owned = []
        self.yellow_owned = []
        self.green_owned = []
        self.blue_owned = []

    def update_position(self, roll):
        self.position = (self.position + roll) % 40

    def withdraw(self, amount):
        self.cash = self.cash - amount
        if self.cash < 0:
            self.is_bankrupt = True









