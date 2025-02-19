import unittest
from audio_processing.load_audio import load_audio
from audio_processing.preprocess_audio import preprocess_audio

class TestAudioProcessing(unittest.TestCase):
    def test_load_audio(self):
        audio_array, framerate, n_channels, sampwidth = load_audio('myvoice.wav')
        self.assertIsNotNone(audio_array)
        self.assertEqual(framerate, 16000)  # Assuming the original framerate is 16kHz
        self.assertEqual(n_channels, 1)  # Assuming mono audio
        self.assertEqual(sampwidth, 2)  # Assuming 16-bit audio

    def test_preprocess_audio(self):
        audio_array, _, _, _ = load_audio('myvoice.wav')
        processed_audio = preprocess_audio(audio_array, 22050)
        self.assertIsNotNone(processed_audio)

if __name__ == '__main__':
    unittest.main()
