from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI

def summarize_pdf(pdf_path: str) -> str:
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(pages, embeddings)

    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
    query = "Provide a concise summary."
    result = qa_chain.run(query)
    return result