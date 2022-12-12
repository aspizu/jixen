from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Union


class Node(ABC):
    @abstractmethod
    def to_js(self, alias: Optional[str]) -> str:
        ...


class Js(str, Node):
    """Represents inline javascript code"""

    def __repr__(self) -> str:
        return f"Js({self})"

    def to_js(self, alias: Optional[str]) -> str:
        return str(self)


class Text(str, Node):
    """Represents text inside HTML tags"""

    def __repr__(self) -> str:
        return f"Text({self})"

    def to_js(self, alias: Optional[str]) -> str:
        return repr(str(self))


@dataclass
class Attr(Node):
    """Represents a HTML attribute"""

    name: str  # name of HTML attribute
    value: Union[Js, Text]  # value of HTML attribute

    def to_js(self, alias: Optional[str]) -> str:
        if self.name == "class":
            return f"{alias}.classList={self.value.to_js(alias)};"
        if self.name.startswith("on"):
            return f'{alias}.addEventListener("{self.name[2:]}",()=>{{{self.value.to_js(alias)}}});'
        else:
            return f"{alias}.{self.name}={self.value};"


@dataclass
class Element(Node):
    """Represents a HTML element"""

    name: str  # Tag name of HTML element
    alias: str  # Variable name to be used instead of `e`
    attrs: list[Attr]  # list of HTML attributes
    children: list[Node]

    def to_js(self, alias: Optional[str] = None) -> str:
        code: list[str] = []
        code.append(f'let {self.alias}=document.createElement("{self.name}");')
        for child in self.children:
            code.append(f"{self.alias}.append({child.to_js(self.alias)});")
        for attr in self.attrs:
            code.append(attr.to_js(self.alias))
        code.append(f"return {self.alias};")
        return "(()=>{" + "".join(code) + "})()"
