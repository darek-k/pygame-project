# Function that deletes item from inventory


########### NIE DZIAŁA #######################
import sys

import pygame

from clock import clock, FPS
from create import button_maker
from main import inventory, inventory_window, player1_equipment, player1


def delete_item_from_inventory(index):
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

                            # If deleted item is still in inventory.inventory[] -> equip this item
                            if item_index.name in items_names:
                                # player1.update_attributes()

                                print('atak: ', player1.attack)
                                print('obrona: ', player1.defence)
                                inventory.show_inventory(0, 0, 0)

                            # If deleted item was the last one -> unequip this item
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

                        inventory_window.open_inventory_window()

            if event.type == pygame.MOUSEBUTTONDOWN:  # NO - Don't remove Item
                button = pygame.Rect(400, 300, 175, 50)
                if event.button == 1:
                    if button.collidepoint(event.pos):
                        inventory_window.open_inventory_window()

        # Window settings
        pygame.display.set_caption('Remove item?')
        ###### Niech się pyta o konkretny przedmiot ############
        button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to REMOVE this item?', 'white',
                     transparent_on=False, transparent_off=False)
        button_maker(225, 300, 175, 50, 'red', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                     transparent_off=False)
        button_maker(400, 300, 175, 50, 'green', 'blue', '', 30, '           NO', 'white', transparent_on=False,
                     transparent_off=False)

        pygame.display.update()
        clock.tick(FPS)