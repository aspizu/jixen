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
        return self


@dataclass
class Attr(Node):
    """Represents a HTML attribute"""

    name: str  # name of HTML attribute
    value: Union[Js, str]  # value of HTML attribute

    def to_js(self, alias: Optional[str]) -> str:
        if self.name == "class":
            return f"{alias}.classList={self.value};"
        if self.name.startswith("on"):
            return f"{alias}.addEventListener('{self.name[2:]}',()=>{{{self.value}}});"
        else:
            return f"{alias}.{self.name}={self.value};"


@dataclass
class Element(Node):
    """Represents a HTML element"""

    name: str  # Tag name of HTML element
    alias: str  # Variable name to be used instead of `e`
    attrs: list[Attr]  # list of HTML attributes
    children: list[Union[Node, str]]

    def to_js(self, alias: Optional[str] = None) -> str:
        code: list[str] = []
        for child in self.children:
            if isinstance(child, Node):
                js = child.to_js(self.alias)
            else:
                js = child
            code.append(f"{self.alias}.append({js});")
        for attr in self.attrs:
            code.append(attr.to_js(self.alias))

        return f'(()=>{{let {self.alias}=document.createElement("{self.name}");{"".join(code)}return {self.alias};}})()'
