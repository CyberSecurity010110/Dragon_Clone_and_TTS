import unittest
from models.ollama_model import OllamaModel

class TestModels(unittest.TestCase):
    def test_generate_speech(self):
        model = OllamaModel()
        model.load_model()
        speech_output = model.generate_speech("Hello, this is a test.")
        self.assertIsNotNone(speech_output)

if __name__ == '__main__':
    unittest.main()
