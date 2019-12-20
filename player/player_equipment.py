

class PlayerEquipment():
    def __init__(self):
        self.equipped_items = []

        self.equipped_weapon_name = ''
        self.equipped_weapon_ID = ''
        self.equipped_weapon_attribute = 0
        self.equipped_torso_name = ''
        self.equipped_torso_attribute = 0
        self.equipped_legs_name = ''
        self.equipped_legs_attribute = 0

    def put_equipped_items_into_container(self, item):
        self.equipped_items.append(item)
        item_index = self.equipped_items.index(item)
        # del inventory.inventory[item_index]



player1_equipment = PlayerEquipment()