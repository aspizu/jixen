from importlib.resources import open_text

from lark import Lark

html_parser = Lark(open_text("res", "html.lark").read())
