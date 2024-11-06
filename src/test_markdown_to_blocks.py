import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type


class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(text)
        assert len(blocks) == 3  
        assert blocks[0] == '# This is a heading'
        assert blocks[1] == 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.'
        assert blocks[2] == '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
    def test_headings(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("### Heading 3"), "heading")
        # Add your test for invalid headings
        self.assertEqual(block_to_block_type("#No space"), "paragraph")
        self.assertEqual(block_to_block_type("####### Too many"), "paragraph")

    def test_code_blocks(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), "code")
        # What other code block cases should we test?

    def test_quotes(self):
        self.assertEqual(block_to_block_type("> Single quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), "quote")
        self.assertEqual(block_to_block_type(">No space"), "paragraph")
        # Add more quote tests

    def test_ordered_lists(self):
        # Valid ordered lists
        self.assertEqual(block_to_block_type("1. First\n2. Second"), "ordered_list")
        self.assertEqual(block_to_block_type("1. Only one"), "ordered_list")
        
        # Invalid ordered lists should be paragraphs
        self.assertEqual(block_to_block_type("1. First\n3. Third"), "paragraph")  # Skipped number
        self.assertEqual(block_to_block_type("2. Wrong start"), "paragraph")      # Doesn't start with 1
        self.assertEqual(block_to_block_type("1.No space"), "paragraph")          # Missing space after dot
        self.assertEqual(block_to_block_type("1. First\n2.No space"), "paragraph")  # Missing space in second line

    def test_unordered_lists(self):
        # Valid unordered lists
        self.assertEqual(block_to_block_type("* First item"), "unordered_list")
        self.assertEqual(block_to_block_type("- First item"), "unordered_list")
        self.assertEqual(block_to_block_type("* First\n* Second"), "unordered_list")
        self.assertEqual(block_to_block_type("- First\n- Second"), "unordered_list")
        self.assertEqual(block_to_block_type("* First\n- Second"), "unordered_list")  # Mixed markers
        
        # Invalid unordered lists should be paragraphs
        self.assertEqual(block_to_block_type("*No space"), "paragraph")           # Missing space
        self.assertEqual(block_to_block_type("* First\nSecond"), "paragraph")    # Missing marker
        self.assertEqual(block_to_block_type("+ Invalid marker"), "paragraph")   # Wrong marker