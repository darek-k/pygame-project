import pygame
from clock import clock, FPS
from create import writing_text, button_maker
from display import display

class VictoryWindow:
    def __init__(self):
        pass


    def open_game_over_window(self):
        pygame.mixer.music.load('audio/the_end.mp3')
        pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     button = pygame.Rect(270, 400, 100, 50)
                #     if event.button == 1:
                #         if button.collidepoint(event.pos):
                #             main_menu_window.open_main_menu_window()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.Rect(430, 400, 100, 50)
                    if event.button == 1:
                        if button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            # Window settings, graphic and sound
            pygame.display.set_caption('GAME OVER')
            game_over_image = pygame.image.load('images/game_over.jpg')
            display.blit(game_over_image, (0, 0))

            writing_text('', 70, 'GAME OVER', 'red', 250, 150)
            # writing_text('', 50, 'Your level: ' + str(player1.level), 'white', 300, 300)
            writing_text('', 40, 'Again?', 'white', 350, 300)
            button_maker(270, 400, 100, 50, 'green', 'white', '', 35, 'YES', 'white', transparent_on=False,
                         transparent_off=True)
            button_maker(430, 400, 100, 50, 'red', 'white', '', 35, 'NO', 'white', transparent_on=False,
                         transparent_off=True)

            pygame.display.update()
            clock.tick(FPS)