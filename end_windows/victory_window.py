import sys

import pygame
from clock import clock, FPS
from create import writing_text, button_maker
from display import display



class VictoryWindow:
    def __init__(self):
        pass

    def open_victory_window(self):
        pygame.mixer.music.load('audio/victory_music.mp3')
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
                            pass


                if event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.Rect(430, 400, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            # Window settings, graphic and sound
            pygame.display.set_caption('CONGRATULATIONS!')
            victory_image = pygame.image.load('images/victory_window.jpg')
            display.blit(victory_image, (0, 0))

            writing_text('', 70, 'Congratulations!', 'red', 200, 150)
            # writing_text('', 50, 'Your level: ' + str(player1.level), 'white', 300, 300)
            writing_text('', 40, 'Again?', 'white', 350, 300)
            button_maker(270, 400, 100, 50, 'green', 'white', '', 35, 'YES', 'white', transparent_on=False,
                         transparent_off=True)
            button_maker(430, 400, 100, 50, 'red', 'white', '', 35, 'NO', 'white', transparent_on=False,
                         transparent_off=True)

            pygame.display.update()
            clock.tick(FPS)