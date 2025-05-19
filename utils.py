import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to chunk the extracted text into smaller parts
def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = text_splitter.split_text(text)
    return chunks
def search_in_chunks(question, chunks):
    question_words = set(question.lower().split())

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        common_words = question_words.intersection(chunk_words)
        if len(common_words) >= 2:  # Adjust threshold as needed
            return chunk  # Return the first relevant chunk

    return None  # If nothing relevant is found
