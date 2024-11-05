import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):   
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

        node7 = TextNode("This is a *text node*", TextType.TEXT)
        node8 = TextNode("This *Should be a text* node", TextType.TEXT)
        node9 = TextNode("*This is not* a text node",TextType.CODE)
        old_nodes_3 = [node7, node8, node9]
        with self.assertRaises(Exception):
            new_nodes_3 = split_nodes_delimiter(old_nodes_3, "^", TextType.ITALIC)

        node10 = TextNode("This is a *text node", TextType.TEXT)
        node11 = TextNode("This *Should be a text* node", TextType.TEXT)
        node12 = TextNode("*This is not* a text node",TextType.CODE)
        old_nodes_4 = [node10, node11, node12]
        with self.assertRaises(Exception):
            new_nodes_4 = split_nodes_delimiter(old_nodes_4, "*", TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()