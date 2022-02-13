from colored import attr, fg, names, stylize
from colour import Color
import random

def rprint(text, seq=0, **kwargs):
    sequences = [
        color_sequence,
        gradient
    ]
    color = sequences[seq](**kwargs)
    colored_chars = []

    for char in text:
        text_color = next(color)
        style = stylize(char, fg(text_color), attr(0))
        colored_chars.append(style)

    print(''.join(colored_chars))

def color_sequence():
    colors = names[19:230]
    index = random.randint(0, len(colors) - 1)

    while True:
        yield colors[index].lower()
        index = (1 + index) % len(colors)

def gradient(**kwargs):
    start = Color(kwargs['start']) if kwargs else Color('red')
    end   = Color(kwargs['end'])   if kwargs else Color('blue')
    colors = list(start.range_to(end, 256))
    index  = random.randint(0, len(colors) - 1)

    while True:
        yield colors[index].get_hex()
        index = (1 + index) % len(colors)