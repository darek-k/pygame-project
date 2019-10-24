import sys

import pygame

from main import inventory_window, button_maker, clock, FPS, game_over_window, inventory
from player import PlayerEquipment


class Player:
    def __init__(self, name, strength, speed, dexterity, intelligence, charisma):

        self.name = name

        self.strength = strength
        self.speed = speed
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.charisma = charisma

        self.attack = 1
        self.defence = 1

        self.food = 70
        self.drink = 70
        self.stamina = 70
        self.health = 70

        self.exp = 40
        self.exp_to_next_level = 50
        self.level = 1
        self.leveled_up = 0

    def level_up(self):
        print('LEVELED UP!!!')
        self.level += 1
        self.exp_to_next_level += self.exp + 20
        self.leveled_up += 1

    def update_attributes(self):
        #######   Z tych dwóch linii zrób jedną ###########################
        # self.attack += PlayerEquipment().equipped_weapon_attribute
        self.attack = 1 + PlayerEquipment().equipped_weapon_attribute
        self.attack = round(self.attack, 1)

        self.defence = 1 + (PlayerEquipment().equipped_torso_attribute + PlayerEquipment().equipped_legs_attribute)
        self.defence = round(self.defence, 1)

    def reset_attributes(self, type):
        if type == 'weapon':
            PlayerEquipment().equipped_weapon_name = ''
            self.attack = 1
        elif type == 'torso':
            PlayerEquipment().equipped_torso_name = ''
        elif type == 'legs':
            PlayerEquipment().equipped_legs_name = ''

    def food_and_drink(self):
        if self.food < 0:
            self.health -= 5
            self.food = 0
        if self.drink < 0:
            self.health -= 10
            self.drink = 0
        if self.health <= 0:
            game_over_window.open_game_over_window()

    def use_item(self, index, type, attribute):  ######## Przenieś tę metodę do klasy PlayerEquipment ##########
        item_index = list(inventory.sorted_inventory)[index]
        items_names = []

        for item in inventory.inventory:  # create a list of items names
            items_names.append(item.name)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    inventory_window.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # YES - Use Item
                    button = pygame.Rect(225, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            inventory.inventory.remove(item_index)  # Remove Item from inventory.inventory[]
                            items_names.remove(item_index.name)  # Remove Item from items_names[]

                            if type == 'food':
                                self.food += (attribute * 10)
                                if self.food > 100:
                                    self.food = 100
                            elif type == 'drink':
                                self.drink += (attribute * 10)
                                if self.drink > 100:
                                    self.drink = 100
                            elif type == 'stamina':
                                self.stamina += (attribute * 10)
                                if self.stamina > 100:
                                    self.stamina = 100
                            elif type == 'health':
                                self.health += (attribute * 10)
                                if self.health > 100:
                                    self.health = 100

                            inventory_window.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # NO - Don't use Item
                    button = pygame.Rect(400, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            inventory_window.open_inventory_window()

            # Window settings
            pygame.display.set_caption('Use item?')
            ###### Niech się pyta o konkretny przedmiot ############
            button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to USE this item?', 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(225, 300, 175, 50, 'green', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                         transparent_off=False)
            button_maker(400, 300, 175, 50, 'red', 'blue', '', 30, '           NO', 'white', transparent_on=False,
                         transparent_off=False)

            pygame.display.update()
            clock.tick(FPS)
