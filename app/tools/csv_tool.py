import pandas as pd
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain.document_loaders import CSVLoader

def summarize_csv(csv_path: str) -> str:
    loader = CSVLoader(file_path=csv_path)
    data = loader.load()

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(data, embeddings)

    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
    query = "Provide a concise summary."
    result = qa_chain.run(query)
    return result