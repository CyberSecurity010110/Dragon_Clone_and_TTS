def generate_speech(model, text_input, cloned_voice=None):
    # Use the cloned voice if provided, otherwise use the default voice
    speech_output = model.generate_speech(text_input, cloned_voice)
    return speech_output
