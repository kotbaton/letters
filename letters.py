#!/usr/bin/python3
import sys
import fonts

colors = [
    "\033[0m",
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[37m",
    "\033[39m",
]


def print_rainbowed(text, font, spacing = 2):
    for letter_part in font:
        c = 1
        for l in text:
            if ' ' <= l <= '_':
                print(f"{' '*(spacing//2)}",
                      f"{colors[c]}{letter_part[ord(l)-ord(' ')]}{colors[0]}",
                      f"{' '*(spacing//2)}",
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
    print(f"\033[3{fg_color};4{bg_color}m", end="")
    for letter_part in font:
        for l in text:
            if ' ' <= l <= '_':
                print(f"{' '*(spacing//2)}",
                      f"{letter_part[ord(l)-ord(' ')]}",
                      f"{' '*(spacing//2)}",
                      end="", sep="")
            else:
                print(" "*(spacing*2), end="")
        print()
    print("\033[0m", end="")


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:]).upper()
    else:
        text = "some text"

    print()
    print_rainbowed(text,
                    fonts.font1,
                    spacing = 1)
    #  print_attributed(text,
    #                   fonts.font1,
    #                   spacing = 2,
    #                   fg_color = 3,
    #                   bg_color = 0)
    print()


if __name__=="__main__":
    main()
