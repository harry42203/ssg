def markdown_to_blocks(markdown):
    blocks_unstripped = markdown.split("\n\n")
    blocks = []
    for block in blocks_unstripped:
        if block != "":
            blocks.append(block.strip())
    return blocks
def block_to_block_type(block):
    if block.startswith("#"):
        stripped_block = block.split()
        if stripped_block[0][-1] != "#":
            return "paragraph"
        if len(stripped_block[0]) > 6:
            return "paragraph"
        for word in stripped_block[1:]:
            if "#" in word:
                return "paragraph"
        return "heading"
    
    if block.startswith("```") and block.endswith("```"):
        if "\n" in block:
            return "pre_code"
        else:
            return "code"
    
    if block.startswith("> "):
        split_block = block.split("\n")
        for line in split_block:
            if not line.startswith("> "):
                return "paragraph"
        return "quote"
    
    if block.startswith("* ") or block.startswith("- "):
        split_block = block.split("\n")
        for line in split_block:
            if not (line.startswith("- ") or line.startswith("* ")):
                return "paragraph"
        return "unordered_list"
    
    if block[0].isdigit():
        split_block = block.split("\n")
        expected_num = 1
        for line in split_block:
            dot = line.find(".")
            if not line[0:dot].isdigit():
                return "paragraph"
            elif not line[dot+1] == " ":
                return "paragraph"
            current_item = int(line[:dot])
            if current_item != expected_num:
                return "paragraph"
            expected_num += 1
        return "ordered_list"
    else:
        return "paragraph"
