import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_nontext(self):
        node = TextNode("This is all bold", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [TextNode("This is all bold", TextType.BOLD)]
        )
    def test_mismatched_delimiter(self):
        node = TextNode("This is _italic text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_delimiter_start(self):
        node = TextNode("_Italic text_ delimiter at the start", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC),
            [TextNode("Italic text", TextType.ITALIC),
             TextNode(" delimiter at the start", TextType.TEXT)]
        )

    def test_delimiter_end(self):
        node = TextNode("delimiter at **the end**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node],"**", TextType.BOLD),
            [TextNode("delimiter at ", TextType.TEXT),
             TextNode("the end", TextType.BOLD)]
        )

    def test_multiple_delimiter(self):
        node = TextNode("`code here` and also `here!`", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node],"`", TextType.CODE),
            [TextNode("code here", TextType.CODE),
             TextNode(" and also ", TextType.TEXT),
            TextNode("here!", TextType.CODE)]
        )

if __name__ == "__main__":
    unittest.main()
