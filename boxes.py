# -*- coding: utf-8 -*-
import random


def SimpleBox(width, height):
    for i in range(height):
        yield "█" * width


def RandomBox(width, height):
    chars = ["█", "▀", "▄", "▌", "▐", "▖", "▗", "▘", "▙", "▚", "▛", "▜", "▝", "▞", "▟", " "]
    yield "".join(random.choices(chars, k=width))
    for line in SimpleBox(width - 2, height - 2):
        yield random.choice(chars) + line + random.choice(chars)
    yield "".join(random.choices(chars, k=width))


if __name__ == "__main__":
    for line in RandomBox(20, 12):
        print("  " + line)