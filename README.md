# Audio Chat Bot

This repository includes various modes of interaction with an OpenAI GPT-based chat agent. You can interact using text or speech. The system can provide outputs as text or text-to-speech.

## Setup

1. Clone the repository

```
git clone
```

2. Navigate to the cloned directory

```
cd
```

3. Install the required Python packages

```
pip install -r requirements.txt
```

4. Add your OpenAI API key to a `.env` file in the root of the project directory:

```
OPENAI_KEY=your-openai-key-here
```

5. You're all set!

## Usage

The main script can be run with different "modes" of operation using the `--mode` command-line argument. The modes include:

- `terminal_chat`: Text input and output in terminal
- `openai_chat`: Interact with OpenAI model via terminal
- `whisper_chat`: Microphone input and terminal output
- `tts_chat`: Terminal input and text-to-speech output
- `tts_tts_chat`: Terminal input, OpenAI response via text-to-speech
- `stt_tts_chat`: Microphone input, OpenAI response via text-to-speech

To run the script with a specific mode, use the following command:

```bash
python3 main.py --mode tts_chat
```

If no mode is specified, the script defaults to `whisper_chat`.

## Credit

This project is based on the work done by [sshh12](https://github.com/sshh12) in the [llm_convo](https://github.com/sshh12/llm_convo) repository.
