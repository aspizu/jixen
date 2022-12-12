from typing import Any

from html_tree import Attr, Element, Js
from lark import Token, Transformer


class HTMLTransformer(Transformer[Token, Element]):
    def start(self, args: list[Any]) -> Element:
        return args[0]

    def tag(self, args: list[Any]) -> Element:
        if args[0].children[0] != args[-1].children[0]:
            raise Exception("Tag mismatch")
        return Element(
            name=args[0].children[0],
            alias=args[0].children[1] or "e",
            attrs=args[0].children[2:],
            children=args[1:-1],
        )

    def attr(self, args: list[Any]) -> Attr:
        return Attr(name=args[0], value=args[1])

    def js(self, args: list[Any]) -> Js:
        return Js("".join(args)[1:-1])

    def js_(self, args: list[Any]) -> str:
        return "{" + "".join(args) + "}"
