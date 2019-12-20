from inventory import inventory


class ItemsNamesList:
    """ Create list with items names """

    def items_names_list(self):
        return [item.name for item in inventory.inventory]
