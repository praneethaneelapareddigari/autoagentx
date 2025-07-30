# AutoAgentX

## Overview
AutoAgentX is a fully autonomous LLM agent using LangChain, GPT-4, Pinecone, and FAISS for multi-step workflows such as document Q&A, email drafting, and report generation.

Features:
- Multi-agent memory
- Tool execution tracking
- Custom RAG over PDF/CSV
- JWT secured FastAPI backend
- Dockerized deployment
- Prometheus monitoring
- AWS EC2 deploy-ready
- CI/CD GitHub Actions pipeline

## Setup

1. Clone repo
2. Create `.env` with Pinecone, OpenAI, and JWT secrets
3. Run locally:
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
4. Use Docker:
```bash
docker build -t autoagentx .
docker run -p 8000:8000 autoagentx
```

## API

- POST `/api/agent/ask` - query the LLM agent

## License
MIT