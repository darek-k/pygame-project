# main_menu_window.open_main_menu_window()
from file import chest, map_window

if __name__ == '__main__':
    # Put random number of random items into locations
    for chest_location, random_items in chest.locations:
        chest.get_random_items(chest_location, random_items)

    map_window.open_map_window()