from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        text_eq = self.text == text_node.text
        type_eq = self.text_type == text_node.text_type
        url_eq = self.url == text_node.url
        return text_eq and type_eq and url_eq

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    text_node_val = text_node.text_type

    if text_node_val == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node_val == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node_val == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node_val == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node_val == TextType.LINK:
        return LeafNode(
            "a",
            text_node.text,
            {"href": f"{text_node.url}"},
        )
    if text_node_val == TextType.IMAGE:
        return LeafNode(
            "img",
            "",
            {"src": f"{text_node.url}",
             "alt": f"{text_node.text}",
             },
        )
    raise ValueError(f"Unsupported type: {text_node_val}")
