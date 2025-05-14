# Whisper Audio Transcriber
# --------------------------------------
# This script uses OpenAI's Whisper model to transcribe audio files
# in multiple languages and outputs the full transcript to a .txt file.
# Ideal for students, researchers, and professionals who want to convert
# spoken content into written text efficiently.

import whisper
import torch
import os
import sys

# ---------------------------
# Configuration Parameters
# ---------------------------
SUPPORTED_FORMATS = (".aac", ".mp3", ".wav", ".flac", ".m4a", ".ogg", ".webm")
AUDIO_PATH = "input_audio.aac"         # Path to the input audio file
OUTPUT_PATH = "transcript_output.txt"  # Output text file
LANGUAGE = None                         # Set to None for auto-detection, or provide e.g., "en", "de", "ar"
MODEL_SIZE = "large-v3"                # Whisper model to use
USE_FP16 = True                         # Use half-precision for faster GPU inference


def validate_audio_format(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"❌ Unsupported audio format: {ext}. Supported formats: {SUPPORTED_FORMATS}")


def main():
    # Check device availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🔍 Using device: {device}")

    # Validate audio file format
    try:
        validate_audio_format(AUDIO_PATH)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Load Whisper model
    print("⏳ Loading Whisper model...")
    model = whisper.load_model(MODEL_SIZE, device=device)

    # Transcribe audio
    print(f"🎧 Transcribing audio file: {os.path.basename(AUDIO_PATH)}")
    result = model.transcribe(
        AUDIO_PATH,
        language=LANGUAGE,
        fp16=USE_FP16 if device == "cuda" else False
    )

    # Save transcript to file
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"✅ Transcription complete. Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
