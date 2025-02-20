def generate_speech(model, text_input, cloned_voice=None):
    # Use the cloned voice if provided, otherwise use the default voice
    if cloned_voice is not None:
        # Generate speech using the cloned voice
        speech_output = model.generate_speech(text_input, cloned_voice)
    else:
        # Generate speech using the default voice
        speech_output = model.generate_speech(text_input)
    
    return speech_output
