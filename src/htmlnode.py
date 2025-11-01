class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "'to_html' function needs to be override by child classes"
        )

    def props_to_html(self):
        props_list = []
        if self.props:
            for k, v in self.props.items():
                props_list.append(f" {k}=\"{v}\"")
            return "".join(props_list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        # If props is None it would add "None" in the middle of the html string
        # so if it's None replace it by an empty sting
        if self.props is None:
            str_props = ""
        else:
            str_props = self.props_to_html()
        return f"<{self.tag}{str_props}>{self.value}</{self.tag}>"

    def __repr__(self):
        # Override the __repr__ of the parent class to not have the children
        # represented since there cant be one
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
