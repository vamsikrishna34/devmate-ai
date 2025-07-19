from sentence_transformers import SentenceTransformer, util

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def compare_code_versions(original: str, revised: str) -> dict:
    """
    Compare two code snippets semantically and return similarity score.
    """
    embedding_1 = model.encode(original, convert_to_tensor=True)
    embedding_2 = model.encode(revised, convert_to_tensor=True)

    similarity = util.cos_sim(embedding_1, embedding_2).item()

    return {
        "similarity_score": round(similarity, 3),
        "verdict": interpret_similarity(similarity)
    }

def interpret_similarity(score: float) -> str:
    """
    Provide human-readable verdict based on similarity score.
    """
    if score > 0.9:
        return "Code versions are nearly identical in meaning."
    elif score > 0.75:
        return "Revised version maintains the original logic with slight changes."
    elif score > 0.5:
        return "Core logic has some overlap, but key differences exist."
    else:
        return "Revised code significantly alters or diverges from the original."
