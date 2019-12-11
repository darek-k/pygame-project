from file import map_window
from search import chest

if __name__ == '__main__':
    """Put random number of random items into locations"""
    for chest_location, random_items in chest.locations:
        chest.get_random_items(chest_location, random_items)

    map_window.open_map_window()
