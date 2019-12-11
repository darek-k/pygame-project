import sys
import time

import pygame
from display import display

from clock import clock, FPS
from create import button_maker, statistics_buttons, writing_text
from player import player1


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

                if event.type == pygame.MOUSEBUTTONDOWN:  # click EXIT button
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
