from textnode import TextNode, TextType
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_to_return = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                raise Exception("Delimiter not in node")
            nodes_to_return.extend(set_nodes(node.text, delimiter, text_type))
        else: 
            nodes_to_return.append(node)
    
    return nodes_to_return

def set_nodes(node_text, delim, text_type):
    new_nodes = []
    text_to_split = node_text
    split_nodes = text_to_split.split(delim)
    inside_delimiter = False
    if text_to_split.count(delim) % 2 != 0:
            raise Exception("Unmatched delimiter count in node text")
    
    for node in split_nodes:
        if inside_delimiter:
            new_nodes.append(TextNode(node, text_type))
        else:
            if node:  # Ensure the node isn't empty before adding
                new_nodes.append(TextNode(node, TextType.TEXT))
        
        # Toggle the flag as we move through each node part
        inside_delimiter = not inside_delimiter

    return new_nodes

def split_nodes_link(old_nodes):
    nodes_to_return = []
    for node in old_nodes:
        text = node.text
        pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        matches = re.findall(pattern, text)
        for match in matches:
            url_name, url = match
            nodes_to_return.append(TextNode(url_name,TextType.LINK, url))
            text.replace(url_name, "*")
            text.replace(url, "*")
            print(text)
    
    return nodes_to_return


def split_nodes_image(old_nodes):
    pass
