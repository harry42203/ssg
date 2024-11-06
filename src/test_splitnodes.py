import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestHTMLNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):   
        node1 = TextNode("This is a *text* node", TextType.TEXT)
        node2 = TextNode("This *Should* be a *text* node", TextType.TEXT)
        node3 = TextNode("This is *not* a text node",TextType.CODE)
        old_nodes = [node1, node2, node3]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        expected_list = [
            TextNode("This is a ", TextType.TEXT, None), 
            TextNode("text", TextType.BOLD, None), 
            TextNode(" node", TextType.TEXT, None), 
            TextNode("This ", TextType.TEXT, None), 
            TextNode("Should", TextType.BOLD, None), 
            TextNode(" be a ", TextType.TEXT, None), 
            TextNode("text", TextType.BOLD, None), 
            TextNode(" node", TextType.TEXT, None), 
            TextNode("This is *not* a text node", TextType.CODE, None)
            ]
        self.assertEqual(new_nodes, expected_list)
           
        node4 = TextNode("This is a *text node*", TextType.TEXT)
        node5 = TextNode("This *Should be a text* node", TextType.TEXT)
        node6 = TextNode("*This is not* a text node",TextType.CODE)
        old_nodes_2 = [node4, node5, node6]
        new_nodes_2 = split_nodes_delimiter(old_nodes_2, "*", TextType.ITALIC)
        expected_list_2 = [
            TextNode("This is a ", TextType.TEXT, None),                
            TextNode("text node", TextType.ITALIC, None), 
            TextNode("This ", TextType.TEXT, None), 
            TextNode("Should be a text", TextType.ITALIC, None), 
            TextNode(" node", TextType.TEXT, None), 
            TextNode("*This is not* a text node", TextType.CODE, None)
            ]
        self.assertEqual(new_nodes_2, expected_list_2)

    def test_split_nodes_image(self):
        node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        node2 = TextNode(
        "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        nodes = [node, node2]
        expected = [
            TextNode("This is text with a ", TextType.TEXT, None), 
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), 
            TextNode(" and ", TextType.TEXT, None), 
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT, None)
            ]
        self.assertEqual(split_nodes_image(nodes), expected)

        # Test 1: Basic image splitting
        node = TextNode("Hello ![alt](http://example.com)", TextType.TEXT)
        nodes = split_nodes_image([node])
        assert len(nodes) == 2
        assert nodes[0].text == "Hello "
        assert nodes[1].text == "alt"
        assert nodes[1].url == "http://example.com"

        # Test 2: Multiple images
        node = TextNode(
            "![first](one.jpg) middle ![second](two.jpg)", 
            TextType.TEXT
        )
        nodes = split_nodes_image([node])
        assert len(nodes) == 3
        assert nodes[0].text == "first"
        assert nodes[1].text == " middle "
        assert nodes[2].text == "second"

        # Test 3: No images
        node = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_image([node])
        assert len(nodes) == 1
        assert nodes[0].text == "Just plain text"

        # Test 4: Non-text node should pass through unchanged
        node = TextNode("example", TextType.LINK, "http://example.com")
        nodes = split_nodes_image([node])
        assert len(nodes) == 1
        assert nodes[0].text == "example"
        assert nodes[0].text_type == TextType.LINK

    def test_split_nodes_link(self):
        node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        node2 = TextNode(
        "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        nodes = [node, node2]
        expected = [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT, None), 
            TextNode("This is text with a ", TextType.TEXT, None), 
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"), 
            TextNode(" and ", TextType.TEXT, None), 
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        self.assertEqual(split_nodes_link(nodes), expected)
            # Test 1: Basic link splitting
        node2 = TextNode("Here's a [link](http://example.com)", TextType.TEXT)
        nodes2 = split_nodes_link([node2])
        assert len(nodes2) == 2
        assert nodes2[0].text == "Here's a "
        assert nodes2[1].text == "link"
        assert nodes2[1].url == "http://example.com"
            # Test 2: Multiple links
        node3 = TextNode(
            "This has [two](test1.com) separate [links](test2.com)", 
            TextType.TEXT
        )
        nodes3 = split_nodes_link([node3])
        assert len(nodes3) == 4
        assert nodes3[0].text == "This has "
        assert nodes3[1].text == "two"
        assert nodes3[1].url == "test1.com"
        assert nodes3[2].text == " separate "
        assert nodes3[3].text == "links"
        assert nodes3[3].url == "test2.com"

        # Test 3: No links
        node4 = TextNode("Just plain text", TextType.TEXT)
        nodes4 = split_nodes_link([node4])
        assert len(nodes4) == 1
        assert nodes4[0].text == "Just plain text"

        # Test 4: Link at start
        node5 = TextNode("[start](test.com) then text", TextType.TEXT)
        nodes5 = split_nodes_link([node5])
        assert len(nodes5) == 2
        assert nodes5[0].text == "start"
        assert nodes5[0].url == "test.com"
        assert nodes5[1].text == " then text"

                # Test 5: Link at end
        node6 = TextNode("text then [end](test.com)", TextType.TEXT)
        nodes6 = split_nodes_link([node6])
        assert len(nodes6) == 2
        assert nodes6[0].text == "text then "
        assert nodes6[1].text == "end"
        assert nodes6[1].url == "test.com"
        assert nodes6[1].text_type == TextType.LINK

if __name__ == "__main__":
    unittest.main()