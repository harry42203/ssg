from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    CODE_BLOCK = "pre_code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case (TextType.TEXT):
            node = LeafNode(None, text_node.text)
        case (TextType.BOLD):
            node = LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            node = LeafNode("i", text_node.text)
        case (TextType.CODE_BLOCK):
            node = LeafNode("pre_code", text_node.text)
        case (TextType.CODE):
            node = LeafNode("code", text_node.text)
        case (TextType.LINK):
            node = LeafNode("a", text_node.text, {"href":text_node.url})
        case (TextType.IMAGE):
            node = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Not a valid node type")
    return node
