# Dragon_clone_and_tts
A voice cloner/tts for ollama models/screenreader/stanadalone text input reader with large ouput cpabilities

# TTS Project

## Overview

This project aims to create a Text-to-Speech (TTS) system that can use a custom cloned voice and integrate with various TTS models, including Ollama models. The system will function as a standalone text input reader and screen reader, capable of generating speech output for at least a few minutes continuously.

## Features

- **Voice Cloning**: Use a custom cloned voice from `myvoice.wav`.
- **Model Compatibility**: Support for various TTS models, including Ollama models.
- **Standalone Functionality**: Operate as a standalone text input reader and screen reader.
- **Output Length**: Capable of generating speech output for at least a few minutes.
- **Hardware Utilization**: Efficiently utilize available hardware, including GPU (GTX 1080 with 8GB VRAM) and system RAM (16GB DDR4).

## Project Structure

tts_project/ ├── audio_processing/ │ ├── init.py │ ├── load_audio.py │ └── preprocess_audio.py ├── models/ │ ├── init.py │ ├── model_interface.py │ ├── ollama_model.py │ └── other_models.py ├── output_handling/ │ ├── init.py │ ├── generate_speech.py │ └── handle_output.py ├── ui/ │ ├── init.py │ ├── text_input.py │ └── screen_reader.py ├── tests/ │ ├── init.py │ ├── test_audio_processing.py │ ├── test_models.py │ ├── test_output_handling.py │ └── test_ui.py ├── main.py └── requirements.txt

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/tts_project.git
   cd tts_project

2. Install the required packages: 
   pip install -r requirements.txt

Future Work

    Integrate Ollama models and other TTS models.
    Implement the logic for generating and handling speech output.
    Develop a user interface for text input and screen reader functionality.
    Test and validate the system with different models.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License

This project is licensed under the MIT License.
