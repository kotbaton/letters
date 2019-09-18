class Attribute:
    reset       = 0 
    normal      = 0 
    bold        = 1 
    dim         = 2 
    italic      = 3 
    underscore  = 4 
    negative    = 7 
    strikeout   = 9 


def reset():
    """Reset all aplyed color setting."""
    return "\033[0m"


def by_index(fg_color_index, bg_color_index = 0, attribute = 0):
    """
    Return string with ANSI escape code for set text colors 

    fg_color_index: color index from 0 to 255, applied to text
    bg_color_index: color index from 0 to 255, applied to background
    attribute: use Attribute class variables
    """
    return f"\033[{attribute};38;5;{fg_color_index};48;5;{bg_color_index}m"

def by_hex(fg, bg = "#000000", attribute = 0):
    """
    Return string with ANSI escape code for set text colors 

    fg: html hex code for text color
    bg: html hex code for background color
    attribute: use Attribute class variables
    """
    # Delete #
    fg = fg.replace("#", "")
    bg = bg.replace("#", "")

    fg_r = int(fg[0:2], 16)
    fg_g = int(fg[2:4], 16)
    fg_b = int(fg[4:6], 16)
    fg_rgb = f"{fg_r};{fg_g};{fg_b}"

    bg_r = int(bg[0:2], 16)
    bg_g = int(bg[2:4], 16)
    bg_b = int(bg[4:6], 16)
    bg_rgb = f"{bg_r};{bg_g};{bg_b}"

    return f"\033[{attribute};38;2;{fg_rgb};48;2;{bg_rgb}m"

def get(fg, bg=None, attribute = 0):
    """
    Return string with ANSI escape code for set text colors

    fg: html code or color index for text color
    attribute: use Attribute class variables
    """
    if type(fg) is str:
        bg = bg if bg else "#000000"
        return by_hex(fg, bg, attribute=attribute)

    elif type(fg) is int and 0 <= fg <= 255:
        bg = bg if bg else 0
        return by_index(fg, bg, attribute=attribute)

    else:
        raise  TypeError("You can use only string or int.")
