from typing import List, Optional
from abc import ABC, abstractmethod
from audio_input import WhisperMicrophone
from audio_output import GoogleTTS, TTSClient
from openai_io import OpenAIChatCompletion


class ChatAgent(ABC):
    @abstractmethod
    def get_response(self, transcript: List[str]) -> str:
        pass

    def start(self):
        pass


class TerminalInPrintOut(ChatAgent):
    def get_response(self, transcript: List[str]) -> str:
        if len(transcript) > 0:
            print(transcript[-1])
        return input(" response > ")


class OpenAIChat(ChatAgent):
    def __init__(self, system_prompt: str, init_phrase: Optional[str] = None):
        self.openai_chat = OpenAIChatCompletion(system_prompt=system_prompt)
        self.init_phrase = init_phrase

    def get_response(self, transcript: List[str]) -> str:
        if len(transcript) > 0:
            response = self.openai_chat.get_response(transcript)
        else:
            response = self.init_phrase
        return response


class MicrophoneInTextOut(ChatAgent):
    def __init__(self):
        self.mic = WhisperMicrophone()

    def get_response(self, transcript: List[str]) -> str:
        if len(transcript) > 0:
            print(transcript[-1])
        return self.mic.get_transcription()


class TerminalInTTSOut(ChatAgent):
    def __init__(self, tts: Optional[TTSClient] = None):
        self.speaker = tts or GoogleTTS()

    def get_response(self, transcript: List[str]) -> str:
        response = input(" response > ")
        self.speaker.play_text(response)
        return response


class OpenaiInTTSOut(ChatAgent):
    def __init__(self, system_prompt: str, init_phrase: Optional[str] = None, tts: Optional[TTSClient] = None):
        self.openai_chat = OpenAIChatCompletion(system_prompt=system_prompt)
        self.init_phrase = init_phrase
        self.speaker = tts or GoogleTTS()

    def get_response(self, transcript: List[str]) -> str:
        if len(transcript) > 0:
            response = self.openai_chat.get_response(transcript)
        else:
            response = self.init_phrase

        self.speaker.play_text(response)
        return response
