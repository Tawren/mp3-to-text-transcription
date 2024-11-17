# MP3 to Text Transcription

This project allows you to transcribe audio files (MP3 format) into text using OpenAI's Whisper. It supports progress tracking during transcription and allows users to select their preferred transcription language.

## Features
- Supports transcription in multiple languages supported by Whisper.
- Progress bar with estimated completion time.
- Generates a plain text file of the transcription.
- Handles large files by splitting them into manageable chunks.
- Easy-to-use Python script with customizable language settings.

## Supported Languages
Whisper supports the following languages:  
English (`en`), French (`fr`), German (`de`), Spanish (`es`), Italian (`it`), Portuguese (`pt`), Dutch (`nl`), Russian (`ru`), Chinese (`zh`), Japanese (`ja`), Korean (`ko`), Arabic (`ar`), and many more.  
A full list of supported languages can be found [here](https://github.com/openai/whisper#available-languages).

## Installation and Usage

### Prerequisites
- Python 3.10 or later must be installed.
- FFmpeg must be installed and configured in your system's PATH.

### Steps to Run
1. Place your mp3 file in the project folder ans put his name in the main.py at line 31
4. Modify the language parameter in main.py to your preferred language code (defaut is French (`fr`)) at line 24
5. Run the script with `run.bat` or `run.sh`

## Notes
- Make sure FFmpeg in installed. If not, install it from [FFmpeg official website](https://ffmpeg.org/) or use a package manager like choco or brew.
- Fot a complete list of supported languages, refer to the [Whisper documentation](https://github.com/openai/whisper#available-languages).
