from enum import Enum

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
