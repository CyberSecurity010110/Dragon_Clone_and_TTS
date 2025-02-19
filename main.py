from audio_processing.load_audio import load_audio
from audio_processing.preprocess_audio import preprocess_audio
from models.ollama_model import OllamaModel
from output_handling.generate_speech import generate_speech
from output_handling.handle_output import handle_output
from ui.text_input import get_text_input
from ui.screen_reader import read_screen_text

def main():
    # Path to the voice sample
    voice_sample_path = 'myvoice.wav'
    
    # Load the audio file
    audio_array, framerate, n_channels, sampwidth = load_audio(voice_sample_path)
    
    # Preprocess the audio file
    target_framerate = 22050  # Example target framerate
    processed_audio = preprocess_audio(audio_array, target_framerate)
    
    # Initialize and load the model
    model = OllamaModel()
    model.load_model()
    
    # Get text input from the user
    text_input = get_text_input()
    
    # Generate speech
    speech_output = generate_speech(model, text_input)
    
    # Handle the output
    handle_output(speech_output)
    
    # Read the screen text using the screen reader
    read_screen_text(speech_output)

if __name__ == '__main__':
    main()
