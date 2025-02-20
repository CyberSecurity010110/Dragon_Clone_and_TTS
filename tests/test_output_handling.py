import unittest
from output_handling.generate_speech import generate_speech
from output_handling.handle_output import handle_output
from models.ollama_model import OllamaModel

class TestOutputHandling(unittest.TestCase):
    def test_generate_and_handle_output(self):
        model = OllamaModel()
        model.load_model()
        speech_output = generate_speech(model, "Hello, this is a test.")
        self.assertIsNotNone(speech_output)
        handle_output(speech_output)

if __name__ == '__main__':
    unittest.main()
