from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from app.tools.pdf_tool import summarize_pdf
from app.tools.csv_tool import summarize_csv

def get_agent():
    llm = ChatOpenAI(temperature=0)
    tools = [
        Tool(
            name="PDF Summarizer",
            func=summarize_pdf,
            description="Summarizes PDF documents"
        ),
        Tool(
            name="CSV Summarizer",
            func=summarize_csv,
            description="Summarizes CSV documents"
        )
    ]
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent = initialize_agent(tools, llm, agent="conversational-react-description", memory=memory, verbose=True)
    return agent