import unittest

from text_to_nodes import text_to_textnodes
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_text_to_textnodes(self):
            # Test 1: Plain text only
        text = "This is plain text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "This is plain text"
        assert nodes[0].text_type == TextType.TEXT
        
        # Test 2: Bold text
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == " text"

        # Test 3: Italic text
        text = "This is *italic* text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[1].text == "italic"
        assert nodes[1].text_type == TextType.ITALIC
        # Test 4: combination of all
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
        TextNode("This is ", TextType.TEXT, None), 
        TextNode("text", TextType.BOLD, None), 
        TextNode(" with an ", TextType.TEXT, None), 
        TextNode("italic", TextType.ITALIC, None), 
        TextNode(" word and a ", TextType.TEXT, None), 
        TextNode("code block", TextType.CODE, None), 
        TextNode(" and an ", TextType.TEXT, None), 
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
        TextNode(" and a ", TextType.TEXT, None), 
        TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(text_to_textnodes(text), expected)