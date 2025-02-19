from audio_processing.load_audio import load_audio
from audio_processing.preprocess_audio import preprocess_audio

def main():
    # Path to the voice sample
    voice_sample_path = 'myvoice.wav'
    
    # Load the audio file
    audio_array, framerate, n_channels, sampwidth = load_audio(voice_sample_path)
    
    # Preprocess the audio file
    target_framerate = 22050  # Example target framerate
    processed_audio = preprocess_audio(audio_array, target_framerate)
    
    # Placeholder for further processing (e.g., model inference)
    # ...

if __name__ == '__main__':
    main()