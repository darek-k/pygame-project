# Function that makes interactive buttons
import pygame

from create import colors
from display import display


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

def statistics_buttons(x, y, w, h, font, font_size, text_input, stat_group, stat_points):
    global color
    text_color = colors['black']

    if stat_group == 'needs':
        if stat_points >= 70:
            color = colors['green']
        elif stat_points < 70 and stat_points >= 30:
            color = colors['yellow']
        elif stat_points < 30:
            color = colors['red']

    elif stat_group == 'fight':
        color = colors['light_cream']

    elif stat_group == 'exp':
        color = colors['black']
        text_color = colors['white']

    elif stat_group == 'attribute':
        color = colors['dark_cream']

    pygame.draw.rect(display, (color), (x, y, w, h))
    my_font = pygame.font.SysFont(font, font_size)
    text = my_font.render(text_input, True, (text_color))
    display.blit(text, (x + 1, y + 2))


def equipment_buttons(x, y, w, h, item_name, item_type):
    # item_name - name of the equipped item
    if item_name == '':
        button_maker(x, y, w, h, 'black', 'pure_red', 'Comic Sans MS', 23, item_type, 'white',
                     text_on=False, )
    else:
        item = item_name
        button_maker(x, y, w, h, 'black', 'pure_red', 'Comic Sans MS', 23, item, 'white',
                     text_on=True, )