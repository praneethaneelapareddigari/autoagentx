import os
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

SECRET_KEY = os.getenv("JWT_SECRET", "your-secret-key")
ALGORITHM = "HS256"

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api"):
            credentials = HTTPBearer()(request)
            try:
                token = (await credentials).credentials
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                request.state.user = payload
            except JWTError:
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Invalid token"})
        response = await call_next(request)
        return response

jwt_auth_middleware = JWTAuthMiddleware

async def get_current_user(request: Request):
    if not hasattr(request.state, "user"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return request.state.user