import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
CHROMA_PATH = "chroma"

def main():
    generate_data_store("./resources/")

def generate_data_store(directory):
    documents = load_documents(directory)
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents(directory):
    allpages = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                pages = loader.load_and_split()
                allpages.extend(pages)
                print("document with", len(pages), "pages processed")
    return allpages

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


# def save_to_chroma(chunks):
#     # Clear out the database first.
#     if os.path.exists(CHROMA_PATH):
#         shutil.rmtree(CHROMA_PATH)
#     embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=google_api_key)
#     db = Chroma.from_documents(chunks,embeddings, persist_directory=CHROMA_PATH)
#     db.persist()
#     print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def save_to_chroma(chunks):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=google_api_key)
    
    # Define the maximum batch size
    max_batch_size = 5400
    
    # Initialize an empty Chroma collection
    db = Chroma(persist_directory=CHROMA_PATH)
    
    # Split the chunks into smaller batches and add them to the Chroma collection
    for i in range(0, len(chunks), max_batch_size):
        batch_chunks = chunks[i:i + max_batch_size]
        
        # Generate embeddings for the current batch
        db = Chroma.from_documents(batch_chunks,embeddings, persist_directory=CHROMA_PATH)
        print(f"Saved {len(batch_chunks)} chunks to {CHROMA_PATH}.")
    
    # Save the collection
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == '__main__':
    main()
