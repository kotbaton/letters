#!/usr/bin/python3
import sys
import fonts
import color


def print_rainbowed(text, font, spacing = 2):
    for letter_part in font:
        c = 1
        for l in text:
            if ' ' <= l <= '_':
                print(" "*(spacing//2),
                      color.by_index(c),
                      letter_part[ord(l)-ord(' ')],
                      color.reset(),
                      " "*(spacing//2),
                      end="", sep="")
                c = c+1 if c<7 else 1
            else:
                print(" "*(spacing*2), end="")
        print()


def print_attributed(text,
                     font,
                     spacing = 2,
                     fg_color = 9,
                     bg_color = 0):
    print(color.by_index(fg_color, bg_color), end="")
    for letter_part in font:
        for l in text:
            if ' ' <= l <= '_':
                print(" "*(spacing//2),
                      letter_part[ord(l)-ord(' ')],
                      " "*(spacing//2),
                      end="", sep="")
            else:
                print(" "*(spacing*2), end="")
        print()
    print(color.reset(), end="")


def main():
    text = "some text".upper()
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).upper()

    print()
    print_rainbowed(text,
                    fonts.font1,
                    spacing = 2)
    #  print_attributed(text,
    #                   fonts.font1,
    #                   spacing = 2,
    #                   fg_color = 3,
    #                   bg_color = 0)
    print()


if __name__=="__main__":
    main()
