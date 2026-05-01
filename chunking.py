import json

def save_chunks(chunks):
    with open("data/transcripts.json", "w") as f:
        json.dump(chunks, f, indent=2)