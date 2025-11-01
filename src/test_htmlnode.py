import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
