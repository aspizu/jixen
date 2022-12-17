import sys
from pathlib import Path
from typing import TextIO

from html_transformer import html_to_tree


def html_to_js(html: str) -> str:
    return html_to_tree(html).to_js()


def process(input: TextIO, output: TextIO):
    q = False
    b = ""
    while True:
        c = input.read(1)
        if not c:
            break
        if q:
            if c == "`":
                q = False
                output.write(html_to_js(b))
            else:
                b += c
        else:
            if c == "`":
                q = True
                b = ""
            else:
                output.write(c)


def main():
    if len(sys.argv) < 3:
        print("Usage: jixen /path/to/input.js /path/to/output.js")
        exit(1)
    input = sys.argv[1]
    output = sys.argv[2]

    if input == "-":
        input_file = sys.stdin
    else:
        input_file = Path(input).open("r")
    if output == "-":
        output_file = sys.stdout
    else:
        output_file = Path(output).open("r")

    process(input_file, output_file)


main()
