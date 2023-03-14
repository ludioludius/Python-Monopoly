class Player:

    def __init__(self, num, name):
        self.name = name
        self.player_num = num
        self.position = 0
        self.turn = False
        self.cash = 1500
        self.is_bankrupt = False
        self.roll = 0
        self.is_in_jail = False
        self.jail_turn_counter = 0
        self.num_of_community_GOOJF_cards = 0
        self.num_of_chance_GOOJF_cards = 0

        self.roll_memory = []
        self.position_memory = []

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

    def deposit(self, amount):
        self.cash += amount

    # DOESNT WORK WHEN MOVING BACKWARDS
    def check_pass_go(self):
        if len(self.position_memory) >= 2:
            if self.position_memory[-1] < self.position_memory[-2]:
                self.cash += 200
                print(self.name, "receives $200 for passing Go")

    def jail(self):
        self.move(10)
        self.jail_turn_counter = 0
        self.is_in_jail = True

    def unjail(self):
        self.jail_turn_counter = 0
        self.is_in_jail = False

    def move(self, slot_number_moved_to):
        self.position = slot_number_moved_to
        self.position_memory.append(slot_number_moved_to)















