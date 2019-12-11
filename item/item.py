# Items class
class Item:
    def __init__(self, name, attribute, type, icon):
        self.name = name
        self.attribute = attribute
        self.size_x = 200
        self.size_y = 150
        self.icon = icon
        self.type = type