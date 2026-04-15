from openai import OpenAI
from utils import read_text_from_file, chunk_text

client = OpenAI()

book_txt = read_text_from_file("/full/path/to/book.txt")
chunks = chunk_text(book_txt, chunk_size=50)

print(f"Number of chunks: {len(chunks)}")

for chunk in chunks:
    chunk_summary = client.responses.create(
        model="gpt-4o-mini",
        input=f"Summarize this text: {chunk}"
    )
    print(chunk_summary.output_text)
    print("---")
