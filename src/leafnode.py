from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props is None:
            str_props = ""
        else:
            str_props = self.props_to_html()
        return f"<{self.tag}{str_props}>{self.value}</{self.tag}>"
