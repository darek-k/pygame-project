# Initialization
import sys
import time

import pygame

from clock import clock, FPS
from create import writing_text, button_maker, colors, statistics_buttons, equipment_buttons, ItemsNamesList
from display import display
from end_windows import VictoryWindow
from inventory import inventory
from items import Item
from player import player1_equipment, player1
from search import chest
from sleep import Sleep

pygame.init()

def get_level():
    return player1.level

class SetDefence:
    def __init__(self):
        self.black_pearl_defence = 50
        self.bridge_defence = 20
        self.crane_defence = 50
        self.flat_defence = 40
        self.forest_defence = 30
        self.hotel_defence = 50
        self.office_defence = 40
        self.opera_defence = 30
        self.restaurant_defence = 20
        self.soldek_defence = 50
        self.basilica_defence = 20
        self.supermarket_defence = 10

    def set_defence(self, location_name, new_defence):
        if location_name == 'black_pearl':
            self.black_pearl_defence = new_defence
        if location_name == 'bridge':
            self.bridge_defence = new_defence
        if location_name == 'crane':
            self.crane_defence = new_defence
        if location_name == 'flat':
            self.flat_defence = new_defence
        if location_name == 'forest':
            self.forest_defence = new_defence
        if location_name == 'gate':
            self.gate_defence = new_defence
        if location_name == 'hotel':
            self.hotel_defence = new_defence
        if location_name == 'office':
            self.office_defence = new_defence
        if location_name == 'opera':
            self.opera_defence = new_defence
        if location_name == 'restaurant':
            self.restaurant_defence = new_defence
        if location_name == 'soldek':
            self.soldek_defence = new_defence
        if location_name == 'basilica':
            self.basilica_defence = new_defence
        if location_name == 'supermarket':
            self.supermarket_defence = new_defence


set_defence = SetDefence()  # Instance of Barricade class


class UpdateDefence:
    @staticmethod
    def update_defence(image, window_name, found_item_location, defence,
                       location_name):
        # Open previous window and update 'Defence'
        location_window.open_location_window(image, window_name, 'random_items', found_item_location, defence,
                                             location_name)


class OpenBarricadeWindow:
    @staticmethod
    def open_barricade_window(image, previous_window, defence, location_name, window_name,
                              found_item_location):
        # It's used in open_location_window()
        defence_on_begin = defence

        stamina_on_begin = int(player1.stamina)
        stamina = int(player1.stamina)

        food_on_begin = int(player1.food)
        food = int(player1.food)

        drink_on_begin = int(player1.drink)
        drink = int(player1.drink)

        health_on_begin = int(player1.health)
        health = int(player1.health)
        count_health = 0

        # Count number of Boards in Inventory
        boards_number_on_begin = ItemsNamesList().items_names_list().count('Board')
        boards_number = ItemsNamesList().items_names_list().count('Board')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN:  # click "+" Button
                    button = pygame.Rect(320, 100, 80, 45)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            # Change DEFENCE stat
                            if defence == 100:
                                print("DEFENCE = MAX")
                            elif defence < 100:
                                if boards_number > 0:
                                    if stamina > 5:
                                        defence += 10
                                        if defence > 100:
                                            defence = 100
                                        boards_number -= 1
                                        stamina -= 5
                                        if food > 0:
                                            food -= 5
                                        else:
                                            food = 0
                                            if health > 5:
                                                health -= 5
                                                count_health += 1
                                            else:
                                                print("Health too low") # todo change this into statement
                                        if drink > 0:
                                            drink -= 5
                                        else:
                                            drink = 0
                                            if health > 5:
                                                health -= 5
                                                count_health += 1
                                            else:
                                                print("Health too low") # todo change this into statement
                                    elif stamina <= 5:
                                        print("Stamina too low") # todo change this into statement
                                elif boards_number == 0:
                                    print("You don't have boards") # todo change this into statement

                if event.type == pygame.MOUSEBUTTONDOWN:  # click "-" Button
                    button = pygame.Rect(400, 100, 80, 45)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            if defence > defence_on_begin:
                                defence -= 10

                            if boards_number < boards_number_on_begin:
                                boards_number += 1

                            if stamina < stamina_on_begin:
                                stamina += 5

                            if food < food_on_begin:
                                food += 5

                            if drink < drink_on_begin:
                                drink += 5

                            if health < health_on_begin:
                                health += 5
                                count_health -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:  # click BARRICADE Button
                    button = pygame.Rect(305, 440, 190, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            # Remove used Boards
                            used_boards_number = boards_number_on_begin - boards_number

                            # Update statistics
                            new_defence = defence
                            player1.stamina = stamina
                            player1.health = health
                            player1.food = food
                            player1.drink = drink
                            player1.exp += used_boards_number * 10
                            if player1.exp >= player1.exp_to_next_level:
                                player1.level_up()

                            start_index = 0
                            for item in range(used_boards_number):
                                index = ItemsNamesList().items_names_list().index("Board", start_index)
                                start_index += 1
                                del inventory.inventory[index]

                            # Barricade "animation"
                            barricade_image = pygame.image.load('images/barricade.jpg')
                            display.blit(barricade_image, (0, 0))
                            pygame.display.update()
                            time.sleep(0.8)

                            set_defence.set_defence(location_name, defence)
                            return UpdateDefence().update_defence(image, window_name, found_item_location, defence,
                                                                  location_name)

            # Window settings and graphic
            pygame.display.set_caption("Barricade")
            location_image = pygame.image.load(image)
            display.blit(location_image, (0, 0))

            button_maker(330, 50, 135, 35, 'grey', 'grey', '', 35, "Barricade?", 'white',
                         transparent_on=False, transparent_off=False)  # Barricade?

            button_maker(320, 100, 80, 45, 'green', 'green', '', 40, '    +', 'white',  # +
                         transparent_on=False, transparent_off=False)
            button_maker(400, 100, 80, 45, 'red', 'red', '', 40, '     -', 'white',  # -
                         transparent_on=False, transparent_off=False)

            button_maker(310, 160, 180, 35, 'black', 'black', '', 35, 'DEFENCE = ' + str(defence), 'red',  # Defence
                         transparent_on=False, transparent_off=False)

            button_maker(310, 200, 180, 35, 'grey', 'grey', '', 35, 'BOARDS = ' + str(boards_number), 'gold',  # Boards
                         transparent_on=False, transparent_off=False)

            pygame.draw.line(display, colors['red'], (310, 245), (490, 245), 4)  # line

            button_maker(310, 260, 180, 35, 'grey', 'grey', '', 35, 'STAMINA = ' + str(stamina), 'white',  # Stamina
                         transparent_on=False, transparent_off=False)
            button_maker(310, 300, 180, 35, 'grey', 'grey', '', 35, 'FOOD = ' + str(food), 'white',  # Food
                         transparent_on=False, transparent_off=False)
            button_maker(310, 340, 180, 35, 'grey', 'grey', '', 35, 'DRINK = ' + str(drink), 'white',  # Drink
                         transparent_on=False, transparent_off=False)
            button_maker(310, 380, 180, 35, 'grey', 'grey', '', 35, 'HEALTH = ' + str(health), 'green',  # Drink
                         transparent_on=False, transparent_off=False)

            button_maker(305, 440, 190, 35, 'green', 'blue', '', 45, 'BARRICADE', 'white',  # BARRICADE
                         transparent_on=False, transparent_off=False)

            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
                         transparent_on=False)  # Exit

            pygame.display.update()
            clock.tick(FPS)


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
key1 = Item('Key 1', '', 'other', '')
key2 = Item('Key 2', '', 'other', '')
key3 = Item('Key 3', '', 'other', '')

# Add items to inventory
inventory.add_to_inventory(axe)
inventory.add_to_inventory(vodka)
inventory.add_to_inventory(vodka)
inventory.add_to_inventory(vodka)
inventory.add_to_inventory(dog_food)
inventory.add_to_inventory(board)
inventory.add_to_inventory(board)
inventory.add_to_inventory(key1)


class JournalWindow:

    def open_journal_window(self):

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return map_window.open_map_window()

                # create squares in Inventory
                if event.type == pygame.MOUSEBUTTONDOWN:
                    loop = True
                    x = 0
                    y = 0
                    w = 200
                    h = 150

                    while loop == True:
                        button = pygame.Rect(x, y, w, h)
                        x += 200
                        if x > 600:
                            x = 0
                            y += 150

            # Window setting
            pygame.display.set_caption("Journal")
            journal_image = pygame.image.load('images/journal.jpg')
            display.blit(journal_image, (0, 0))

            writing_text('', 35, "I need to find a way to get into this closed GATE in the city.", 'black', 5, 15)
            writing_text('', 35, "I can do this in a few ways:", 'black', 5, 55)
            writing_text('', 35, "-Find 3 keys for the 3 padlocks in the GATE", 'black', 20, 120)
            writing_text('', 35, "-Use my ATTACK to destroy the padlocks", 'black', 20, 180)
            writing_text('', 35, "-Use my DEXTERITY to brake in", 'black', 20, 240)

            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Back', 'white',
                         transparent_on=False)  # Exit

            pygame.display.update()
            clock.tick(FPS)


journal_window = JournalWindow()


class InventoryWindow:

    def equip_item(self, index):

        item = list(inventory.inventory)[index]

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    inventory_window.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # YES - Equip Item
                    button = pygame.Rect(225, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            # musi przeszukać listę wyposażonych rzeczy czy jest w niej coś
                            # I jeżeli items.type jest taki sam, to przedmiot z ekwipunku wrzuca do Inventory
                            # a z Inventory do ekwipunku

                            # todo zamień te ify na metodę:
                            if item.type == 'weapon':
                                player1_equipment.equipped_weapon_attribute = item.attribute
                                player1_equipment.equipped_weapon_name = item.name
                                player1.update_attributes()
                                player1_equipment.put_equipped_items_into_container(item)
                                print(player1_equipment.equipped_items)


                            elif item.type == 'torso':
                                player1_equipment.equipped_torso_attribute = item.attribute
                                player1_equipment.equipped_torso_name = item.name
                                player1.update_attributes()

                            elif item.type == 'legs':
                                player1_equipment.equipped_legs_attribute = item.attribute
                                player1_equipment.equipped_legs_name = item.name
                                player1.update_attributes()

                            statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # NO - Don't equip Item
                    button = pygame.Rect(400, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            statistic_window.open_statistics_window()  ### Zmień to później na okno z wyborem itemu

            # Window settings
            pygame.display.set_caption('Equip items?')

            button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to equip this items?', 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(225, 300, 175, 50, 'green', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                         transparent_off=False)
            button_maker(400, 300, 175, 50, 'red', 'blue', '', 30, '           NO', 'white',
                         transparent_on=False, transparent_off=False)

            pygame.display.update()
            clock.tick(FPS)

    def delete_item_from_inventory(self, index):
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

                if event.type == pygame.MOUSEBUTTONDOWN:  # YES - Remove Item
                    button = pygame.Rect(225, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            inventory.inventory.remove(item_index)  # Remove Item from inventory.inventory[]
                            items_names.remove(item_index.name)  # Remove Item from items_names[]

                            if item_index.name == player1_equipment.equipped_weapon_name or \
                                    item_index.name == player1_equipment.equipped_torso_name or \
                                    item_index.name == player1_equipment.equipped_legs_name:

                                # If deleted items is still in inventory.inventory[] -> equip this items
                                if item_index.name in items_names:
                                    # player1.update_attributes()

                                    print('atak: ', player1.attack)
                                    print('obrona: ', player1.defence)
                                    inventory.show_inventory(0, 0, 0)

                                # If deleted items was the last one -> unequip this items
                                elif item_index.name not in items_names:
                                    player1.reset_attributes(item_index.type)

                                    if item_index.type == 'weapon':
                                        # player1.attack = player1.attack - item_index.attribute
                                        player1_equipment.equipped_weapon_attribute -= item_index.attribute

                                    if item_index.type == 'torso':
                                        # player1.defence = player1.defence - item_index.attribute
                                        player1_equipment.equipped_torso_attribute -= item_index.attribute

                                    if item_index.type == 'legs':
                                        player1_equipment.equipped_legs_attribute -= item_index.attribute

                                    player1.update_attributes()

                                    print('atak: ', player1.attack)
                                    print('obrona: ', player1.defence)
                                    inventory.show_inventory(0, 0, 0)

                            self.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # NO - Don't remove Item
                    button = pygame.Rect(400, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_inventory_window()

            # Window settings
            pygame.display.set_caption('Remove items?')
            ###### Niech się pyta o konkretny przedmiot ############
            button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to REMOVE this items?', 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(225, 300, 175, 50, 'red', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                         transparent_off=False)
            button_maker(400, 300, 175, 50, 'green', 'blue', '', 30, '           NO', 'white', transparent_on=False,
                         transparent_off=False)

            pygame.display.update()
            clock.tick(FPS)

    def use_item(self, index, type, attribute):
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
                    self.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # YES - Use Item
                    button = pygame.Rect(225, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):

                            inventory.inventory.remove(item_index)  # Remove Item from inventory.inventory[]
                            items_names.remove(item_index.name)  # Remove Item from items_names[]

                            if type == 'food':
                                player1.food += (attribute * 10)
                                if player1.food > 100:
                                    player1.food = 100
                            elif type == 'drink':
                                player1.drink += (attribute * 10)
                                if player1.drink > 100:
                                    player1.drink = 100
                            elif type == 'stamina':
                                player1.stamina += (attribute * 10)
                                if player1.stamina > 100:
                                    player1.stamina = 100
                            elif type == 'health':
                                player1.health += (attribute * 10)
                                if player1.health > 100:
                                    player1.health = 100

                            self.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # NO - Don't use Item
                    button = pygame.Rect(400, 300, 175, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_inventory_window()

            # Window settings
            pygame.display.set_caption('Use items?')
            ###### Niech się pyta o konkretny przedmiot ############
            button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to USE this items?', 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(225, 300, 175, 50, 'green', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                         transparent_off=False)
            button_maker(400, 300, 175, 50, 'red', 'blue', '', 30, '           NO', 'white', transparent_on=False,
                         transparent_off=False)

            pygame.display.update()
            clock.tick(FPS)

    def open_inventory_window(self):  # create Inventory Window
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return map_window.open_map_window()

                # create squares in Inventory
                if event.type == pygame.MOUSEBUTTONDOWN:
                    loop = True
                    x = 0
                    y = 0
                    w = 200
                    h = 150

                    while loop == True:
                        button = pygame.Rect(x, y, w, h)
                        x += 200
                        if x > 600:
                            x = 0
                            y += 150

                        #  Use Item
                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                try:

                                    use_item = inventory_window.use_item

                                    if x == 200 and y == 0:
                                        index = 0
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 400 and y == 0:
                                        index = 1
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 600 and y == 0:
                                        index = 2
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 0 and y == 150:
                                        index = 3
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 200 and y == 150:
                                        index = 4
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 400 and y == 150:
                                        index = 5
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 600 and y == 150:
                                        index = 6
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 0 and y == 300:
                                        index = 7
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 200 and y == 300:
                                        index = 8
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 400 and y == 300:
                                        index = 9
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                    if x == 600 and y == 300:
                                        index = 10
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass  # todo Add possibillity of equip item from here

                                    if x == 0 and y == 450:
                                        index = 11
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            pass # todo Add possibillity of equip item from here

                                except IndexError:
                                    break

                                loop = False

                                # Items in Inventory
                                pygame.display.update()
                                clock.tick(FPS)

                        if event.button == 2:
                            break

                        # Delete items
                        if event.button == 3:
                            if button.collidepoint(event.pos):
                                try:
                                    delete_item_from_inventory = inventory_window.delete_item_from_inventory

                                    if y == 0:
                                        if x == 200:
                                            delete_item_from_inventory(0)
                                        if x == 400:
                                            delete_item_from_inventory(1)
                                        if x == 600:
                                            delete_item_from_inventory(2)

                                    if y == 150:
                                        if x == 0:
                                            delete_item_from_inventory(3)
                                        if x == 200:
                                            delete_item_from_inventory(4)
                                        if x == 400:
                                            delete_item_from_inventory(5)
                                        if x == 600:
                                            delete_item_from_inventory(6)

                                    if y == 300:
                                        if x == 0:
                                            delete_item_from_inventory(7)
                                        if x == 200:
                                            delete_item_from_inventory(8)
                                        if x == 400:
                                            delete_item_from_inventory(9)
                                        if x == 600:
                                            delete_item_from_inventory(10)

                                    if y == 450 and x == 0:
                                        delete_item_from_inventory(11)

                                except IndexError:
                                    break

                                loop = False

                                # Items in Inventory
                                pygame.display.update()
                                clock.tick(FPS)

            # Window setting
            pygame.display.set_caption("Inventory")
            backpack_image = pygame.image.load('images/backpack.jpg')
            display.blit(backpack_image, (0, 0))

            writing_text('', 18, 'LMB = Use Item', 'pure_red', 0, 555)
            writing_text('', 18, 'RMB = Delete Item', 'pure_red', 0, 580)
            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Back', 'white',
                         transparent_on=False)  # Exit

            statistics_buttons(130, 570, 110, 20, '', 25, f'FOOD = {player1.food}', 'needs', player1.food)
            statistics_buttons(250, 570, 110, 20, '', 25, f'DRINK = {player1.drink}', 'needs', player1.drink)
            statistics_buttons(370, 570, 130, 20, '', 25, f'STAMINA = {player1.stamina}', 'needs', player1.stamina)
            statistics_buttons(510, 570, 130, 20, '', 25, f'HEALTH = {player1.health}', 'needs', player1.health)

            # Items in Inventory
            inventory.show_inventory(0, 0, 0)
            pygame.display.update()
            clock.tick(FPS)


inventory_window = InventoryWindow()


class EquipItemWindow:

    @staticmethod
    def open_equip_item_window(image, window_name, type, attribute_text):

        while True:
            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    loop = True
                    x = 0
                    y = 0
                    w = 200
                    h = 150

                    while loop == True:  # create squares
                        button = pygame.Rect(x, y, w, h)
                        x += 200
                        if x > 600:
                            x = 0
                            y += 150

                        if event.button == 3:  # RMB
                            if button.collidepoint(event.pos):
                                break

                        if event.button == 1:  # LMB
                            if button.collidepoint(event.pos):

                                try:

                                    equip_item = inventory_window.equip_item

                                    if x == 200 and y == 0:
                                        equip_item(0)
                                    if x == 400 and y == 0:
                                        equip_item(1)
                                    if x == 600 and y == 0:
                                        equip_item(2)
                                    if x == 0 and y == 150:
                                        equip_item(3)
                                    if x == 200 and y == 150:
                                        equip_item(4)
                                    if x == 400 and y == 150:
                                        equip_item(5)
                                    if x == 600 and y == 150:
                                        equip_item(6)
                                    if x == 0 and y == 300:
                                        equip_item(7)
                                    if x == 200 and y == 300:
                                        equip_item(8)
                                    if x == 400 and y == 300:
                                        equip_item(9)
                                    if x == 600 and y == 300:
                                        equip_item(10)
                                    if x == 0 and y == 450:
                                        equip_item(11)

                                except IndexError:
                                    break

                                loop = False

                                # Items in Inventory
                                pygame.display.update()
                                clock.tick(FPS)

            # Window setting
            pygame.display.set_caption(window_name)
            set_image = pygame.image.load(image)
            display.blit(set_image, (0, 0))
            writing_text('', 35, 'LMB = Equip Item', 'pure_red', 0, 570)

            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Back', 'white',
                         transparent_on=False)  # Exit

            # Items in Inventory
            inventory.show_items_to_equip(type, attribute_text)
            pygame.display.update()
            clock.tick(FPS)


equip_item_window = EquipItemWindow()


class StatisticsWindow:

    def open_statistics_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Press 'WEAPON' Button
                    button = pygame.Rect(380, 420, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            equip_item_window.open_equip_item_window('images/weapon.jpg', "Equip Weapon", 'weapon',
                                                                     'Damage: ')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Press 'TORSO' Button
                    button = pygame.Rect(500, 200, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            equip_item_window.open_equip_item_window('images/torso.jpg', "Equip Torso", 'torso',
                                                                     'Defence: ')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Press 'LEGS' Button
                    button = pygame.Rect(530, 490, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            equip_item_window.open_equip_item_window('images/legs.jpg', "Equip Legs", 'legs',
                                                                     'Defence: ')

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click Strength + button
                    button = pygame.Rect(250, 0, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.strength += 1
                            player1.leveled_up -= 1
                            player1.update_attributes()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click Speed + button
                    button = pygame.Rect(250, 50, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.speed += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:  # click Dexterity + button
                    button = pygame.Rect(250, 100, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.dexterity += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:  # click Intelligence + button
                    button = pygame.Rect(250, 150, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.intelligence += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:  # click Charisma + button
                    button = pygame.Rect(250, 200, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.charisma += 1
                            player1.leveled_up -= 1

            # Window settings
            pygame.display.set_caption('Statistics')
            stats_image = pygame.image.load('images/stats.jpg')
            display.blit(stats_image, (245, 0))

            statistics_buttons(0, 0, 245, 50, '', 36, 'STRENGTH:   ' + str(player1.strength), 'attribute',
                               player1.strength)
            statistics_buttons(0, 50, 245, 50, '', 36, 'SPEED:   ' + str(player1.speed), 'attribute',
                               player1.speed)
            statistics_buttons(0, 100, 245, 50, '', 36, 'DEXTERITY:   ' + str(player1.dexterity), 'attribute',
                               player1.dexterity)
            statistics_buttons(0, 150, 245, 50, '', 36, 'INTELLIGENCE:   ' + str(player1.intelligence),
                               'attribute', player1.intelligence)
            statistics_buttons(0, 200, 245, 50, '', 36, 'CHARISMA:   ' + str(player1.charisma), 'attribute',
                               player1.charisma)

            statistics_buttons(0, 250, 245, 45, '', 36, 'ATTACK:   ' + str(player1.attack), 'fight',
                               player1.attack)
            statistics_buttons(0, 295, 245, 45, '', 36, 'DEFENCE:   ' + str(player1.defence), 'fight',
                               player1.defence)

            statistics_buttons(0, 340, 245, 40, '', 36, 'FOOD:   ' + str(player1.food), 'needs', player1.food)
            statistics_buttons(0, 380, 245, 40, '', 36, 'DRINK:   ' + str(player1.drink), 'needs', player1.drink)
            statistics_buttons(0, 420, 245, 40, '', 36, 'STAMINA:   ' + str(player1.stamina), 'needs',
                               player1.stamina)
            statistics_buttons(0, 460, 245, 40, '', 36, 'HEALTH:   ' + str(player1.health), 'needs',
                               player1.health)

            statistics_buttons(0, 500, 245, 50, '', 36,
                               'EXP:    ' + str(player1.exp) + ' / ' + str(player1.exp_to_next_level),
                               'exp', player1.exp)
            statistics_buttons(0, 550, 245, 50, '', 36, 'LEVEL:   ' + str(player1.level), 'exp', player1.level)

            # Equipment buttons
            equipment_buttons(380, 420, 100, 50, player1_equipment.equipped_weapon_name, 'Weapon')  # Weapon
            equipment_buttons(500, 200, 100, 50, player1_equipment.equipped_torso_name, '   Torso')  # Torso
            equipment_buttons(530, 490, 100, 50, player1_equipment.equipped_legs_name, '   Legs')  # Legs

            # ESC button
            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Back', 'white',
                         transparent_on=False)  # Exit

            if player1.leveled_up > 0:
                # Remaining level points
                writing_text('', 36, f'Level points = {player1.leveled_up}', 'white', 595, 15)

                # Leveled up buttons
                button_maker(250, 0, 35, 35, 'green', 'black', '', 40, " +", 'white', transparent_on=False,
                             transparent_off=False)
                button_maker(250, 50, 35, 35, 'green', 'black', '', 40, " +", 'white', transparent_on=False,
                             transparent_off=False)
                button_maker(250, 100, 35, 35, 'green', 'black', '', 40, " +", 'white', transparent_on=False,
                             transparent_off=False)
                button_maker(250, 150, 35, 35, 'green', 'black', '', 40, " +", 'white', transparent_on=False,
                             transparent_off=False)
                button_maker(250, 200, 35, 35, 'green', 'black', '', 40, " +", 'white', transparent_on=False,
                             transparent_off=False)

            pygame.display.update()
            clock.tick(FPS)


statistic_window = StatisticsWindow()


class SearchWindow:

    def open_search_window(self, image, previous_window, chest_location, found_item_location):  # create Chest Window
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN:  # Search
                    button = pygame.Rect(0, 550, 100, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            chest.search(chest_location, found_item_location)  # Add items to the "found items" chest
                            pygame.display.update()
                            clock.tick(FPS)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Exit
                    button = pygame.Rect(700, 550, 100, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN:
                    loop = True
                    x = 0
                    y = 0
                    w = 200
                    h = 150

                    while loop == True:
                        button = pygame.Rect(x, y, w, h)
                        x += 200
                        if x > 600:
                            x = 0
                            y += 150

                        if event.button == 2:
                            break

                        if event.button == 3:
                            break

                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                try:
                                    if x == 200 and y == 0:
                                        chest.add_to_inventory_while_search(0, found_item_location)
                                    if x == 400 and y == 0:
                                        chest.add_to_inventory_while_search(1, found_item_location)
                                    if x == 600 and y == 0:
                                        chest.add_to_inventory_while_search(2, found_item_location)
                                    if x == 0 and y == 150:
                                        chest.add_to_inventory_while_search(3, found_item_location)
                                    if x == 200 and y == 150:
                                        chest.add_to_inventory_while_search(4, found_item_location)
                                    if x == 400 and y == 150:
                                        chest.add_to_inventory_while_search(5, found_item_location)
                                    if x == 600 and y == 150:
                                        chest.add_to_inventory_while_search(6, found_item_location)
                                    if x == 0 and y == 300:
                                        chest.add_to_inventory_while_search(7, found_item_location)
                                    if x == 200 and y == 300:
                                        chest.add_to_inventory_while_search(8, found_item_location)
                                    if x == 400 and y == 300:
                                        chest.add_to_inventory_while_search(9, found_item_location)
                                    if x == 600 and y == 300:
                                        chest.add_to_inventory_while_search(10, found_item_location)
                                    if x == 0 and y == 450:
                                        chest.add_to_inventory_while_search(11, found_item_location)

                                except IndexError:
                                    break

                                loop = False

                                # Items in Inventory
                                pygame.display.update()
                                clock.tick(FPS)

            # Window setting
            pygame.display.set_caption("Found Items")
            location_image = pygame.image.load(image)
            display.blit(location_image, (0, 0))

            # Add menu buttons
            button_maker(0, 550, 100, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Search', 'white',
                         transparent_on=False)  # Search

            statistics_buttons(100, 550, 150, 40, '', 30, f'FOOD = {player1.food}', 'needs', player1.food)
            statistics_buttons(250, 550, 150, 40, '', 30, f'DRINK = {player1.drink}', 'needs', player1.drink)
            statistics_buttons(400, 550, 150, 40, '', 30, f'STAMINA = {player1.stamina}', 'needs', player1.stamina)
            statistics_buttons(550, 550, 150, 40, '', 30, f'HEALTH = {player1.health}', 'needs', player1.health)

            button_maker(700, 550, 100, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  Back', 'white',
                         transparent_on=False)  # Exit

            # Information
            writing_text('', 35, 'LMB = Take Item', 'pure_red', 300, 500)

            # Items in Inventory
            chest.show_found_items(found_item_location)
            pygame.display.update()
            clock.tick(FPS)


chest_inventory = SearchWindow()


class TradeWindow:

    def open_trade_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return map_window.open_map_window()

            # Window settings
            pygame.display.set_caption('Trade')
            trade_image = pygame.image.load('images/trade.jpg')
            display.blit(trade_image, (0, 0))

            # ESC button
            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Back', 'white',
                         transparent_on=False)  # Exit

            pygame.display.update()
            clock.tick(FPS)


trade_window = TradeWindow()


class LocationWindow:
    def __init__(self):
        self.locations = ['black_pearl', 'bridge', 'crane', 'flat', 'forest', 'gate', 'hotel', 'office', 'opera',
                          'restaurant', 'soldek', 'basilica', 'supermarket']

    @staticmethod
    def open_location_window(image, window_name, random_items, found_item_location, defence, location_name):

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    map_window.open_map_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Search
                    button = pygame.Rect(0, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            chest.search(random_items, found_item_location)
                            chest_inventory.open_search_window(image, location_window.open_location_window,
                                                               random_items, found_item_location)
                            pygame.display.update()
                            clock.tick(FPS)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Sleep
                    button = pygame.Rect(200, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            Sleep().open_sleep_window(image, location_window.open_location_window)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Barricade
                    button = pygame.Rect(400, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            OpenBarricadeWindow().open_barricade_window(image, location_window.open_location_window,
                                                                        defence,
                                                                        location_name, window_name, found_item_location)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Exit
                    button = pygame.Rect(600, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            map_window.open_map_window()

            # Window name
            pygame.display.set_caption(window_name)

            # Add screen image
            location_image = pygame.image.load(image)
            display.blit(location_image, (0, 0))

            # Add menu buttons
            button_maker(0, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23, '        Search', 'white',
                         transparent_on=False, transparent_off=False)  # Search
            button_maker(200, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23, '         Sleep', 'white',
                         transparent_on=False, transparent_off=False)  # Sleep
            button_maker(400, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23, '      Barricade', 'white',
                         transparent_on=False, transparent_off=False)  # Barricade
            button_maker(600, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23, '          Back', 'white',
                         transparent_on=False, transparent_off=False)  # Exit

            # Show DEFENCE stat
            button_maker(20, 20, 220, 40, 'black', 'black', '', 45, 'Defence = ' + str(defence), 'red',
                         transparent_on=False, transparent_off=False)
            # writing_text('', 45, 'Defence: ' + str(self.defence), 'pure_red', 20, 20)

            pygame.display.update()
            clock.tick(FPS)


location_window = LocationWindow()


# Creates map window
class MapWindow:
    def __init__(self):
        self.open_sound = pygame.mixer.Sound('audio/open_sound.wav')
        self.door_sound = pygame.mixer.Sound('audio/door.wav')
        self.raven_sound = pygame.mixer.Sound('audio/raven2.wav')
        self.open_book = pygame.mixer.Sound('audio/open_book.wav')

    def open_map_window(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a Journal window !!!!!!!!!!!!!!!
                    button = pygame.Rect(0, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_book.play()
                            journal_window.open_journal_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open an Inventory window
                    button = pygame.Rect(200, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_sound.play()
                            inventory_window.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a Statistics window
                    button = pygame.Rect(400, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_sound.play()
                            statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a Trade window
                    button = pygame.Rect(600, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.open_sound.play()
                            trade_window.open_trade_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Black Pearl" window
                    print(chest.random_items_black_pearl)
                    button = pygame.Rect(575, 430, 135, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/black_pearl.jpg', '"Black Pearl"',
                                                                 chest.random_items_black_pearl,
                                                                 chest.found_items_black_pearl,
                                                                 set_defence.black_pearl_defence, 'black_pearl')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Bridge" window
                    button = pygame.Rect(170, 100, 80, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/bridge.jpg', 'Bridge',
                                                                 chest.random_items_bridge,
                                                                 chest.found_items_bridge, set_defence.bridge_defence,
                                                                 'bridge')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Crane" window
                    button = pygame.Rect(280, 150, 70, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/crane.jpg', 'Crane', chest.random_items_crane,
                                                                 chest.found_items_crane, set_defence.crane_defence,
                                                                 'crane')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Flat" window
                    button = pygame.Rect(500, 175, 50, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/flat.jpg', 'Flat', chest.random_items_flat,
                                                                 chest.found_items_flat, set_defence.flat_defence,
                                                                 'flat')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Forest" window
                    button = pygame.Rect(450, 25, 75, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.raven_sound.play()
                            location_window.open_location_window('images/forest.jpg', 'Forest',
                                                                 chest.random_items_forest,
                                                                 chest.found_items_forest, set_defence.forest_defence,
                                                                 'forest')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Gate" window
                    button = pygame.Rect(610, 160, 60, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            if (key1 and key2 and key3) in inventory.inventory or player1.attack == 15 \
                                    or player1.dexterity == 10:
                                self.door_sound.play()
                                VictoryWindow().open_victory_window()

                            else:
                                while True:

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()

                                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                            map_window.open_map_window()

                                        if event.type == pygame.MOUSEBUTTONDOWN:  # Exit
                                            button = pygame.Rect(600, 550, 200, 40)
                                            if event.button == 1:
                                                if button.collidepoint(event.pos):
                                                    map_window.open_map_window()

                                        if event.type == pygame.MOUSEBUTTONDOWN:  # OPEN
                                            button = pygame.Rect(325, 275, 150, 50)
                                            if event.button == 1:
                                                if button.collidepoint(event.pos):
                                                    if (key1 and key2 and key3) in inventory.inventory or player1.attack >= 15 \
                                                            or player1.dexterity >= 10:
                                                        self.door_sound.play()
                                                        VictoryWindow().open_victory_window()
                                                    else:
                                                        button_maker(250, 220, 300, 40, 'blue', 'blue', '', 36,
                                                                     " You can't open this now", 'white',
                                                                     transparent_on=False, transparent_off=False)
                                                        pygame.display.update()
                                                        time.sleep(1.5)

                                    # Window name
                                    pygame.display.set_caption("Gate")

                                    # Add screen image
                                    location_image = pygame.image.load('images/closed_gate.jpg')
                                    display.blit(location_image, (0, 0))

                                    # Add menu buttons
                                    button_maker(600, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23,
                                                 '          Back', 'white',
                                                 transparent_on=False, transparent_off=False)  # Exit

                                    button_maker(325, 275, 150, 50, 'green', 'grey', 'Comic Sans MS', 23,
                                                 '      OPEN', 'white',
                                                 transparent_on=False, transparent_off=False)  # Open

                                    pygame.display.update()
                                    clock.tick(FPS)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Hotel" window
                    button = pygame.Rect(450, 265, 70, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/hotel.jpeg', 'Hotel', chest.random_items_hotel,
                                                                 chest.found_items_hotel, set_defence.hotel_defence,
                                                                 'hotel')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Office" window
                    button = pygame.Rect(650, 270, 80, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/office.jpg', 'Office',
                                                                 chest.random_items_office,
                                                                 chest.found_items_office, set_defence.office_defence,
                                                                 'office')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Opera House" window
                    button = pygame.Rect(180, 450, 140, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/opera.jpg', 'Opera House',
                                                                 chest.random_items_opera,
                                                                 chest.found_items_opera, set_defence.opera_defence,
                                                                 'opera')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Restaurant" window
                    button = pygame.Rect(30, 230, 115, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/restaurant.jpg', 'Restaurant',
                                                                 chest.random_items_restaurant,
                                                                 chest.found_items_restaurant,
                                                                 set_defence.restaurant_defence, 'restaurant')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Sołdek" window
                    button = pygame.Rect(200, 310, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/soldek.jpg', '"Sołdek"',
                                                                 chest.random_items_soldek,
                                                                 chest.found_items_soldek, set_defence.soldek_defence,
                                                                 'soldek')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "St. Mary's Basilica" window
                    button = pygame.Rect(540, 70, 180, 45)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/basilica.jpg', "St. Mary's Basilica",
                                                                 chest.random_items_basilica,
                                                                 chest.found_items_basilica,
                                                                 set_defence.basilica_defence, 'basilica')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Supermarket" window
                    button = pygame.Rect(10, 50, 135, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            self.door_sound.play()
                            location_window.open_location_window('images/supermarket.jpg', '"Supermarket"',
                                                                 chest.random_items_supermarket,
                                                                 chest.found_items_supermarket,
                                                                 set_defence.supermarket_defence, 'supermarket')

                # Open an Inventory window
                if player1.health <= 20 or player1.food == 0 or player1.drink == 0 or player1.stamina <= 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button = pygame.Rect(760, 10, 25, 25)
                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                self.open_sound.play()
                                inventory_window.open_inventory_window()

                # Open an Statistics window
                if player1.leveled_up > 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button = pygame.Rect(20, 10, 130, 25)
                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                self.open_sound.play()
                                statistic_window.open_statistics_window()

            # Screen settings and graphic
            pygame.display.set_caption("Map")
            map_image = pygame.image.load('images/map.jpg')
            display.blit(map_image, (0, 0))

            if player1.health <= 20 or player1.food == 0 or player1.drink == 0 or player1.stamina <= 10:
                button_maker(760, 10, 25, 25, 'black', 'black', '', 30, '!'.center(3, ' '), 'pure_red',
                             transparent_on=False,
                             transparent_off=False)

            if player1.leveled_up > 0:
                button_maker(20, 10, 130, 25, 'red', 'black', '', 30, 'NEW LEVEL!'.center(3, ' '), 'green',
                             transparent_on=False,
                             transparent_off=False)

            # Locations on the Map
            button_maker(575, 430, 135, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, '"Black Pearl"', 'white',
                         transparent_on=False, text_on=False)  # Black Pearl
            button_maker(170, 100, 80, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Bridge', 'white',
                         transparent_on=False, text_on=False)  # Bridge
            button_maker(280, 150, 70, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Crane', 'white',
                         transparent_on=False, text_on=False)  # Crane
            button_maker(500, 175, 50, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Flat', 'white',
                         transparent_on=False, text_on=False)  # Flat
            button_maker(450, 25, 75, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Forest', 'white',
                         transparent_on=False, text_on=False)  # Forest

            button_maker(610, 160, 60, 40, 'grey', 'yellow', 'Comic Sans MS', 23, 'Gate', 'white',
                         transparent_on=False, text_on=False)  # Gate

            button_maker(450, 265, 70, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Hotel', 'white',
                         transparent_on=False, text_on=False)  # Hotel
            button_maker(650, 270, 80, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Office', 'white',
                         transparent_on=False, text_on=False)  # Office
            button_maker(180, 450, 140, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Opera House', 'white',
                         transparent_on=False, text_on=False)  # Opera
            button_maker(30, 230, 115, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Restaurant', 'white',
                         transparent_on=False, text_on=False)  # Restaurant
            button_maker(200, 310, 100, 50, 'grey', 'pure_red', 'Comic Sans MS', 23, '"Sołdek"', 'white',
                         transparent_on=False, text_on=False)  # Sołdek
            button_maker(540, 70, 180, 45, 'grey', 'pure_red', 'Comic Sans MS', 20, "St. Mary's Basilica", 'white',
                         transparent_on=False, text_on=False)  # St. Mary's Basilica
            button_maker(10, 50, 135, 40, 'grey', 'pure_red', 'Comic Sans MS', 21, 'Supermarket', 'white',
                         transparent_on=False, text_on=False)  # Supermarket

            # Menu buttons
            button_maker(0, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '        Journal', 'white',
                         transparent_on=False)  # Journal
            button_maker(200, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, 'Inventory'.center(20), 'white',
                         transparent_on=False)  # Inventory
            button_maker(400, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '      Statistics', 'white',
                         transparent_on=False)  # Statistics
            button_maker(600, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '        Trade', 'white',
                         transparent_on=False)  # Options

            pygame.display.update()
            clock.tick(FPS)


map_window = MapWindow()


class MainMenuWindow:
    def open_main_menu_window(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click START Button
                    button = pygame.Rect(350, 400, 80, 30)
                    if event.button == 1:
                        # `event.pos` is the mouse position
                        if button.collidepoint(event.pos):
                            # effect = pygame.mixer.Sound('zombie_sound.wav')
                            # effect.play()
                            # time.sleep(2)
                            map_window.open_map_window()
                            map_window.open_map_window()

            # Window settings
            pygame.display.set_caption("Main menu")
            map_image = pygame.image.load('images/map.jpg')
            display.blit(map_image, (0, 0))
            writing_text('Comic Sans MS', 40, "Untitled Game", "white", 228, 254)

            # Interactive START button
            button_maker(350, 400, 80, 30, 'pure_red', 'red', 'Calibri', 28, 'START', 'black', transparent_on=False,
                         transparent_off=False)
            writing_text('Calibri', 28, 'START', 'white', 355, 400)

            pygame.display.update()
            clock.tick(FPS)


main_menu_window = MainMenuWindow()
