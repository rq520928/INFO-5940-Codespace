import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Retrieve the API key from environment variables key
api_key = os.getenv("API_KEY")
if not api_key:
    st.error("API key not found. Please set the API_KEY environment variable.")
    st.stop()
# Set up the OpenAI chat client (Cornell’s internal API endpoint)
client = ChatOpenAI(
    model="openai.gpt-4o",
    temperature=0.2,
    openai_api_key=api_key,
    openai_api_base="https://api.ai.it.cornell.edu",
)

# Streamlit app starts
st.title("RAG-based Document Chat")

# Allow users upload one or more documents (.txt or .pdf)
uploaded_files = st.file_uploader("Upload your documents", type=["txt", "pdf"], accept_multiple_files=True)

if uploaded_files:
    documents = []

    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension == ".txt":
            # Process .txt files
            text = uploaded_file.read().decode("utf-8")
            loader = TextLoader(text)
        elif file_extension == ".pdf":
            # Process .pdf files
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(uploaded_file.read())
                temp_pdf_path = temp_pdf.name

            loader = PyPDFLoader(temp_pdf_path)
        else:
            st.error(f"Unsupported file format: {file_extension}")
            continue

        document = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(document)
        documents.extend(chunks)

    # Build the vector store and embeddings to find the most relevant parts of the documents
    embeddings = OpenAIEmbeddings(
        openai_api_key=api_key,
        openai_api_base="https://api.ai.it.cornell.edu",
        model="openai.text-embedding-3-large" 
    )
    vector_store = Chroma.from_documents(documents, embeddings)

    # Create a Retrieval and QA chain
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=client, retriever=retriever)

    # Chat interface setup
    st.session_state["messages"] = st.session_state.get("messages", [])

    for message in st.session_state["messages"]:
        st.chat_message(message["role"]).write(message["content"])

    user_input = st.chat_input("Ask a question about your documents")

    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Generate response
        response = qa_chain.run(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)