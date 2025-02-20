import unittest
from ui.text_input import get_text_input
from ui.screen_reader import read_screen_text

class TestUI(unittest.TestCase):
    def test_read_screen_text(self):
        text = "This is a test."
        read_screen_text(text)

if __name__ == '__main__':
    unittest.main()
