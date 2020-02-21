
# create a Player
import random

from end_windows import GameOverWindow
from player import player1_equipment


class Player:
    def __init__(self):

        self.strength = 0
        self.speed = 0
        self.dexterity = 0
        self.intelligence = 0
        self.charisma = 0

        self.attack = 1 + (self.strength / 2)
        self.defence = 1

        self.food = 0
        self.drink = 0
        self.stamina = 0
        self.health = 0

        self.exp = 0
        self.exp_to_next_level = 50
        self.level = 1
        self.leveled_up = 0

    def random_statistics(self):
        needs = [0,0]
        stats = [0,0]

        while sum(needs) < 200 or sum(needs) > 400:
            self.food = random.randrange(50, 100)
            self.drink = random.randrange(50, 100)
            self.stamina = random.randrange(50, 100)
            self.health = random.randrange(50, 100)
            needs = (self.food, self.drink, self.stamina, self.health)

        while sum(stats) < 20 or sum(stats) > 30:
            self.strength = random.randrange(1, 7)
            self.speed = random.randrange(1, 7)
            self.dexterity = random.randrange(1, 7)
            self.intelligence = random.randrange(1, 7)
            self.charisma = random.randrange(1, 7)
            stats = (self.strength, self.speed, self.dexterity, self.intelligence, self.charisma)

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

player1 = Player()