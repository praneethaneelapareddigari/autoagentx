from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.agents.planner_agent import get_agent
from app.middleware.auth import get_current_user

router = APIRouter()

class AgentInput(BaseModel):
    prompt: str

@router.post("/agent/ask")
async def agent_ask(data: AgentInput, user=Depends(get_current_user)):
    agent = get_agent()
    try:
        response = agent.run(data.prompt)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))