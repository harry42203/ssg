from markdown_to_html_nodes import markdown_to_html_nodes

def main():
    text = "### This is a heading\n\n## This is a h2\n\n###### This is a h6\n\n```code\nmorecode```\n\nThis is a paragraph of *text*. It has, some some **bold** and *italic* words **inside of** it\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    html_str =  markdown_to_html_nodes(text)
    print(html_str)
if __name__ == "__main__":
    main()