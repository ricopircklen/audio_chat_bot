import openai
from typing import List
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.environ["OPENAI_KEY"]


class OpenAIChatCompletion:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def get_response(self, transcript: List[str]) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
        ]
        for i, text in enumerate(reversed(transcript)):
            messages.insert(1, {"role": "user" if i % 2 == 0 else "assistant", "content": text})
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100
        )
        return output["choices"][0]["message"]["content"]
