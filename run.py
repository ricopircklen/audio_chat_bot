from agents import OpenAIChat, TerminalInPrintOut, MicrophoneInTextOut, TerminalInTTSOut, OpenaiInTTSOut
from conversation import run_conversation
import logging
import argparse

logging.getLogger().setLevel(logging.INFO)


def run_terminal_chat():
    agent_b = TerminalInPrintOut()
    agent_a = TerminalInPrintOut()
    run_conversation(agent_a, agent_b)


def run_openai_chat():
    agent_a = OpenAIChat(
        system_prompt="You are a customer service agent. Ask how you can help the client. Provide short and clear answers.",
        init_phrase="Hi, how can I help you?")
    agent_b = TerminalInPrintOut()
    run_conversation(agent_a, agent_b)


def run_whisper_chat():
    agent_a = MicrophoneInTextOut()
    agent_b = TerminalInPrintOut()
    run_conversation(agent_a, agent_b)


def run_tts_chat():
    agent_a = TerminalInTTSOut()
    agent_b = TerminalInTTSOut()
    run_conversation(agent_a, agent_b)


def run_tts_tts_chat():
    agent_a = TerminalInTTSOut()
    agent_b = OpenaiInTTSOut(
        system_prompt="You are a customer service agent. Ask how you can help the client. Provide short and clear answers.",
        init_phrase="Hi, how can I help you?")
    run_conversation(agent_a, agent_b)


def run_stt_tts_chat():
    agent_a = OpenaiInTTSOut(
        system_prompt="You are a customer service agent. Ask how you can help the client. Provide short and clear answers.",
        init_phrase="Hi, how can I help you?")
    agent_b = MicrophoneInTextOut()
    run_conversation(agent_a, agent_b)


def main():
    parser = argparse.ArgumentParser(description="Run the chatbot in different modes")
    parser.add_argument("--mode", type=str, help="Chat mode", default="whisper_chat",
                        choices=["terminal_chat", "openai_chat", "whisper_chat", "tts_chat", "tts_tts_chat", "stt_tts_chat"])
    args = parser.parse_args()

    modes = {
        "terminal_chat": run_terminal_chat,
        "openai_chat": run_openai_chat,
        "whisper_chat": run_whisper_chat,
        "tts_chat": run_tts_chat,
        "tts_tts_chat": run_tts_tts_chat,
        "stt_tts_chat": run_stt_tts_chat,
    }

    modes[args.mode]()


if __name__ == "__main__":
    main()
