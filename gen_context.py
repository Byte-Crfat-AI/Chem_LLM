import os
import argparse
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

CHROMA_PATH = "chroma"
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
PROMPT_TEMPLATE = """
answer as precisely as possible based on the below context
Question: \n {question} \n
Context: \n {context}?\n
Answer:"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=google_api_key)

    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0:
            print(f"Unable to find matching results.")
            return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print("\n\n",prompt)

    model = genai.GenerativeModel(model_name = "gemini-pro")
    response_text = model.generate_content(prompt).text
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)

if(__name__=='__main__'):
    main()