import io
import os
import tempfile
import functools
import logging

from pydub import AudioSegment
import speech_recognition as sr
import whisper


@functools.cache
def get_whisper_model(size: str = "tiny"):
    logging.info(f"Loading whisper {size}")
    return whisper.load_model(size)


class WhisperMicrophone:
    def __init__(self):
        self.audio_model = get_whisper_model()
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 500
        self.recognizer.pause_threshold = 0.8
        self.recognizer.dynamic_energy_threshold = False

    def get_transcription(self) -> str:
        with sr.Microphone(sample_rate=16000) as source:
            logging.info("Waiting for mic...")
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = os.path.join(tmp, "mic.wav")
                audio = self.recognizer.listen(source)
                data = io.BytesIO(audio.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                audio_clip.export(tmp_path, format="wav")
                result = self.audio_model.transcribe(tmp_path, language="english")
            predicted_text = result["text"]
        return predicted_text
