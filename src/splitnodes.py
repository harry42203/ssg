from textnode import TextNode, TextType
from link_image_extraction import extract_markdown_links, extract_markdown_images
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_to_return = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            #if delimiter not in node.text:
                #raise Exception("Delimiter not in node")
                
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
        if node.text_type != TextType.TEXT:
            nodes_to_return.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        remaining_text = text

        for match in matches:
            url_name, url = match
            full_link = f"[{url_name}]({url})"
            sections = remaining_text.split(full_link, maxsplit=1)

            if sections[0]:
                nodes_to_return.append(TextNode(sections[0],TextType.TEXT))
            
            nodes_to_return.append(TextNode(url_name, TextType.LINK, url))
            remaining_text = sections[1] if len(sections) > 1 else ""

        if remaining_text:
            nodes_to_return.append(TextNode(remaining_text, TextType.TEXT))

    return nodes_to_return

def split_nodes_image(old_nodes):
    nodes_to_return = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_to_return.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        remaining_text = node.text

        for match in matches:
            img_name, img = match
            full_link = f"![{img_name}]({img})"
            sections = remaining_text.split(full_link, maxsplit=1)

            if sections[0]:
                nodes_to_return.append(TextNode(sections[0],TextType.TEXT))
            
            nodes_to_return.append(TextNode(img_name, TextType.IMAGE, img))
            remaining_text = sections[1] if len(sections) > 1 else ""

        if remaining_text:
            nodes_to_return.append(TextNode(remaining_text, TextType.TEXT))

    return nodes_to_return
