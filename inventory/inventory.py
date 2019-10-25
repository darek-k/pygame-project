import sys

import pygame

from create import button_maker
from main import statistic_window, player1_equipment, player1, inventory_window, inventory


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self, count_weapon, count_torso, count_legs):
        x = 0
        y = 0

        self.sorted_inventory = sorted(self.inventory, key=operator.attrgetter('type', 'name'))

        # for item in self.inventory:
        for item in self.sorted_inventory:

            # icon = pygame.image.load(item.icon)     ###### Wyświetlanie grafiki #######
            # display.blit(icon, (300,120))

            if item.type == 'weapon':
                text = 'Damage: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'orange', x, y + 50)

            if item.type == 'torso' or item.type == 'legs':
                text = 'Defence: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'violet', x, y + 50)

            if item.type == 'food':
                text = 'Food: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'brown', x, y + 50)

            if item.type == 'drink':
                text = 'Drink: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'blue', x, y + 50)

            if item.type == 'health':
                text = 'Health: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'green', x, y + 50)

            if item.type == 'stamina':
                text = 'Stamina: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'white')
                writing_text('', 35, text + str(item.attribute), 'yellow', x, y + 50)

            if item.type == 'other':
                text = ''
                button_maker(x, y, item.size_x, item.size_y, 'gold', 'blue', '', 40, item.name, 'gold')
                writing_text('', 35, text + str(item.attribute), 'gold', x, y + 50)

            # Make equipped items GREEN
            if count_weapon == 0:
                if item.name == player1_equipment.equipped_weapon_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_green')
                    writing_text('', 35, text + str(item.attribute), 'orange', x, y + 50)
                    count_weapon += 1
            if count_torso == 0:
                if item.name == player1_equipment.equipped_torso_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_green')
                    writing_text('', 35, text + str(item.attribute), 'violet', x, y + 50)
                    count_torso += 1
            if count_legs == 0:
                if item.name == player1_equipment.equipped_legs_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'ultra_green')
                    writing_text('', 35, text + str(item.attribute), 'violet', x, y + 50)
                    count_legs += 1

            x += 200
            if x > 600:
                x = 0
                y += 150

        if len(self.inventory) < 12:
            length = 12 - len(self.inventory)
            for i in range(length):
                button_maker(x, y, 200, 150, 'red', 'blue', '', 40, '', 'ultra_green')

                x += 200
                if x > 600:
                    x = 0
                    y += 150

    def show_items_to_equip(self, type, attribute_text):
        x = 0
        y = 0

        for item in self.inventory:
            index = inventory.inventory.index(item)

            if item.type == type:

                if index <= 3:
                    y = 0
                elif index <= 7:
                    y = 150
                elif index <= 11:
                    y = 300

                if index == 0 or index == 4 or index == 8:
                    x = 0
                elif index == 1 or index == 5 or index == 9:
                    x = 200
                elif index == 2 or index == 6 or index == 10:
                    x = 400
                elif index == 3 or index == 7 or index == 11:
                    x = 600

                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', 40, item.name, 'red')
                writing_text('', 35, attribute_text + str(item.attribute), 'white', x, y + 50)
                button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
                             transparent_on=False)  # Exit

    def equip_item(self, index, type):

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
                            if item.type == 'weapon':
                                player1_equipment.equipped_weapon_attribute = item.attribute
                                print('item atribute = ', item.attribute)
                                print('equiped weapon atribute = ', player1_equipment.equipped_weapon_attribute)

                                player1_equipment.equipped_weapon_name = item.name
                                print('weapon name = ', item.name)
                                print('equiped weapon name = ', player1_equipment.equipped_weapon_name)

                                player1.update_attributes()
                                print('atak = ', player1.attack)


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

            if item.type == type:

                # Window settings
                pygame.display.set_caption('Equip item?')

                button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to equip this item?', 'white',
                             transparent_on=False, transparent_off=False)
                button_maker(225, 300, 175, 50, 'green', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                             transparent_off=False)
                button_maker(400, 300, 175, 50, 'red', 'blue', '', 30, '           NO', 'white',
                             transparent_on=False, transparent_off=False)

            else:
                break

            pygame.display.update()
