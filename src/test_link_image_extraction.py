import unittest

from link_image_extraction import extract_markdown_images, extract_markdown_links
class TestHTMLNode(unittest.TestCase):
    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "This is text with a no images"        
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), expected)
        expected_2 = []
        self.assertEqual(extract_markdown_images(text2), expected_2)

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text2 = "This is text with a no links"
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(extract_markdown_links(text), expected)
        expected_2 = []
        self.assertEqual(extract_markdown_links(text2), expected_2)
if __name__ == "__main__":
    unittest.main()