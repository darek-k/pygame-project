
# create a Player
from end_windows import GameOverWindow
from player import player1_equipment


class Player:
    def __init__(self, name, strength, speed, dexterity, intelligence, charisma):

        self.name = name

        self.strength = strength
        self.speed = speed
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.charisma = charisma

        self.attack = 100 + (self.strength / 2)
        self.defence = 1

        self.food = 10
        self.drink = 10
        self.stamina = 10
        self.health = 1000

        self.exp = 0
        self.exp_to_next_level = 50
        self.level = 1
        self.leveled_up = 0

    def level_up(self):
        self.level += 1
        self.exp_to_next_level += self.exp + 20
        self.leveled_up += 1

    def update_attributes(self):
        self.attack = round(1 + player1_equipment.equipped_weapon_attribute + (self.strength / 2), 1)

        self.defence = round(1 + (player1_equipment.equipped_torso_attribute
                                  + player1_equipment.equipped_legs_attribute), 1)

    def reset_attributes(self, type):
        if type == 'weapon':
            player1_equipment.equipped_weapon_name = ''
        elif type == 'torso':
            player1_equipment.equipped_torso_name = ''
        elif type == 'legs':
            player1_equipment.equipped_legs_name = ''

    def food_and_drink(self):
        if self.food < 0:
            self.health -= 5
            self.food = 0
        if self.drink < 0:
            self.health -= 10
            self.drink = 0
        if self.stamina < 0:
            self.health -= 10
            self.stamina = 0
        if self.health <= 0:
            GameOverWindow().open_game_over_window()

player1 = Player('John', 5, 5, 5, 5, 5)