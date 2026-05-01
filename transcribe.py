import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(audio_folder):
    results = []

    for file in os.listdir(audio_folder):
        if file.endswith(".mp3"):
            path = os.path.join(audio_folder, file)
            result = model.transcribe(path)

            for segment in result["segments"]:
                results.append({
                    "text": segment["text"],
                    "start": segment["start"],
                    "end": segment["end"],
                    "video": file
                })

    return results