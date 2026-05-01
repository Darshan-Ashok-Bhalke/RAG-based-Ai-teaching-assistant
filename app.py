from embeddings import create_embedding
from retriever import get_top_chunks
import json

with open("data/transcripts.json") as f:
    chunks = json.load(f)

stored_embeddings = [create_embedding(c["text"]) for c in chunks]

print("AI Assistant Ready 🚀")

while True:
    query = input("\nAsk question: ")

    if query.lower() == "exit":
        break

    query_emb = create_embedding(query)

    top_chunks = get_top_chunks(query_emb, stored_embeddings, chunks)

    context = " ".join([c["text"] for c in top_chunks])

    print("\nAnswer based on context:")
    print(context)