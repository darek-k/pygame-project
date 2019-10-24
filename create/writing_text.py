import pygame

from create import colors
from display import display


def writing_text(font, font_size, text_input, color, x, y):
    my_font = pygame.font.SysFont(font, font_size)
    text = my_font.render(text_input, True, (colors[color]))
    display.blit(text, (x, y))