import unittest

from .html_tree import Attr, Element


class TestHTMLTree(unittest.TestCase):
    def tests(self):
        self.assertEqual(
            Element("div", "alias", [Attr("class", '"classname"')], []).to_js(),
            '(()=>{let alias=document.createElement("div");alias.classList="classname";return alias;})()',
        )
