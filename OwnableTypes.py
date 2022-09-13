# need to add house and hotel functionality later
# each ownable type will have a calculate_rent method
def get_max_building_level(property_list):
    maximum_building_level = 0
    for i in property_list:
        if i.building_level > maximum_building_level:
            maximum_building_level = i.building_level
    return maximum_building_level


def get_min_building_level(property_list):
    minimum_building_level = 0
    for i in property_list:
        if i.building_level > minimum_building_level:
            minimum_building_level = i.building_level
    return minimum_building_level


def upgradable_options(maximum, minimum, property_list, game_board):
    upgradable = []
    for i in property_list:
        if i.building_level == minimum:
            upgradable.append(i)
    for i in upgradable:
        print("would you like to upgrade this property?\n")
        x = input("Type 'Y' or 'N'")
        if x == "Y":
            game_board.get_current_player().withdraw(i.building_cost)
            # change property state
            i.building_level = i.building_level + 1


class BrownProperty:

    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 50

    # caller functions handle setting curr_building_level and determining which property to upgrade
    # function
    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self, game_board):
        if game_board.get_other_player().brown_owned == 2 and self.building_level == 0:
            return self.rent_values[0] * 2
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().brown_owned.size() == 2:
            maximum_building_level = get_max_building_level(game_board.get_current_player().brown_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().brown_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().brown_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().brown_owned.append(self)  # adds property to players portfolio
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(game_board), "in rent")

    # need to check mortgage status here
    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class LightBlueProperty:

    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 50

    # caller functions handle setting curr_building_level and determining which property to upgrade
    # function
    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().light_blue_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().light_blue_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().light_blue_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().light_blue_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().light_blue_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

    # need to check mortgage status here
    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class PinkProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 100

    # caller functions handle setting curr_building_level and determining which property to upgrade
    # function
    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().pink_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().pink_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().pink_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().pink_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().pink_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

    # need to check mortgage status here
    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class OrangeProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 100

    # caller functions handle setting curr_building_level and determining which property to upgrade
    # function
    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().orange_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().orange_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().orange_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().orange_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().orange_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

    # need to check mortgage status here
    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class RedProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 100

    # caller functions handle setting curr_building_level and determining which property to upgrade
    # function
    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().orange_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().orange_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().orange_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().orange_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().orange_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

    # need to check mortgage status here
    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class YellowProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 150

        # caller functions handle setting curr_building_level and determining which property to upgrade
        # function

    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().yellow_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().yellow_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().yellow_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().yellow_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().yellow_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

        # need to check mortgage status here

    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class GreenProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 200

        # caller functions handle setting curr_building_level and determining which property to upgrade
        # function

    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().green_owned.size() == 3:
            maximum_building_level = get_max_building_level(game_board.get_current_player().green_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().green_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().green_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().green_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

        # need to check mortgage status here

    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class BlueProperty:
    def __init__(self, name, purchase_value, mortgage_value, rent0, rent1, rent2, rent3, rent4, rent_hotel,
                 slot_id):
        self.owner = 0
        self.slot_id = slot_id
        self.name = name
        self.purchase_value = purchase_value
        self.mortgage_value = mortgage_value
        self.rent_values = [rent0, rent1, rent2, rent3, rent4, rent_hotel]
        self.building_level = 0
        self.building_cost = 200

        # caller functions handle setting curr_building_level and determining which property to upgrade
        # function

    def build_property(self):
        self.building_level = self.building_level + 1

    def calculate_rent(self):
        return self.rent_values[self.building_level]

    def owned_spot(self, game_board):
        print("you have landed on your property")
        if game_board.get_current_player().blue_owned.size() == 2:
            maximum_building_level = get_max_building_level(game_board.get_current_player().blue_owned)
            minimum_building_level = get_min_building_level(game_board.get_current_player().blue_owned)
            if min != 5:
                upgradable_options(maximum_building_level, minimum_building_level,
                                   game_board.get_current_player().blue_owned, game_board)
            else:
                print("properties maxed out")

    def unowned_spot(self, game_board):
        x = input(
            "property available for purchase; you may either purchase the property or start an auction with the"
            "bank. Type 'purchase' or 'auction'")
        if x == "purchase":
            if game_board.get_current_player().cash >= self.purchase_value:
                self.owner = game_board.determine_turn()  # sets property owner
                game_board.get_current_player().orange_owned.append(self)
                print("you bought this property")
            else:
                print("you dont have enough cash")  # need to implement mortgaging functionality
        elif x == "auction":
            game_board.auction(self)

    def pay_rent_spot(self, game_board):
        x = input("pay up fool")
        game_board.get_current_player().withdraw(self.calculate_rent())
        print("you paid", self.calculate_rent(), "in rent")

        # need to check mortgage status here

    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            self.owned_spot(game_board)
        elif self.owner == 0:
            self.unowned_spot(game_board)
        else:
            self.pay_rent_spot(game_board)


class Railroad:
    purchase_value = 200
    mortgage_value = 100
    unmortgage_value = 110

    def __init__(self, name, slot_id):
        self.owner = 0
        self.name = name
        self.slot_id = slot_id

    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            print("you landed on your railroad")
        elif self.owner == 0:
            x = input(
                "railroad available for purchase; you may either purchase the railroad or start an auction with the"
                "bank. Type 'purchase' or 'auction'")
            if x == "purchase":
                if game_board.get_current_player().cash >= self.purchase_value:
                    self.owner = game_board.determine_turn()  # sets property owner
                    game_board.get_current_player().rails_owned.append(self)
                    print("you bought this railroad")
                else:
                    print("you dont have enough cash")  # need to implement mortgaging functionality
            elif x == "auction":
                game_board.auction(self)
        else:
            num_rails_owned = game_board.get_other_player().rails_owned.size

            if num_rails_owned == 1:
                rent = 25
            elif num_rails_owned == 2:
                rent = 50
            elif num_rails_owned == 3:
                rent = 100
            else:
                rent = 200


class Utility:
    purchase_value = 150
    mortgage_value = 75

    def __init__(self, name, slot_id):
        self.owner = 0
        self.name = name
        self.slot_id = slot_id

    def land_action(self, game_board):
        if game_board.determine_turn() == self.owner:
            print("you already own this utility")
        elif self.owner == 0:
            x = input(
                "utility available for purchase; you may either purchase the utility or start an auction with the"
                "bank. Type 'purchase' or 'auction'")
            if x == "purchase":
                if game_board.get_current_player().cash >= self.purchase_value:
                    self.owner = game_board.determine_turn()  # sets property owner
                    game_board.get_current_player().utilities.append(self)
                    print("you bought this utlilty")
                else:
                    print("you dont have enough cash")  # need to implement mortgaging functionality
            elif x == "auction":
                game_board.auction(self)
        else:
            num_utilities_owned = game_board.get_other_player().utilities_owned.size()
            roll_val = game_board.get_current_player.roll
            if num_utilities_owned == 2:
                rent = roll_val * 10
            else:
                rent = roll_val * 4
