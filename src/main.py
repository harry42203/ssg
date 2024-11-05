from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from link_image_extraction import extract_markdown_links, extract_markdown_images
from splitnodes import split_nodes_delimiter

def main():
    # Create a test node and print it
    text = "This is text with a link  and "
    print(extract_markdown_links(text))



if __name__ == "__main__":
    main()