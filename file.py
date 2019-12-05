# Initialization
import operator
import pygame
import random
import sys
import time

from clock import clock, FPS
from create import writing_text, button_maker, colors, statistics_buttons, equipment_buttons
from display import display
from player import player1_equipment

pygame.init()


def get_random_number(first_number, second_number):
    return random.randint(first_number, second_number)


# create a Player
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

        self.food = 100
        self.drink = 100
        self.stamina = 100
        self.health = 100

        self.exp = 40
        self.exp_to_next_level = 50
        self.level = 1
        self.leveled_up = 0

    def level_up(self):
        self.level += 1
        self.exp_to_next_level += self.exp + 20
        self.leveled_up += 1

    def update_attributes(self):
        self.attack = round(1 + player1_equipment.equipped_weapon_attribute, 1)

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
        if self.health <= 0:
            GameOverWindow().open_game_over_window()

    def use_item(self, index, type, attribute):   ######## Przenieś tę metodę do klasy PlayerEquipment ##########
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


player1 = Player('John', 5, 5, 5, 5, 5)


class Sleep:

    def open_sleep_window(self, image, previous_window):
        h = str(1)

        if player1.stamina < 100:
            stamina = int(player1.stamina) + 10
        else:
            stamina = 100

        hours_to_full_stamina = int((100 - player1.stamina) / 10)

        if player1.health < 100:
            health = int(player1.health) + 10
        else:
            health = 100
        hours_to_full_health = int((80 - player1.health) / 10)

        food = int(player1.food)
        drink = int(player1.drink)

        if player1.food > 0:
            food = int(player1.food) - 5
        if player1.drink > 0:
            drink = int(player1.drink) - 5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN:  # click MORE Button
                    button = pygame.Rect(410, 240, 60, 25)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            # Change hour
                            if h == 12:
                                h = 12
                            elif int(h) < 12:
                                if food > 0 and drink > 0:
                                    h = int(h) + 1

                                    if stamina < 100:  # Change stamina value
                                        stamina += 10

                                    if health < 80:  # Change health value
                                        health += 10

                                    food -= 5
                                    drink -= 5

                                elif food == 0:
                                    writing_text('', 45, "You are too hungry to sleep", 'red', 235, 100)
                                    pygame.display.update()
                                    clock.tick(FPS)
                                    time.sleep(1.5)
                                elif drink == 0:
                                    writing_text('', 45, "You are too thirsty to sleep", 'red', 235, 100)
                                    pygame.display.update()
                                    clock.tick(FPS)
                                    time.sleep(1.5)

                if event.type == pygame.MOUSEBUTTONDOWN:  # click LESS Button
                    button = pygame.Rect(410, 265, 60, 25)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            # Change hour
                            if int(h) < 2:
                                h = 1
                            elif int(h) >= 2:
                                h = int(h) - 1

                                if stamina == 100:  # Change stamina value
                                    if h >= hours_to_full_stamina:
                                        stamina = 100
                                    elif h < hours_to_full_stamina:
                                        stamina -= 10
                                elif stamina < 100:
                                    stamina -= 10

                                if health >= 80:  # Change stamina value
                                    if h >= hours_to_full_health:
                                        health = health
                                    elif h < hours_to_full_health:
                                        health -= 10
                                elif health < 80:
                                    health -= 10

                                food += 5
                                drink += 5

                if event.type == pygame.MOUSEBUTTONDOWN:  # click SLEEP Button
                    button = pygame.Rect(350, 500, 100, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.stamina = stamina
                            player1.health = health
                            player1.food = food
                            player1.drink = drink

                            # Sleep "animation"
                            sleep_image = pygame.image.load('images/sleep1.jpg')
                            display.blit(sleep_image, (0, 0))
                            pygame.display.update()
                            time.sleep(0.8)
                            sleep_image = pygame.image.load('images/sleep2.jpg')
                            display.blit(sleep_image, (0, 0))
                            pygame.display.update()
                            time.sleep(0.8)
                            sleep_image = pygame.image.load('images/sleep3.jpg')
                            display.blit(sleep_image, (0, 0))
                            pygame.display.update()
                            time.sleep(0.8)

                            return previous_window

                if event.type == pygame.MOUSEBUTTONDOWN: # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return previous_window


            # Window settings and graphic
            pygame.display.set_caption("Sleep")
            location_image = pygame.image.load(image)
            display.blit(location_image, (0, 0))

            button_maker(200, 200, 380, 35, 'grey', 'grey', '', 35, "How long do you want to sleep?", 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(330, 240, 80, 50, 'grey', 'grey', '', 60, str(h) + 'h', 'white',  # How many hours
                         transparent_on=False, transparent_off=False)
            button_maker(410, 240, 60, 25, 'green', 'green', '', 40, '   +', 'white',  # More
                         transparent_on=False, transparent_off=False)
            button_maker(410, 265, 60, 25, 'red', 'red', '', 40, '   -', 'white',  # Less
                         transparent_on=False, transparent_off=False)

            statistics_buttons(310, 300, 180, 35, '', 35, f'STAMINA = {stamina}', 'needs',
                                                stamina)
            statistics_buttons(310, 340, 180, 35, '', 35, f'HEALTH = {health}', 'needs',
                                                health)
            statistics_buttons(310, 380, 180, 35, '', 35, f'FOOD = {food}', 'needs',
                                                food)
            statistics_buttons(310, 420, 180, 35, '', 35, f'DRINK = {drink}', 'needs',
                                                drink)

            button_maker(350, 500, 100, 35, 'green', 'blue', '', 45, 'SLEEP', 'white',  # SLEEP
                         transparent_on=False, transparent_off=False)

            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
                         transparent_on=False)  # Exit


            pygame.display.update()
            clock.tick(FPS)



class Barricade:
    def __init__(self):
        self.black_pearl_defence = 50
        self.bridge_defence = 20
        self.crane_defence = 50
        self.flat_defence = 40
        self.forest_defence = 30
        self.gate_defence = 100
        self.hotel_defence = 50
        self.office_defence = 40
        self.opera_defence = 30
        self.restaurant_defence = 20
        self.soldek_defence = 50
        self.basilica_defence = 20
        self.supermarket_defence = 10


    def set_defence(self, location_name, defence, new_defence, image, window_name, chest_location, found_item_location):

        if location_name == 'black_pearl':
            barricade.black_pearl_defence = new_defence
        if location_name == 'bridge':
            barricade.bridge_defence = new_defence
        if location_name == 'crane':
            barricade.crane_defence = new_defence
        if location_name == 'flat':
            barricade.flat_defence = new_defence
        if location_name == 'forest':
            barricade.forest_defence = new_defence
        if location_name == 'gate':
            barricade.gate_defence = new_defence
        if location_name == 'hotel':
            barricade.hotel_defence = new_defence
        if location_name == 'office':
            barricade.office_defence = new_defence
        if location_name == 'opera':
            barricade.opera_defence = new_defence
        if location_name == 'restaurant':
            barricade.restaurant_defence = new_defence
        if location_name == 'soldek':
            barricade.soldek_defence = new_defence
        if location_name == 'basilica':
            barricade.basilica_defence = new_defence
        if location_name == 'supermarket':
            barricade.supermarket_defence = new_defence

        # Open previous window and update 'Defence'
        location_window.open_location_window(image, window_name, chest_location, found_item_location, defence, location_name)


    def open_barricade_window(self, image, previous_window, defence, location_name, window_name, chest_location, found_item_location):
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

        # create list with items names
        names_list = []
        for item in inventory.inventory:
            names_list.append(item.name.strip())

        # Count number of Boards in Inventory
        boards_number_on_begin = names_list.count('Board')
        boards_number = names_list.count('Board')


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
                                                print("Health too low")
                                        if drink > 0:
                                            drink -= 5
                                        else:
                                            drink = 0
                                            if health > 5:
                                                health -= 5
                                                count_health += 1
                                            else:
                                                print("Health too low")
                                    elif stamina <= 5:
                                        print("Stamina too low")
                                elif boards_number == 0:
                                    print("You don't have boards")


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

                            # create list of items names
                            names_list = [item.name for item in inventory.inventory]

                            start_index = 0
                            for item in range(used_boards_number):
                                index = names_list.index("Board", start_index)
                                start_index += 1
                                del inventory.inventory[index]
                                names_list = [item.name for item in inventory.inventory]


                            # Barricade "animation"
                            barricade_image = pygame.image.load('images/barricade.jpg')
                            display.blit(barricade_image, (0, 0))
                            pygame.display.update()
                            time.sleep(0.8)

                            return barricade.set_defence(location_name, defence, new_defence, image, window_name,
                                                         chest_location, found_item_location)


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

            pygame.draw.line(display, colors['red'], (310, 245), (490, 245), 4) # line

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


barricade = Barricade()  # Instance of Barricade class


# Items class
class Item:
    def __init__(self, name, attribute, type, icon):
        self.name = name
        self.attribute = attribute
        self.size_x = 200
        self.size_y = 150
        self.icon = icon
        self.type = type


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
cocaine = Item('Cocaine', 5,  'stamina', '')

# create other instances
board = Item('Board', '', 'other', '')
key = Item('Key', '', 'other', '')


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
            index = self.inventory.index(item)

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

    def equip_item(self, index):

        item = list(self.inventory)[index]

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
                            # I jeżeli item.type jest taki sam, to przedmiot z ekwipunku wrzuca do Inventory
                            # a z Inventory do ekwipunku

                            #todo zamień te ify na metodę:
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
            pygame.display.set_caption('Equip item?')

            button_maker(225, 250, 350, 50, 'blue', 'blue', '', 30, 'Do you want to equip this item?', 'white',
                         transparent_on=False, transparent_off=False)
            button_maker(225, 300, 175, 50, 'green', 'blue', '', 30, '         YES', 'white', transparent_on=False,
                         transparent_off=False)
            button_maker(400, 300, 175, 50, 'red', 'blue', '', 30, '           NO', 'white',
                         transparent_on=False, transparent_off=False)


            pygame.display.update()
            clock.tick(FPS)


    def delete_item_from_inventory(self, index):
        """ Function that deletes item from inventory """
        item_index = list(self.sorted_inventory)[index]
        items_names = []

        for item in self.inventory:  # create a list of items names
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

                            self.inventory.remove(item_index)  # Remove Item from inventory.inventory[]
                            items_names.remove(item_index.name)  # Remove Item from items_names[]

                            if item_index.name == player1_equipment.equipped_weapon_name or \
                                    item_index.name == player1_equipment.equipped_torso_name or \
                                    item_index.name == player1_equipment.equipped_legs_name:

                                # If deleted item is still in inventory.inventory[] -> equip this item
                                if item_index.name in items_names:
                                    # player1.update_attributes()

                                    print('atak: ', player1.attack)
                                    print('obrona: ', player1.defence)
                                    self.show_inventory(0, 0, 0)

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
                                    self.show_inventory(0, 0, 0)

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


inventory = Inventory()  # create instance - Inventory



# Add items to inventory
inventory.add_to_inventory(axe)
inventory.add_to_inventory(knife)
inventory.add_to_inventory(armor)
inventory.add_to_inventory(vest)
inventory.add_to_inventory(jeans)
inventory.add_to_inventory(sweatpants)



class InventoryWindow:

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
                                    if x == 200 and y == 0:
                                        index = 0
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                            item_index.type == 'stamina' or item_index.type == 'health':
                                                player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                                    print('You can wear this item in Statistics')
                                                    ########   Możliwość wyposażenia przedmiotu dodaj

                                    if x == 400 and y == 0:
                                        index = 1
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 600 and y == 0:
                                        index = 2
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 0 and y == 150:
                                        index = 3
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 200 and y == 150:
                                        index = 4
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 400 and y == 150:
                                        index = 5
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 600 and y == 150:
                                        index = 6
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 0 and y == 300:
                                        index = 7
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 200 and y == 300:
                                        index = 8
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 400 and y == 300:
                                        index = 9
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 600 and y == 300:
                                        index = 10
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                    if x == 0 and y == 450:
                                        index = 11
                                        item_index = list(inventory.sorted_inventory)[index]
                                        if item_index.type == 'food' or item_index.type == 'drink' or \
                                                item_index.type == 'stamina' or item_index.type == 'health':
                                            player1.use_item(index, item_index.type, item_index.attribute)
                                        elif item_index.type == 'weapon' or item_index.type == 'torso' or \
                                                item_index.type == 'legs':
                                            print('You can wear this item in Statistics')

                                except IndexError:
                                    break

                                loop = False

                                # Items in Inventory
                                pygame.display.update()
                                clock.tick(FPS)

                        if event.button == 2:
                            break

                        # Delete item
                        if event.button == 3:
                            if button.collidepoint(event.pos):
                                try:
                                    delete_item_from_inventory = inventory.delete_item_from_inventory
                                    
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
            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
                         transparent_on=False)  # Exit

            statistics_buttons(130, 570, 110, 20, '', 25, f'FOOD = {player1.food}', 'needs', player1.food)
            statistics_buttons(250, 570, 110, 20, '', 25, f'DRINK = {player1.drink}', 'needs', player1.drink)
            statistics_buttons(370, 570, 130, 20, '', 25, f'STAMINA = {player1.stamina}', 'needs', player1.stamina)
            statistics_buttons(510, 570, 130, 20, '', 25, f'HEALTH = {player1.health}', 'needs', player1.health)

            # Items in Inventory
            inventory.show_inventory(0, 0, 0)
            pygame.display.update()
            clock.tick(FPS)


inventory_window = InventoryWindow()  # Creates instance - Inventory Window


class EquipItemWindow:

    def open_equip_item_window(self, image, window_name, type, attribute_text):

        while True:
            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN: # click EXIT button
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

                                    if x == 200 and y == 0:
                                        inventory.equip_item(0)
                                    if x == 400 and y == 0:
                                        inventory.equip_item(1)
                                    if x == 600 and y == 0:
                                        inventory.equip_item(2)
                                    if x == 0 and y == 150:
                                        inventory.equip_item(3)
                                    if x == 200 and y == 150:
                                        inventory.equip_item(4)
                                    if x == 400 and y == 150:
                                        inventory.equip_item(5)
                                    if x == 600 and y == 150:
                                        inventory.equip_item(6)
                                    if x == 0 and y == 300:
                                        inventory.equip_item(7)
                                    if x == 200 and y == 300:
                                        inventory.equip_item(8)
                                    if x == 400 and y == 300:
                                        inventory.equip_item(9)
                                    if x == 600 and y == 300:
                                        inventory.equip_item(10)
                                    if x == 0 and y == 450:
                                        inventory.equip_item(11)

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

            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
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
                            equip_item_window.open_equip_item_window('images/weapon.jpg', "Equip Weapon", 'weapon', 'Damage: ')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Press 'TORSO' Button
                    button = pygame.Rect(500, 200, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            equip_item_window.open_equip_item_window('images/torso.jpg', "Equip Torso", 'torso', 'Defence: ')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Press 'LEGS' Button
                    button = pygame.Rect(530, 490, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            equip_item_window.open_equip_item_window('images/legs.jpg', "Equip Legs", 'legs', 'Defence: ')

                if event.type == pygame.MOUSEBUTTONDOWN: # click EXIT button
                    button = pygame.Rect(650, 550, 150, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            return map_window.open_map_window()


                if event.type == pygame.MOUSEBUTTONDOWN: # click Strength + button
                    button = pygame.Rect(250, 0, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.strength += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN: # click Speed + button
                    button = pygame.Rect(250, 50, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.speed += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN: # click Dexterity + button
                    button = pygame.Rect(250, 100, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.dexterity += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN: # click Intelligence + button
                    button = pygame.Rect(250, 150, 35, 35)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            player1.intelligence += 1
                            player1.leveled_up -= 1

                if event.type == pygame.MOUSEBUTTONDOWN: # click Charisma + button
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

            statistics_buttons(0, 500, 245, 50, '', 36, 'EXP:    ' + str(player1.exp) + ' / ' + str(player1.exp_to_next_level),
                                    'exp', player1.exp)
            statistics_buttons(0, 550, 245, 50, '', 36, 'LEVEL:   ' + str(player1.level), 'exp', player1.level)


            # Equipment buttons
            equipment_buttons(380, 420, 100, 50, player1_equipment.equipped_weapon_name, 'Weapon')  # Weapon
            equipment_buttons(500, 200, 100, 50, player1_equipment.equipped_torso_name, '   Torso')  # Torso
            equipment_buttons(530, 490, 100, 50, player1_equipment.equipped_legs_name, '   Legs')  # Legs

            # ESC button
            button_maker(650, 550, 150, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  ESC = Exit', 'white',
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


# create instance of Statistic Window class
statistic_window = StatisticsWindow()


class SearchItem:

    itemsy = [stone, rod, bat, oar, hammer, knife, axe, shirt, vest, jacket, armor, sweatpants, jeans,
              fishing_trouser, military_trousers, insect, rat, fish, dog_food, canned_food, soda, juice, water,
              vodka, painkillers, bandage, energy_drink, coffee, cocaine, board, key]

    def __init__(self):

        self.chest_black_pearl = [rod, bat, oar, hammer, axe, shirt, vest, jacket, sweatpants, jeans, fishing_trouser,
                                  military_trousers, rat, fish, canned_food, insect, soda, juice, water, vodka,
                                  bandage, energy_drink, coffee, board]
        self.random_items_black_pearl = []
        self.found_items_black_pearl = []


        self.chest_bridge = [stone, rod, bat, shirt, vest, jeans, fishing_trouser, insect, rat, fish,water, vodka,
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


        self.chest_hotel = [hammer, knife, axe, shirt, vest, jacket, sweatpants, jeans, insect, rat, dog_food, canned_food,
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
        random_number = get_random_number(1,6)
        for i in range(random_number):
            random_index = random.randint(0, len(chest_location) -1)
            random_items.append(chest_location[random_index])


    def search(self, random_items, found_item_location):
        try:
            random_index = random.randint(0, len(random_items) - 1)  # Searching for random item
            found_item = random_items[random_index]

            # Add item to found items and remove from the chest
            found_item_location.append(found_item)
            random_items.remove(found_item)

            player1.food -= 10
            player1.drink -= 10
            if player1.stamina > 0:
                player1.stamina -= 10
            elif player1.stamina <= 0:
                player1.stamina = 0
                print('You are too tired to search') # todo: Zmień żeby nie dało się wtedy szukać
            player1.exp += 10
            if player1.exp >= player1.exp_to_next_level:
                player1.level_up()

            player1.food_and_drink()

        except ValueError:
            self.show_found_items(found_item_location)
            button_maker(200, 275, 370, 40, 'blue', 'blue', '', 36, "There's nothing more", 'white',
                         transparent_on=False, transparent_off=False)
            pygame.display.update()
            time.sleep(1)

    def add_to_inventory_while_search(self, index, found_item_location):
        if len(inventory.inventory) >= 12:
            button_maker(150, 275, 500, 40, 'blue', 'blue', '', 36, "You don't have a space in your Inventory", 'white',
                         transparent_on=False, transparent_off=False)
            pygame.display.update()
            time.sleep(1.5)
        else:
            item = found_item_location[index]
            inventory.inventory.append(item)
            item_index = list(found_item_location)[index]
            found_item_location.remove(item_index)

    def show_found_items(self, found_item_location):
        x = 0
        y = 0
        for item in found_item_location:
            # icon = pygame.image.load(self.item.icon)     ###### Wyświetlanie grafiki #######
            # display.blit(icon, (300,120))

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

            button_maker(700, 550, 100, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '  Exit', 'white',
                         transparent_on=False)  # Exit

            # Information
            writing_text('', 35, 'LMB = Take Item', 'pure_red', 300, 500)


            # Items in Inventory
            chest.show_found_items(found_item_location)
            pygame.display.update()
            clock.tick(FPS)


chest_inventory = SearchWindow()  # Creates instance of SearchWindow class


class LocationWindow:
    def __init__(self):
        self.locations = ['black_pearl', 'bridge', 'crane', 'flat', 'forest', 'gate', 'hotel', 'office', 'opera',
                          'restaurant', 'soldek', 'basilica', 'supermarket']


    def open_location_window(self, image, window_name, random_items, found_item_location, defence, location_name):

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
                            barricade.open_barricade_window(image, location_window.open_location_window, defence, location_name, window_name, chest_location, found_item_location)

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
            button_maker(0, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '        Search', 'white',
                         transparent_on=False)  # Search
            button_maker(200, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '         Sleep', 'white',
                         transparent_on=False)  # Sleep
            button_maker(400, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '      Barricade', 'white',
                         transparent_on=False)  # Barricade
            button_maker(600, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '          Exit', 'white',
                         transparent_on=False)  # Exit

            # Show DEFENCE stat
            button_maker(20, 20, 220, 40, 'black', 'black', '', 45, 'Defence = ' + str(defence), 'red',
                         transparent_on=False, transparent_off=False)
            # writing_text('', 45, 'Defence: ' + str(self.defence), 'pure_red', 20, 20)

            pygame.display.update()
            clock.tick(FPS)


location_window = LocationWindow()  # Creates an instance of Location class


# Creates map window
class MapWindow:

    def open_map_window(self):
        open_sound = pygame.mixer.Sound('audio/open_sound.wav')
        door_sound = pygame.mixer.Sound('audio/door.wav')
        raven_sound = pygame.mixer.Sound('audio/raven2.wav')
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open an Inventory window
                    button = pygame.Rect(200, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            open_sound.play()
                            inventory_window.open_inventory_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a Statistics window
                    button = pygame.Rect(400, 550, 200, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            open_sound.play()
                            statistic_window.open_statistics_window()


                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Black Pearl" window
                    print(chest.random_items_black_pearl)
                    button = pygame.Rect(575, 430, 135, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/black_pearl.jpg', '"Black Pearl"',
                                                                 chest.random_items_black_pearl, chest.found_items_black_pearl,
                                                                 barricade.black_pearl_defence, 'black_pearl')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Bridge" window
                    button = pygame.Rect(170, 100, 80, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/bridge.jpg', 'Bridge', chest.random_items_bridge,
                                                                 chest.found_items_bridge, barricade.bridge_defence,
                                                                 'bridge')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Crane" window
                    button = pygame.Rect(280, 150, 70, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/crane.jpg', 'Crane', chest.random_items_crane,
                                                                 chest.found_items_crane, barricade.crane_defence,
                                                                 'crane')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Flat" window
                    button = pygame.Rect(500, 175, 50, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/flat.jpg', 'Flat', chest.random_items_flat,
                                                                 chest.found_items_flat, barricade.flat_defence, 'flat')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Forest" window
                    button = pygame.Rect(450, 25, 75, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            raven_sound.play()
                            location_window.open_location_window('images/forest.jpg', 'Forest', chest.random_items_forest,
                                                                 chest.found_items_forest, barricade.forest_defence,
                                                                 'forest')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Gate" window
                    button = pygame.Rect(610, 160, 60, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            if key in inventory.inventory:
                                door_sound.play()
                                location_window.open_location_window('images/open_gate.jpg', 'Gate',
                                                                     chest.random_items_gate,
                                                                     chest.found_items_gate,
                                                                     barricade.gate_defence,
                                                                     'open_gate')

                            elif key not in inventory.inventory:
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

                                    # Window name
                                    pygame.display.set_caption("Closed Gate")

                                    # Add screen image
                                    location_image = pygame.image.load('images/closed_gate.jpg')
                                    display.blit(location_image, (0, 0))

                                    # Add menu buttons
                                    button_maker(600, 550, 200, 40, 'red', 'grey', 'Comic Sans MS', 23,
                                                 '          Exit', 'white',
                                                 transparent_on=False, transparent_off=False)  # Exit

                                    pygame.display.update()
                                    clock.tick(FPS)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Hotel" window
                    button = pygame.Rect(450, 265, 70, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/hotel.jpeg', 'Hotel', chest.random_items_hotel,
                                                                 chest.found_items_hotel, barricade.hotel_defence,
                                                                 'hotel')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Office" window
                    button = pygame.Rect(650, 270, 80, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/office.jpg', 'Office', chest.random_items_office,
                                                                 chest.found_items_office, barricade.office_defence,
                                                                 'office')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Opera House" window
                    button = pygame.Rect(180, 450, 140, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/opera.jpg', 'Opera House', chest.random_items_opera,
                                                                 chest.found_items_opera, barricade.opera_defence,
                                                                 'opera')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Restaurant" window
                    button = pygame.Rect(30, 230, 115, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/restaurant.jpg', 'Restaurant', chest.random_items_restaurant,
                                                                 chest.found_items_restaurant,
                                                                 barricade.restaurant_defence, 'restaurant')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Sołdek" window
                    button = pygame.Rect(200, 310, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/soldek.jpg', '"Sołdek"', chest.random_items_soldek,
                                                                 chest.found_items_soldek, barricade.soldek_defence,
                                                                 'soldek')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "St. Mary's Basilica" window
                    button = pygame.Rect(540, 70, 180, 45)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/basilica.jpg', "St. Mary's Basilica",
                                                                 chest.random_items_basilica, chest.found_items_basilica,
                                                                 barricade.basilica_defence, 'basilica')

                if event.type == pygame.MOUSEBUTTONDOWN:  # Open a "Supermarket" window
                    button = pygame.Rect(10, 50, 135, 40)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            door_sound.play()
                            location_window.open_location_window('images/supermarket.jpg', '"Supermarket"',
                                                                 chest.random_items_supermarket, chest.found_items_supermarket,
                                                                 barricade.supermarket_defence, 'supermarket')

                # Open an Inventory window
                if player1.health <= 20 or player1.food == 0 or player1.drink == 0 or player1.stamina <= 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button = pygame.Rect(760, 10, 25, 25)
                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                open_sound.play()
                                inventory_window.open_inventory_window()

                # Open an Statistics window
                if player1.leveled_up > 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button = pygame.Rect(20, 10, 130, 25)
                        if event.button == 1:
                            if button.collidepoint(event.pos):
                                open_sound.play()
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
            button_maker(600, 550, 200, 40, 'grey', 'pure_red', 'Comic Sans MS', 23, '        Options', 'white',
                         transparent_on=False)  # Options

            pygame.display.update()
            clock.tick(FPS)


map_window = MapWindow()  # Creates instance of MapWindow class


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


main_menu_window = MainMenuWindow()  # Creates instance of MainMenuWindow class


class GameOverWindow:

    def open_game_over_window(self):
        pygame.mixer.music.load('audio/the_end.mp3')
        pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.Rect(270, 400, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            main_menu_window.open_main_menu_window()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.Rect(430, 400, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            # Window settings, graphic and sound
            pygame.display.set_caption('GAME OVER')
            game_over_image = pygame.image.load('images/game_over.jpg')
            display.blit(game_over_image, (0, 0))

            writing_text('', 70, 'GAME OVER', 'red', 250, 150)
            writing_text('', 50, 'Your level: ' + str(player1.level), 'white', 300, 300)
            # writing_text('', 40, 'Again?', 'white', 350, 300)
            # button_maker(270, 400, 100, 50, 'green', 'white', '', 35, 'YES', 'white', transparent_on=False, transparent_off=True)
            # button_maker(430, 400, 100, 50, 'red', 'white', '', 35, 'NO', 'white', transparent_on=False, transparent_off=True)

            pygame.display.update()
            clock.tick(FPS)

# main_menu_window.open_main_menu_window()
if __name__ == '__main__':
    # Put random number of random items into locations
    for chest_location, random_items in chest.locations:
        chest.get_random_items(chest_location, random_items)

    map_window.open_map_window()