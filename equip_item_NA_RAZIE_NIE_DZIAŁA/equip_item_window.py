
"""
todo: Na razie nie działa, trzeba przenieść InventoryWindow i StatisticsWindow z pliku file.py
"""



import sys

import pygame

from clock import clock, FPS
from create import button_maker, writing_text
from display import display

from inventory import inventory


class EquipItemWindow:

    @staticmethod
    def open_equip_item_window(image, window_name, type, attribute_text):

        while True:
            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    statistic_window.open_statistics_window()

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
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

                                    equip_item = inventory_window.equip_item

                                    if x == 200 and y == 0:
                                        equip_item(0)
                                    if x == 400 and y == 0:
                                        equip_item(1)
                                    if x == 600 and y == 0:
                                        equip_item(2)
                                    if x == 0 and y == 150:
                                        equip_item(3)
                                    if x == 200 and y == 150:
                                        equip_item(4)
                                    if x == 400 and y == 150:
                                        equip_item(5)
                                    if x == 600 and y == 150:
                                        equip_item(6)
                                    if x == 0 and y == 300:
                                        equip_item(7)
                                    if x == 200 and y == 300:
                                        equip_item(8)
                                    if x == 400 and y == 300:
                                        equip_item(9)
                                    if x == 600 and y == 300:
                                        equip_item(10)
                                    if x == 0 and y == 450:
                                        equip_item(11)

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
