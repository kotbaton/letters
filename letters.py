#!/usr/bin/python3
import sys
import argparse

import font
import printer

def get_parser():
    parser = argparse.ArgumentParser(description="Print text in different ways.")
    group = parser.add_mutually_exclusive_group()

    def process_color_arg(arg):
        try:
            return int(arg)
        except:
            return arg

    group.add_argument("-c", "--color",
                        nargs='+',
                        type=process_color_arg,
                        help="Set text color by color index or html code. First value will be used as text color and second as background color.")
    group.add_argument("-r", "--rainbow",
                        action="store_true",
                        help="Print with different colors.")
    parser.add_argument("-s", "--spacing",
                        nargs=1,
                        default=[2],
                        action="store",
                        type=int,
                        help="Set space between letters. (default = 2)")
    parser.add_argument("-t", "--text",
                        nargs='*',
                        type=str,
                        help="Text for printing.")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.rainbow:
        text = " ".join(args.text).upper()
        printer.rainbow(text,
                        font.font1,
                        spacing = args.spacing[0])
    elif args.color:
        text = " ".join(args.text).upper()
        printer.attributed(text,
                           font.font1,
                           spacing = args.spacing[0],
                           fg = args.color[0],
                           bg = args.color[1] if len(args.color) > 1 else None)
    else:
        parser.print_help()


if __name__=="__main__":
    main()
