import pygame

# Writing text function
from create import colors
from main import display


def writing_text(font, font_size, text_input, color, x, y):
    my_font = pygame.font.SysFont(font, font_size)
    text = my_font.render(text_input, True, (colors[color]))
    display.blit(text, (x, y))


# Function that makes interactive buttons
def button_maker(x, y, w, h, color_on, color_off, font, font_size, text_input, text_color,
                 transparent_on=True, transparent_off=True, text_on=True):
    mouse_position = pygame.mouse.get_pos()

    # Active button
    if x + w > mouse_position[0] > x and y + h > mouse_position[1] > y:
        pygame.draw.rect(display, (colors[color_on]), (x, y, w, h), transparent_on)
        my_font = pygame.font.SysFont(font, font_size)
        text = my_font.render(text_input, True, (colors[text_color]))
        display.blit(text, (x + 1, y + 2))

    # Non active button
    else:
        pygame.draw.rect(display, (colors[color_off]), (x, y, w, h), transparent_off)
        if text_on:
            my_font = pygame.font.SysFont(font, font_size)
            text = my_font.render(text_input, True, (colors[text_color]))
            display.blit(text, (x + 1, y + 2))