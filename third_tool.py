import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import streamlit as st
from langchain_openai import OpenAIEmbeddings
def load_chunk_persist_pdf() -> Chroma:
    pdf_folder_path = "C:\\Users\\pc\\PycharmProjects\\flaskProjectAiEngineer\\pdf_QA\\"
    documents = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    openai_api_key = "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"
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding=embedding,
        persist_directory="C:\\Users\\pc\\PycharmProjects\\flaskProjectAiEngineer\\testing_space\\chroma_store\\"
    )
    vectordb.persist()
    return vectordb

def create_agent_chain():
    model_name = "gpt-3.5-turbo"
    llm = ChatOpenAI(model_name=model_name)
    chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
    return chain

def get_llm_response(query):
    vectordb = load_chunk_persist_pdf()
    chain = create_agent_chain()
    matching_docs = vectordb.similarity_search(query)
    answer = chain.run(input_documents=matching_docs, question=query)

    return answer

def rapid_qa_on_pdfs(query):
    st.set_page_config(page_title="Doc Searcher", page_icon=":robot:")
    st.header("Query PDF Source")
    form_input = st.text_input('Enter Query', value=query)
    submit = st.button("Generate")

    if submit:
        st.write(get_llm_response(form_input))

