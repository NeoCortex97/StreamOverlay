# -*- coding: utf-8 -*-


# +----+
# |    |
# +----+
"""
A Function that takes a list or generator and draws a border around it.
"""
def AsciiBorder(content, width, footer=False, height=3):
    yield "+" + ("-" * (width - 2)) + "+"
    for line in content:
        if len(line) == width - 2:
            yield "|" + line + "|"
        elif len(line) < width - 2:
            yield "|" + line + (" " * ((width - 2) - len(line))) + "|"
    yield "+" + ("-" * (width - 2)) + "+"
    if footer:
        for i in range(height - 1):
            yield "|" + (" " * (width - 2)) + "|"
        yield "+" + ("-" * (width - 2)) + "+"


# TODO: Elegant unicode magic :-)
def get_style(style="double"):
    if style == "double":
        return "╔", "╚", "╗", "╝", "║", "═", "╣", "╠"
    elif style == "bold":
        return "┏", "┗", "┓", "┛", "┃", "━", "┫", "┣"
    elif style == "thin":
        return "┌", "└", "┐", "┘", "│", "─", "┤", "├"
    elif style == "rounded":
        return "╭", "╰", "╮", "╯", "│", "─", "┤", "├"


def BoxCaracterBorder(content, width, footer=False, height=3, style="double"):
    clu, cld, cru, crd, ver, hor, lcr, rcr = get_style(style)
    yield clu + (hor * (width - 2)) + cru
    for line in content:
        if len(line) == width - 2:
            yield ver + line + ver
        elif len(line) < width - 2:
            yield ver + line + (" " * ((width - 2) - len(line))) + ver
    if footer:
        yield rcr + (hor * (width - 2)) + lcr
        for i in range(height - 1):
            yield ver + (" " * (width - 2)) + ver
    yield cld + (hor * (width - 2)) + crd


# TODO: Make a border that is a spacer!
def SpaceBorder(content, width, x_thickness, y_thickness):
    pass


if __name__ == "__main__":
    data = ["Hallo Twitch"]
    for line in BoxCaracterBorder(data, 20, footer=True, height=1, style="rounded"):
        print("  " + line)