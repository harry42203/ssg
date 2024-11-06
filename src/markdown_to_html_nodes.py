from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_nodes import text_to_textnodes
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node
 
def markdown_to_html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)
    block_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = get_tag(block, block_type)
        if tag == "ol" or tag == "ul":
            items = []
            list_items = get_block_text(block, block_type)
            for item in list_items:
                text = text_to_textnodes(item)
                children = []
                for node in text:
                    children.append(text_node_to_html_node(node))
                items.append(ParentNode("li", children))
            block_list.append(ParentNode(tag, items))
        if tag == "pre_code":
            items = []
            list_items = get_block_text(block, block_type)
            for item in list_items:
                text = text_to_textnodes(item)
                children = []
                for node in text:
                    children.append(text_node_to_html_node(node))
                items.append(ParentNode("", children))
            block_list.append(ParentNode(tag, items))
        else:
            text = text_to_textnodes(get_block_text(block, block_type))
            children = []
            for node in text:
                    children.append(text_node_to_html_node(node))
            block_list.append(ParentNode(tag, children))
    html_string = ""
    return_str = ""
    for block in block_list:
        html_string = block.to_html()
        return_str += html_string
    return_str = f"<div>{return_str}</div>"
    return return_str
                          
def get_tag(block, block_type):
    match block_type:
        case ("paragraph"):
            return "p"
        case ("heading"):
            stripped_block = block.split()
            return f"h{len(stripped_block[0])}"
        case ("code"):
            return "code"
        case ("pre_code"):
            return "pre_code"
        case ("quote"):
            return "blockquote"
        case ("unordered_list"):
            return "ul"
        case ("ordered_list"):
            return "ol"
        case _:
            raise Exception("no node type")
        
def get_block_text(block, block_type):
    match block_type:
        case ("paragraph"):
            return block
        case ("heading"):
            stripped_block = block.split()
            string = " ".join(stripped_block[1:])
            return string
        case ("code"):
            string = block.replace("`", "")
            return string
        case ("pre_code"):
            block_string = block.replace("`", "")
            split = block_string.split("\n")
            list_items = []
            for str in split:
                if str != "":
                    list_items.append(str) 
            return list_items
        case ("quote"):
            string = block.replace(">", "")
            return string
        case ("unordered_list"):
            block_string = block
            if "\n" in block:
                block_string = block.replace("\n", "")
            if "* " in block_string:
                block_string = block_string.replace("* ", "\n")
            if "- " in block_string:
                block_string = block_string.replace("- ", "\n")
            split = block_string.split("\n")
            list_items = []
            for str in split:
                if str != "":
                    list_items.append(str) 
            return list_items
        case ("ordered_list"):
            lines = block.split("\n")
            list_items = []
            for line in lines:
                if line != "":
                    dot = line.find(".")
                    list_items.append(line[dot+1:])
            return list_items
        case _:
            raise Exception("no block type")