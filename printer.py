import color
import font

def __print(text,
            spacing = 2,
            fg = 15,
            bg = 0,
            attribute = 0):
    # Calculate spacing before and after printed text
    if spacing % 2 == 0:
        spacing = (spacing//2, spacing//2)
    else:
        spacing = (spacing//2+1, spacing//2)
    print(" "*spacing[0],
          color.get(fg, bg, attribute=attribute),
          text,
          color.reset(),
          " "*spacing[1],
          end="", sep="")


def rainbow(text,
            font = font.font1,
            spacing = 2,
            attribute = 0):
    text = text.upper()
    for letter_part in font:
        c = 1
        for l in text:
            if ' ' <= l <= '_':
                __print(letter_part[ord(l)-ord(' ')],
                        spacing=spacing, fg=c, attribute=attribute)
                c = c+1 if c<7 else 1
            else:
                __print(letter_part[ord(' ')])
        print()


def attributed(text,
               font = font.font1,
               spacing = 2,
               fg = 9,
               bg = 0,
               attribute = 0):
    text = text.upper()
    for letter_part in font:
        for l in text:
            if ' ' <= l <= '_':
                __print(letter_part[ord(l)-ord(' ')],
                        spacing=spacing,
                        fg=fg,
                        bg=bg,
                        attribute=attribute)
            else:
                print(" "*(spacing*2), end="")
        print()
