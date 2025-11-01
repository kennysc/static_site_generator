import unittest

from htmlnode import HTMLNode, LeafNode

props_1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}
props_1_html = ' href="https://www.google.com" target="_blank"'
props_2 = {
    "id": "main-container",
    "class": "content-wrapper highlighted",
    "style": "color: #333; background-color: #f9f9f9; padding: 10px;",
    "title": "Example tooltip text",
}
props_2_html = ' id="main-container" class="content-wrapper highlighted" style="color: #333; background-color: #f9f9f9; padding: 10px;" title="Example tooltip text"'


class TestHTMLNode(unittest.TestCase):
    def test_props_format_1(self):
        node = HTMLNode(props=props_1)
        self.assertEqual(node.props_to_html(), props_1_html)

    def test_props_format_2(self):
        node = HTMLNode(props=props_2)
        self.assertEqual(node.props_to_html(), props_2_html)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello World!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode("div", "Hello, world!",{"href": "http://192.168.0.1"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(div, Hello, world!, {'href': 'http://192.168.0.1'})"
        )

    def test_leaf_values(self):
        node = LeafNode(
            "p",
            "This is a leaf Node",
            {"href": "https//duckduckgo.com"}
        )

        self.assertEqual(
            node.tag,
            "p")

        self.assertEqual(
            node.value,
            "This is a leaf Node")

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            {"href": "https//duckduckgo.com"}
        )

if __name__ == "__main__":
    unittest.main()
