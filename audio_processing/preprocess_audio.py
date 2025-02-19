import numpy as np
from scipy.signal import resample

def preprocess_audio(audio_array, target_framerate):
    current_framerate = 16000  # Assuming the original framerate is 16kHz
    if current_framerate != target_framerate:
        audio_array = resample(audio_array, int(len(audio_array) * target_framerate / current_framerate))
    return audio_array