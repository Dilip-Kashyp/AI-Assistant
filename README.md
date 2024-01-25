# Intelligent Assistant

This Python script implements an Intelligent Assistant using OpenAI's GPT-3.5 Turbo model for natural language processing. The assistant is capable of performing various tasks, including answering questions, opening websites, playing YouTube videos, checking the time, sending WhatsApp messages, providing news headlines, and engaging in conversation.AI Assistant designed to perform a variety of tasks through voice commands and a user interface.

## Features
- **Intelligent Conversations:** Engages in intelligent conversations using OpenAI's GPT-3.5 Turbo. Falls back to a custom generative model if needed.

- **Voice Interaction:** Utilizes the `speech_recognition` library to listen for user commands through the microphone.

- **OpenAI GPT-3.5 Turbo:** Employs OpenAI's powerful GPT-3.5 Turbo model for natural language understanding and generation.

- **Web Interaction:** Opens specified websites such as YouTube, Google, Wikipedia, and Facebook using the `webbrowser` module.

- **YouTube Video Playback:** Plays YouTube videos based on user commands with the help of `pywhatkit`.

- **Time Information:** Retrieves and announces the current time when the user asks.

- **WhatsApp Integration:** Sends instant WhatsApp messages to specified contacts using `pywhatkit`.

- **News Headlines:** Fetches and reads the top news headlines from NewsAPI.

- **Polite Exit:** Politely exits the program when the user says "thank you."

  ### Prerequisites

- Python 3.6 or later

## Setup

1. Install required packages using the following command:
   ```bash
   pip install web-browser datetime2 openai==0.28 requests SpeechRecognition pyttsx3 pywhatkit pyaudio eel google.generativeai
   ```

2. Obtain OpenAI API key and save it in `api_key.py`:
   ```python
   # api_key.py
   api_key1 = "your_openai_api_key_here" // Google API
   api_key2 = "your_openai_api_key_here" // openAI
   ```

3 Run the application:

    ```bash
    python run.py
    ```

4 Access the UI at [http://localhost:8000/index.html](http://localhost:8000/index.html).

## Usage

1. Upon execution, the assistant greets the user and awaits commands.

2. Use voice commands to interact with the assistant.

3. Examples of commands:
   - "Open YouTube"
   - "Play [song/artist] on YouTube"
   - "What is the time?"
   - "Send a WhatsApp message"
   - "Tell me the news"
   - "Tell me thw joke"
   - "Chat with AI"

4. Politely exit by saying "Thank you."
### Directory Structure

- `UI/`: Contains HTML and JavaScript files for the user interface.
- `Services/`: Holds utility functions for listening, speaking, and interacting with external services.
- `command.py`: Defines the primary functionality of the AI Assistant.
- `main.py`: Entry point of the application.
- `run.py`: For runinng app
- `controller.js`: Manages UI interactions and communicates with the backend.
- `eel.js`: Eel library script for integrating the Python backend with the UI.

## Additional Notes

- Ensure a stable internet connection for OpenAI API usage.
- Make sure the microphone is connected and accessible for voice commands.

Feel free to explore and enhance the functionality of this Intelligent Assistant script! If you have any questions or suggestions, please create an issue or pull request.

**Note:** Please use responsibly and adhere to OpenAI's use-case policies.
