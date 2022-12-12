import sys
from pathlib import Path
from typing import TextIO

from html_parser import html_parser
from html_transformer import HTMLTransformer


def html_to_js(html: str) -> str:
    return HTMLTransformer().transform(html_parser.parse(html)).to_js()


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


def main(input: Path, output: Path):
    with input.open("r") as input_fp:
        with output.open("w") as output_fp:
            process(input_fp, output_fp)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: jixen /path/to/input.js /path/to/output.js")
        exit(1)
    input = Path(sys.argv[1])
    output = Path(sys.argv[2])
    if not input.is_file():
        raise FileNotFoundError(input)

    main(input, output)
