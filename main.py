from file import map_window, main_menu_window
from search import chest

if __name__ == '__main__':
    """Put random number of random items into locations"""
    for chest_location, random_items in chest.locations:
        chest.get_random_items(chest_location, random_items)

    main_menu_window.open_main_menu_window()
    map_window.open_map_window()

