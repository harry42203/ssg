from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from link_image_extraction import extract_markdown_links, extract_markdown_images
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def main():
    # Create a test node and print it
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )

    print(split_nodes_link([node]))



if __name__ == "__main__":
    main()