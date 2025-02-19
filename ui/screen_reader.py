import pyttsx3

def read_screen_text(text: str):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
