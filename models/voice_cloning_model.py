import torch
import torchaudio
from torchaudio.transforms import Resample

class VoiceCloningModel:
    def __init__(self):
        # Load Tacotron2 and WaveGlow models
        self.tacotron2 = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_tacotron2')
        self.waveglow = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_waveglow')
        self.tacotron2.eval()
        self.waveglow.eval()

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
        torchaudio.save('cloned_voice.wav', audio, 22050)
        return 'cloned_voice.wav'
