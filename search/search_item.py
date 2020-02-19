import random
import time

import pygame

from create import button_maker, writing_text, get_random_number
from inventory import inventory
from items import Item
from player import player1

# create weapon instances
stone = Item('Stone', 2, 'weapon', '')
rod = Item('Rod', 3, 'weapon', '')
bat = Item('Bat', 4, 'weapon', '')
oar = Item('Oar', 5, 'weapon', '')
hammer = Item('Hammer', 6, 'weapon', '')
knife = Item('Knife', 7, 'weapon', '')
axe = Item('Axe', 8, 'weapon', '')

# create torso instances
shirt = Item('Shirt', 2, 'torso', '')
vest = Item('Vest', 4, 'torso', '')
jacket = Item('Jacket', 7, 'torso', '')
armor = Item('Armor', 10, 'torso', '')

# create legs instances
sweatpants = Item('Sweatpants', 3, 'legs', '')
jeans = Item('Jeans', 5, 'legs', '')
fishing_trouser = Item('Fishing ts.', 7, 'legs', '')
military_trousers = Item('Military ts.', 9, 'legs', '')

# create food instances
insect = Item('Apple', 2, 'food', '')
dog_food = Item('Potato', 4, 'food', '')
rat = Item('Dog Food', 5, 'food', '')
fish = Item('Rat', 6, 'food', '')
canned_food = Item('Raw fish', 7, 'food', '')

# create drink instances
soda = Item('Soda', 3, 'drink', '')
juice = Item('Soda', 5, 'drink', '')
water = Item('Water', 7, 'drink', '')

# create health instances
vodka = Item('Vodka', 2, 'health', '')
painkillers = Item('Painkillers', 3, 'health', '')
bandage = Item('Bandage', 6, 'health', '')

# create stamina instances
energy_drink = Item('Energy Drink', 2, 'stamina', '')
coffee = Item('Coffee', 3, 'stamina', '')
cocaine = Item('Cocaine', 5, 'stamina', '')

# create other instances
board = Item('Board', '', 'other', '')
key = Item('Key', '', 'other', '')


class SearchItem:
    """ Itemsy dodane są po to, żeby mieć wszystkie itemy w jednym miejscu, gdybym chciał pozmieniać coś """
    itemsy = [stone, rod, bat, oar, hammer, knife, axe, shirt, vest, jacket, armor, sweatpants, jeans,
              fishing_trouser, military_trousers, insect, rat, fish, dog_food, canned_food, soda, juice, water,
              vodka, painkillers, bandage, energy_drink, coffee, cocaine, board, key]

    def __init__(self):

        self.chest_black_pearl = [rod, bat, oar, hammer, axe, shirt, vest, jacket, sweatpants, jeans, fishing_trouser,
                                  military_trousers, rat, fish, canned_food, insect, soda, juice, water, vodka,
                                  bandage, energy_drink, coffee, board]
        self.random_items_black_pearl = []
        self.found_items_black_pearl = []

        self.chest_bridge = [stone, rod, bat, shirt, vest, jeans, fishing_trouser, insect, rat, fish, water, vodka,
                             cocaine, board, key]
        self.random_items_bridge = []
        self.found_items_bridge = []

        self.chest_crane = [stone, rod, bat, hammer, axe, shirt, armor, jeans, military_trousers, insect, rat,
                            fish, canned_food, soda, juice, water, vodka, painkillers, bandage, board, key]
        self.random_items_crane = []
        self.found_items_crane = []

        self.chest_flat = [bat, hammer, knife, shirt, vest, jacket, sweatpants, jeans, insect, rat, canned_food,
                           dog_food, soda, juice, water, vodka, painkillers, bandage, energy_drink, coffee, cocaine,
                           board, key]
        self.random_items_flat = []
        self.found_items_flat = []

        self.chest_forest = [stone, axe, vest, military_trousers, insect, rat, canned_food, water, vodka, bandage,
                             cocaine, board, key]
        self.random_items_forest = []
        self.found_items_forest = []

        self.chest_gate = [axe, jacket, armor, military_trousers, canned_food, dog_food, juice, water,
                           vodka, painkillers, bandage, energy_drink, coffee, cocaine, board, key]
        self.random_items_gate = []
        self.found_items_gate = []

        self.chest_hotel = [hammer, knife, axe, shirt, vest, jacket, sweatpants, jeans, insect, rat, dog_food,
                            canned_food,
                            soda, juice, water, vodka, painkillers, bandage, energy_drink, coffee, cocaine, board, key]
        self.random_items_hotel = []
        self.found_items_hotel = []

        self.chest_office = [hammer, shirt, jeans, insect, rat, canned_food, soda, juice, water, painkillers, bandage,
                             energy_drink, coffee, cocaine, board, key]
        self.random_items_office = []
        self.found_items_office = []

        self.chest_opera = [rod, hammer, shirt, jeans, insect, rat, water, vodka, painkillers, bandage, energy_drink,
                            coffee, board, key]
        self.random_items_opera = []
        self.found_items_opera = []

        self.chest_restaurant = [knife, insect, rat, fish, dog_food, canned_food, soda, juice, water, vodka,
                                 painkillers, bandage, energy_drink, coffee, board, key]
        self.random_items_restaurant = []
        self.found_items_restaurant = []

        self.chest_soldek = [rod, bat, oar, hammer, axe, vest, jacket, fishing_trouser, military_trousers, insect, rat,
                             fish, canned_food, soda, juice, water, vodka, painkillers, bandage, coffee, board, key]
        self.random_items_soldek = []
        self.found_items_soldek = []

        self.chest_basilica = [stone, vest, jeans, insect, rat, fish, vodka, cocaine, board, key]
        self.random_items_basilica = []
        self.found_items_basilica = []

        self.chest_supermarket = [dog_food, canned_food, soda, juice, water, vodka, painkillers, bandage, energy_drink,
                                  coffee, cocaine, board, key]
        self.random_items_supermarket = []
        self.found_items_supermarket = []

        self.locations = (
            (self.chest_black_pearl, self.random_items_black_pearl), (self.chest_bridge, self.random_items_bridge),
            (self.chest_crane, self.random_items_crane), (self.chest_flat, self.random_items_flat),
            (self.chest_forest, self.random_items_forest), (self.chest_gate, self.random_items_gate),
            (self.chest_hotel, self.random_items_hotel), (self.chest_office, self.random_items_office),
            (self.chest_opera, self.random_items_opera), (self.chest_restaurant, self.random_items_restaurant),
            (self.chest_soldek, self.random_items_soldek), (self.chest_basilica, self.random_items_basilica),
            (self.chest_supermarket, self.random_items_supermarket),
        )

    def get_random_items(self, chest_location, random_items):
        random_number = get_random_number(1, 6)
        for i in range(random_number):
            random_index = random.randint(0, len(chest_location) - 1)
            random_items.append(chest_location[random_index])

    def search(self, random_items, found_item_location):
        try:
            random_index = random.randint(0, len(random_items) - 1)  # Searching for random items
            found_item = random_items[random_index]

            # Add items to found items and remove from the chest
            found_item_location.append(found_item)
            random_items.remove(found_item)

            player1.food -= 10
            player1.drink -= 10
            if player1.stamina > 0:
                player1.stamina -= 10
            elif player1.stamina <= 0:
                player1.stamina = 0
            player1.exp += 20
            if player1.exp >= player1.exp_to_next_level:
                player1.level_up()

            player1.food_and_drink()

        except ValueError:
            self.show_found_items(found_item_location)
            button_maker(300, 275, 200, 40, 'blue', 'blue', '', 36, "    Nothing left", 'white',
                         transparent_on=False, transparent_off=False)
            pygame.display.update()
            time.sleep(0.5)

    def add_to_inventory_while_search(self, index, found_item_location):
        if len(inventory.inventory) >= 12:
            button_maker(290, 275, 220, 40, 'blue', 'blue', '', 36, "    Full Inventory", 'white',
                         transparent_on=False, transparent_off=False)
            pygame.display.update()
            time.sleep(0.5)
        else:
            item = found_item_location[index]
            inventory.inventory.append(item)
            item_index = list(found_item_location)[index]
            found_item_location.remove(item_index)

    def show_found_items(self, found_item_location):
        x = 0
        y = 0
        for item in found_item_location:

            if item.type == 'weapon':
                text = 'Damage: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'orange', x, y + 50)

            if item.type == 'torso' or item.type == 'legs':
                text = 'Defence: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'violet', x, y + 50)

            if item.type == 'food':
                text = 'Food: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'brown', x, y + 50)

            if item.type == 'drink':
                text = 'Drink: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'blue', x, y + 50)

            if item.type == 'health':
                text = 'Health: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'green', x, y + 50)

            if item.type == 'stamina':
                text = 'Stamina: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_blue')
                writing_text('', 35, text + str(item.attribute), 'yellow', x, y + 50)

            if item.type == 'other':
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name.center(20), 'gold')

            x += 200
            if x > 600:
                x = 0
                y += 150


chest = SearchItem()
