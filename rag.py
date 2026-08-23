from pathlib import Path
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENTS_DIR = Path("documents")

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():
    documents = []

    for file_path in DOCUMENTS_DIR.iterdir():
        extension = file_path.suffix.lower()

        try:
            if extension == ".md":
                text = file_path.read_text(encoding="utf-8")

            elif extension == ".csv":
                df = pd.read_csv(file_path)
                text = df.to_string(index=False)

            elif extension == ".json":
                data = json.loads(file_path.read_text(encoding="utf-8"))
                text = json.dumps(data, ensure_ascii=False, indent=2)

            else:
                continue

            documents.append({
                "source": file_path.name,
                "text": text
            })

        except Exception as e:
            print(f"Erro ao carregar {file_path.name}: {e}")

    return documents


def create_chunks(documents, chunk_size=500):
    chunks = []

    for document in documents:
        text = document["text"]

        for i in range(0, len(text), chunk_size):
            chunk_text = text[i:i + chunk_size].strip()

            if chunk_text:
                chunks.append({
                    "source": document["source"],
                    "text": chunk_text
                })

    return chunks


documents = load_documents()
chunks = create_chunks(documents)

chunk_texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(chunk_texts)


def search_documents(question, top_k=3):
    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        embeddings
    )[0]

    ranked_indexes = similarities.argsort()[::-1][:top_k]

    results = []

    for index in ranked_indexes:
        results.append({
            "source": chunks[index]["source"],
            "text": chunks[index]["text"],
            "score": float(similarities[index])
        })

    return results