import operator

from create import button_maker, writing_text
from player import player1_equipment


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self, count_weapon, count_torso, count_legs):
        x = 0
        y = 0
        font_size = 40
        font_size_text = 35

        self.sorted_inventory = sorted(self.inventory, key=operator.attrgetter('type', 'name'))

        for item in self.sorted_inventory:

            if item.type == 'weapon':
                text = 'Damage: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'orange', x, y + 50)

            if item.type == 'torso' or item.type == 'legs':
                text = 'Defence: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'violet', x, y + 50)

            if item.type == 'food':
                text = 'Food: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'brown', x, y + 50)

            if item.type == 'drink':
                text = 'Drink: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'blue', x, y + 50)

            if item.type == 'health':
                text = 'Health: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'green', x, y + 50)

            if item.type == 'stamina':
                text = 'Stamina: '
                button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'white')
                writing_text('', font_size_text, text + str(item.attribute), 'yellow', x, y + 50)

            if item.type == 'other':
                text = ''
                button_maker(x, y, item.size_x, item.size_y, 'gold', 'blue', '', font_size, item.name, 'gold')
                writing_text('', font_size_text, text + str(item.attribute), 'gold', x, y + 50)

            # Make equipped items GREEN
            if count_weapon == 0:
                if item.name == player1_equipment.equipped_weapon_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'ultra_green')
                    writing_text('', font_size_text, text + str(item.attribute), 'orange', x, y + 50)
                    count_weapon += 1

            if count_torso == 0:
                if item.name == player1_equipment.equipped_torso_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'ultra_green')
                    writing_text('', font_size_text, text + str(item.attribute), 'violet', x, y + 50)
                    count_torso += 1

            if count_legs == 0:
                if item.name == player1_equipment.equipped_legs_name:
                    button_maker(x, y, item.size_x, item.size_y, 'red', 'blue', '', font_size, item.name, 'ultra_green')
                    writing_text('', font_size_text, text + str(item.attribute), 'violet', x, y + 50)
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


inventory = Inventory()
