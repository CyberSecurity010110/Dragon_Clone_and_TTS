import torch
import torchaudio
from torchaudio.transforms import Resample

class VoiceCloningModel:
    def __init__(self):
        # Check if CUDA is available
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Load Tacotron2 and WaveGlow models with appropriate device mapping
        self.tacotron2 = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_tacotron2', map_location=self.device)
        self.waveglow = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_waveglow', map_location=self.device)
        
        # Move models to the appropriate device
        self.tacotron2.to(self.device).eval()
        self.waveglow.to(self.device).eval()

    def preprocess_audio(self, audio_path):
        waveform, sample_rate = torchaudio.load(audio_path)
        resample = Resample(orig_freq=sample_rate, new_freq=22050)
        waveform = resample(waveform)
        return waveform

    def clone_voice(self, text, audio_path):
        # Preprocess the audio
        waveform = self.preprocess_audio(audio_path)
        
        # Generate mel spectrogram
        mel_spectrogram = self.tacotron2.infer(text)
        
        # Generate audio using WaveGlow
        with torch.no_grad():
            audio = self.waveglow.infer(mel_spectrogram)
        
        # Save the generated audio
        torchaudio.save('cloned_voice.wav', audio.cpu(), 22050)
        return 'cloned_voice.wav'
