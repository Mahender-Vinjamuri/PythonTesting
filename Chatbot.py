#streamlit - free and open UI interface
#pypdf2 - To Read our pdf files
#langchain - Interface to use open AI services
#faisscpu - Vector to store embeddings

import streamlit as st
from PyPDF2 import PdfReader
from langchain.chains.combine_documents import stuff
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS

OPEN_API_KEY = ""

#upload PDF files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a pdf file and start asking questions", type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text = text + page.extract_text()
        #st.write(text)

    #Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=2000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)#generating embeddings

    #generating embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPEN_API_KEY)

    #creating vector store - FAISS(Facebook AI semantic search)
    vector_store = FAISS.from_texts(chunks, embeddings)

    #get user question
    user_question = st.text_input("Type your question here")

    #do similarity research
    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match)

        #define LLM
        llm = ChatOpenAI(
            openai_api_key=OPEN_API_KEY,
            temperature=0,
            max_tokens=100,
            model_name="gpt-4o"

        )

        #output results
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents= match, question = user_question)
        st.write(response)