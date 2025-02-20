import unittest
from unittest.mock import MagicMock
from output_handling.generate_speech import generate_speech
from models.ollama_model import OllamaModel

class TestGenerateSpeech(unittest.TestCase):
    def setUp(self):
        self.model = OllamaModel()
        self.model.generate_speech = MagicMock(return_value="Generated speech")
        self.text_input = "Hello, this is a test."
        self.cloned_voice = "cloned_voice_sample"

    def test_generate_speech_with_cloned_voice(self):
        speech_output = generate_speech(self.model, self.text_input, self.cloned_voice)
        self.model.generate_speech.assert_called_with(self.text_input, self.cloned_voice)
        self.assertEqual(speech_output, "Generated speech")

    def test_generate_speech_without_cloned_voice(self):
        speech_output = generate_speech(self.model, self.text_input)
        self.model.generate_speech.assert_called_with(self.text_input)
        self.assertEqual(speech_output, "Generated speech")

if __name__ == '__main__':
    unittest.main()
