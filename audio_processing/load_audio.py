import wave
import numpy as np

def load_audio(file_path):
    with wave.open(file_path, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        audio_data = wf.readframes(n_frames)
    
    audio_array = np.frombuffer(audio_data, dtype=np.int16)
    return audio_array, framerate, n_channels, sampwidth