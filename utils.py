from pathlib import Path

def read_text_from_file(file_path: str) -> str:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return file.read()

def chunk_text(text: str, chunk_size: int = 1000) -> list[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i : i + chunk_size]
        chunk = " ".join(chunk)
        chunks.append(chunk)
        i = i + chunk_size
    return chunks
