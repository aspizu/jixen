import unittest

from .html_transformer import html_to_tree
from .html_tree import Attr, Element, Text


class TestHTMLTree(unittest.TestCase):
    def tests(self):
        self.assertEqual(
            Element("div", "alias", [Attr("class", Text("classname"))], []).to_js(),
            '(()=>{let alias=document.createElement("div");alias.classList="classname";return alias;})()',
        )


class TestHTMLParser(unittest.TestCase):
    def tests(self):
        self.assertEqual(
            html_to_tree('<div:alias class="classname">"Text child"</div>'),
            Element(
                "div",
                "alias",
                [Attr("class", Text("classname"))],
                [Text("classname")],
            ),
        )


x: int = '1'