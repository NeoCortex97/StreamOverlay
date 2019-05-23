# -*- coding: utf-8 -*-


# +----+
# |    |
# +----+
def AsciiBorder(content, width, footer=False, height=3):
    """Generator to encapsulate some array or generator with an border made from ascii characters.
    
    :param content: content you want to encapsulate
    :type content: list
    :param width: width border regardless of content width
    :type width: int
    :param footer: draw a second box below the main one
    :type footer: boolean
    :param height: the height of the second footer box
    :type height: int
    """
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
    """takes a Style and return a set of border characters.
    :param style: the style you want to pick
    :type style: str
    """
    if style == "double":
        return "╔", "╚", "╗", "╝", "║", "═", "╣", "╠"
    elif style == "bold":
        return "┏", "┗", "┓", "┛", "┃", "━", "┫", "┣"
    elif style == "thin":
        return "┌", "└", "┐", "┘", "│", "─", "┤", "├"
    elif style == "rounded":
        return "╭", "╰", "╮", "╯", "│", "─", "┤", "├"


def BoxCaracterBorder(content, width, footer=False, height=3, style="double"):
    """Generator to encapsulate some content with border characters.

    :param content: the content you want to encapsulate
    :type content: list
    :param width: width of the border regardless of content width
    :type width: int
    :param footer: draw a second box below the main one
    :type footer: boolean
    :param height: height of the second footer box
    :type height: int
    :param style: the style of the border
    :type style: str
    """
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
    """Generator to encapsulate content with spaces

    :param content: The content to encapsulate
    :type content: list
    :param width: width of the border
    :type width: int
    :param x_thickness: count of spaces right and left
    :type x_thickness: int
    :param y_thickness: anount of blank lines
    :type y_thickness: int
    """
    pass


if __name__ == "__main__":
    data = ["Hallo Twitch"]
    for line in BoxCaracterBorder(data, 20, footer=True, height=1, style="rounded"):
        print("  " + line)
