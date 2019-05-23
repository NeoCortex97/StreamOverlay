# -*- coding: utf-8 -*-
import random


def SimpleBox(width, height):
    """Generator for simple boxes from box characters.
    :param width: sets the width of the box.
    :param height: sets the height of the box.
    """
    for i in range(height):
        yield "█" * width


def RandomBox(width, height):
    """Generator for random borders around boxes.
    :param width: sets the outer width of the box.
    :param height: sets the outer height of the box.
    """
    chars = ["█", "▀", "▄", "▌", "▐", "▖", "▗", "▘", "▙", "▚", "▛", "▜", "▝", "▞", "▟", " "]
    yield "".join(random.choices(chars, k=width))
    for line in SimpleBox(width - 2, height - 2):
        yield random.choice(chars) + line + random.choice(chars)
    yield "".join(random.choices(chars, k=width))


if __name__ == "__main__":
    for line in RandomBox(20, 12):
        print("  " + line)
