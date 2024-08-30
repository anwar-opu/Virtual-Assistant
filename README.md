# Alexa-like Python Virtual Assistant

This repository contains a Python-based virtual assistant that functions similarly to Amazon's Alexa. The assistant can perform various tasks such as telling the time, playing music, searching Wikipedia, telling jokes, and conducting web searches.

## Features

- **Tell Time:** Get the current time.
- **Play Music:** Play any song from YouTube.
- **Wikipedia Search:** Get a brief summary of a topic from Wikipedia.
- **Jokes:** Listen to a random joke.
- **Web Search:** Automatically search the web for unrecognized commands.

## Installation

To set up the virtual assistant on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/anwar-opu/Virtual-Assistant.git
   cd Virtual-Assistant
   ```
2. **Install the Required Libraries:**
   ```bash
   pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
   ```
## Usage Guide

 - **Time:** "Alexa, what's the time?"
 - Play Music: "Alexa, play [song name]."
 - Wikipedia Search: "Alexa, tell me about [topic]."
 - Jokes: "Alexa, tell me a joke."
 - Web Search: If the command doesn't match any of the above, the assistant will perform a web search.

## Acknowledgements

- SpeechRecognition: For recognizing voice input.
- pyttsx3: For converting text to speech.
- pywhatkit: For playing YouTube videos and performing web searches.
- wikipedia-api: For fetching information from Wikipedia.
- pyjokes: For generating jokes
