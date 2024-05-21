import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os

st.set_page_config(page_title="Open Source Explorer", layout="wide")

# Add custom CSS for dark theme and font styles
# Add custom CSS for dark theme and font styles
st.markdown("""
    <style>
        body {
            background-color: #0d1117;
            color: #000000;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #161b22;
            color: #c9d1d9;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 5px;
            transition: background-color 0.3s, transform 0.3s;
        }
        .stButton>button:hover {
            background-color: #2ea043;
            transform: scale(1.05);
        }
        .stTextInput>div>div>input {
            color: #c9d1d9;
            background-color: #0d1117;
            border-radius: 5px;
            border: 1px solid #30363d;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p {
            color: #c9d1d9;
        }
        .stMarkdown h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            animation: fade-in 1s ease-out;
        }
        .stMarkdown h2 {
            font-size: 2em;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .stMarkdown p {
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .stAlert {
            background-color: #21262d;
            color: #c9d1d9;
        }
        .response-text {
            color: #79c0ff;
            font-size: 1.2em;
            margin-top: 20px;
            padding: 10px;
            background-color: #21262d;
            border-radius: 5px;
            animation: slide-up 0.5s ease-out;
        }
        @keyframes fade-in {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        @keyframes slide-up {
            from {
                transform: translateY(20px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        .emoji {
            font-size: 1.5em;
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
# <span class="emoji">🚀</span> Open Source Explorer: Discover Awesome GitHub Repositories <span class="emoji">👩‍💻</span>

This chatbot is built using the Retrieval-Augmented Generation (RAG) framework, leveraging Google's Generative AI model Gemini-PRO. It processes the knowledge from certain open-source GitHub repositories and provides accurate recommendations based on user queries. This advanced approach ensures high-quality, contextually relevant responses for an efficient and effective user experience.

## <span class="emoji">🔍</span> How It Works

Follow these simple steps to interact with the chatbot:

1. **<span class="emoji">📂</span> The system processes the PDF document located in the data directory.**

2. **<span class="emoji">❓</span> Ask a Question**: Ask any question related to open-source repositories, and get a precise recommendation.
""", unsafe_allow_html=True)

# Use the predefined API key
api_key = "AIzaSyBx_Jp6X437DRCZ5zs0h9q-y4HMcfc6pow"

# Path to the predefined PDF file
pdf_file_path = "data/Github_Data.pdf"

def get_pdf_text(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.markdown(f"<div class='response-text'>Reply: {response['output_text']}</div>", unsafe_allow_html=True)

def main():
    st.header("Open Source Explorer 💻")

    # Process the predefined PDF file
    with st.spinner("Processing the predefined PDF file..."):
        raw_text = get_pdf_text(pdf_file_path)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks, api_key)
        st.success("PDF processing complete.")

    user_question = st.text_input("Ask a Question about Open Source Repositories", key="user_question")

    if user_question and api_key:  # Ensure API key and user question are provided
        user_input(user_question, api_key)

if __name__ == "__main__":
    main()
