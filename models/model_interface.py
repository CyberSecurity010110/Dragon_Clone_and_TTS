from abc import ABC, abstractmethod

class TTSModelInterface(ABC):
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def generate_speech(self, text: str) -> str:
        pass
