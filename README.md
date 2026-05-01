# RAG Based AI Teaching Assistant

AI assistant using RAG to answer questions from video content.

Workflow:
Video → Audio → Text → Chunking → Embeddings → Retrieval → Answer
## Note
This project currently uses a local embedding model (Sentence Transformers) for cost efficiency and offline execution.

The full version of the project also supports OpenAI APIs for embedding generation and response generation, which can be integrated as an upgrade.

## Tech Stack
- Python
- Sentence Transformers
- NumPy
- JSON