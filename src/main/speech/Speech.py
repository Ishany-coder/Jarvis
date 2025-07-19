import sounddevice as sd
import soundfile as sf
import whisper
import numpy as np

def record_and_transcribe(duration=5, samplerate=16000, channels=1):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='float32')
    sd.wait()

    audio_file = "temp.wav"
    sf.write(audio_file, recording, samplerate)

    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    print("\nTranscription:\n", result["text"])
    return result["text"]

if __name__ == "__main__":
    record_and_transcribe(5)