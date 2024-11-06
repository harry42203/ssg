from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold_nodes = get_bold([node])  # Pass the text as a string, not the node itself
    bold_code_nodes = get_code(bold_nodes)
    bold_code_italic_nodes = get_italic(bold_code_nodes)
    bold_code_italic_image_nodes = get_image(bold_code_italic_nodes)
    bold_code_italic_image_link_nodes = get_link(bold_code_italic_image_nodes)
    return bold_code_italic_image_link_nodes


def get_bold(nodes):
    delimeter = "**"
    return split_nodes_delimiter(nodes, delimeter, TextType.BOLD)
def get_code(nodes):
    delimeter = "`"
    return split_nodes_delimiter(nodes, delimeter, TextType.CODE)
def get_italic(nodes):
    delimeter = "*"
    return split_nodes_delimiter(nodes, delimeter, TextType.ITALIC)
def get_image(nodes):
    return split_nodes_image(nodes)
def get_link(nodes):
    return split_nodes_link(nodes)