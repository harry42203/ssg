import unittest

from textnode import text_node_to_html_node, TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("this is a third text node", TextType.ITALIC, "http://www.notgoogle.com/")
        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node3, node4)
        self.assertEqual(node2, node5)
        self.assertFalse(node.__eq__(node4))
        self.assertTrue(node.__eq__(node2))

    def test_repr(self):
        node = TextNode("print('hello, world')", TextType.CODE, "http://pythoniseasy.com")
        expected_repr = "TextNode(print('hello, world'), TextType.CODE, http://pythoniseasy.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_text_node_to_html_node(self):
        text_node_1 = TextNode("This is a text node", TextType.ITALIC)
        html_node_1 = text_node_to_html_node(text_node_1)
        self.assertEqual(html_node_1.tag, "i")
        self.assertEqual(html_node_1.value, "This is a text node")
        self.assertEqual(html_node_1.children, [])
        self.assertIsNone(html_node_1.props)

        text_node_2 = TextNode("this is a third text node", TextType.LINK, "http://www.notgoogle.com/")
        html_node_2 = text_node_to_html_node(text_node_2)
        self.assertEqual(html_node_2.tag, "a")
        self.assertEqual(html_node_2.value, "this is a third text node")
        self.assertEqual(html_node_2.props["href"], "http://www.notgoogle.com/")

        text_node_3 = TextNode("This is a text node", TextType.CODE)
        html_node_3 = text_node_to_html_node(text_node_3)
        self.assertEqual(html_node_3.tag, "code")
        self.assertEqual(html_node_3.value, "This is a text node")
        self.assertEqual(html_node_3.children, [])
        self.assertIsNone(html_node_3.props)

        text_node_4 = TextNode("This is a text node", TextType.IMAGE, "http://www.notgoogle.com/")
        html_node_4 = text_node_to_html_node(text_node_4)
        self.assertEqual(html_node_4.tag, "img")
        self.assertEqual(html_node_4.value, "")
        self.assertEqual(html_node_4.props["src"], "http://www.notgoogle.com/")
        self.assertEqual(html_node_4.props["alt"], "This is a text node")

        text_node_5 = TextNode("This is a text node", TextType.BOLD)
        html_node_5 = text_node_to_html_node(text_node_5)
        self.assertEqual(html_node_5.tag, "b")
        self.assertEqual(html_node_5.value, "This is a text node")
        self.assertEqual(html_node_5.children, [])
        self.assertIsNone(html_node_5.props)

        text_node_6 = TextNode("This is a text node", TextType.TEXT)
        html_node_6 = text_node_to_html_node(text_node_6)
        self.assertEqual(html_node_6.tag, None)
        self.assertEqual(html_node_6.value, "This is a text node")
        self.assertEqual(html_node_6.children, [])
        self.assertIsNone(html_node_6.props)

        with self.assertRaises(Exception):
            text_node_7 = TextNode("This is a text node", TextType.TEST)
            html_node_7 = text_node_to_html_node(text_node_7)
if __name__ == "__main__":
    unittest.main()