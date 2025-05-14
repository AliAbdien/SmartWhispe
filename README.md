# 📝 SmartWhisper: AI Audio Transcriber for Students

SmartWhisper is a lightweight and powerful transcription tool built on OpenAI's Whisper model.
It transcribes spoken content from various audio formats directly into clean text files. Perfect for students and researchers.

## 🔧 Features
- Supports German audio (modifiable)
- Accepts most common audio formats: `.mp3`, `.wav`, `.m4a`, `.aac`, `.ogg`, `.flac`, `.webm`
- GPU acceleration via CUDA if available
- Outputs `.txt` transcripts
- Clean, modular code with format validation

## 🚀 Setup

### Install dependencies

```bash
pip install torch ffmpeg-python
pip install git+https://github.com/openai/whisper.git
```

### Usage

Place your audio file in the project folder and update `AUDIO_PATH` in `transcriber.py`.

```bash
python transcriber.py
```

## 📂 Output

- `transcript_output.txt`: The complete transcription from the input audio file.

## 🧠 Ideal for:
- Students recording lectures
- Research interview transcriptions
- Quick conversion of voice memos

---

© 2025 Ali Omar. Released under the MIT License.
