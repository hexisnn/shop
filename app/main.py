from fastapi import FastAPI

import uvicorn
from dotenv import load_dotenv
import os
from app.models import Base
from app.config.database import engine
from app.config import database as db
from app.api.v1.routers.users import router as users_router
from app.api.v1.routers.auth import router as auth_router
load_dotenv()

app = FastAPI()



app.include_router(users_router, prefix=os.getenv("BASE_URL") + "/users", tags=["Users"])
app.include_router(auth_router, prefix=os.getenv("BASE_URL") + "/auth", tags=["Auth"])

