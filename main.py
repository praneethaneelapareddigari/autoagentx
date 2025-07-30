from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.ask import router as ask_router
from app.middleware.auth import jwt_auth_middleware
from prometheus_client import make_asgi_app

app = FastAPI(
    title="AutoAgentX",
    description="Autonomous GenAI Workflow Agent powered by LangChain + GPT-4 + Pinecone",
    version="1.0.0"
)

app.add_middleware(jwt_auth_middleware)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask_router, prefix="/api")

# Prometheus metrics endpoint
app.mount("/metrics", make_asgi_app())