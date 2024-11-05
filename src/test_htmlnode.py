import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    # test props to html function
    def test_props_to_html(self):
        node2 = HTMLNode("h2", "this is smaller title")
        node3 = HTMLNode("h3", "this is an even smaller title")
        node = HTMLNode("h1", "This is a title", [node2, node3],{"href": "https://www.google.com", "href2": "https://www.notgoogle.com"})
        node4 = HTMLNode("h1", "This is a title")
        expected_props = ' href="https://www.google.com" href2="https://www.notgoogle.com"'
        expected_props_node4 = None
        self.assertEqual(node.props_to_html(), expected_props)
        self.assertEqual(node4.props_to_html(), expected_props_node4)

    # Test repr function

    def test_repr(self):
        node1 = HTMLNode("h2", "this is smaller title")
        node2 = HTMLNode("h3", "this is an even smaller title")
        node3 = HTMLNode("h1", "This is a title", [node1, node2],{"href": "https://www.google.com"})
        node4 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.notgoogle.com"})
        node5 = HTMLNode("h2", "This is a small title", [], {})
        expected_repr_node3 = "HTMLNode Tag:h1 Value:This is a title Children:[HTMLNode Tag:h2 Value:this is smaller title Children:None Props:None, HTMLNode Tag:h3 Value:this is an even smaller title Children:None Props:None] Props:{'href': 'https://www.google.com'}"
        expected_repr_node4 = "HTMLNode Tag:p Value:This is a paragraph Children:None Props:{'href': 'https://www.notgoogle.com'}"
        expected_repr_node5 = "HTMLNode Tag:h2 Value:This is a small title Children:[] Props:{}"
        self.assertEqual(repr(node3), expected_repr_node3)
        self.assertEqual(repr(node4), expected_repr_node4)  
        self.assertEqual(repr(node5), expected_repr_node5)

    # Test LeafNode.to_html 5 Cases

    def test_LeafNode_to_html(self):
        node1 = LeafNode("a", "Click Me!", {"href": "https://www.notgoogle.com"})
        node2 = LeafNode("h1", "A Big Title")
        node3 = LeafNode(None, "just a value")
        node4 = LeafNode("h2", None)
        node5 = LeafNode("h2", "")
        node7 = LeafNode("h1", "This is a title", "this is an incorrect prop")
        expected_html_node1 = '<a href="https://www.notgoogle.com">Click Me!</a>'
        expected_html_node2 = '<h1>A Big Title</h1>'
        expected_html_node3 = 'just a value'
        self.assertEqual(node1.to_html(), expected_html_node1)
        self.assertEqual(node2.to_html(), expected_html_node2)
        self.assertEqual(node3.to_html(), expected_html_node3)
        with self.assertRaises(ValueError):
            node4.to_html()
        with self.assertRaises(ValueError):
            node5.to_html()
        with self.assertRaises(TypeError):
            node6 = LeafNode("h1", "This is a title", [node1, node2], {"href": "https://www.google.com"})
        with self.assertRaises(TypeError):
            node7.to_html()
        
        # test ParentNode.to_html() 
    def test_ParentNode_to_html(self):
        node1 = LeafNode("a", "Click Me!", {"href": "https://www.notgoogle.com"})
        node2 = LeafNode("h1", "A Big Title")
        node3 = ParentNode("body", [node1, node2], None)    #Multiple children
        node4 = ParentNode("head", [node3])                 #Nested ParentNode
        node5 = ParentNode("body", [node1])                 #Single Child
        expected_html_node3 = '<body><a href="https://www.notgoogle.com">Click Me!</a><h1>A Big Title</h1></body>'
        expected_html_node4 = '<head><body><a href="https://www.notgoogle.com">Click Me!</a><h1>A Big Title</h1></body></head>'
        expected_html_node5 = '<body><a href="https://www.notgoogle.com">Click Me!</a></body>'
        self.assertEqual(node3.to_html(), expected_html_node3)
        self.assertEqual(node4.to_html(), expected_html_node4)
        self.assertEqual(node5.to_html(), expected_html_node5)
        with self.assertRaises(ValueError):
            node6 = ParentNode("body", None)                #No children
        with self.assertRaises(ValueError):
            node7 = ParentNode("body", node1)               #Children not in list

if __name__ == "__main__":
    unittest.main()