from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.schemas import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.services.auth_service import authService
from app.services.user_service import userService
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os

load_dotenv()


router = APIRouter()

@router.post("/login")
async def login(user: User, db: AsyncSession = Depends(get_db)):
    try:
        
        user = await authService.login(user, db)

        return user

    except Exception as e:
        raise HTTPException(505, {"msg": "Server error", "err": e})
    
@router.post("/registration")
async def register(user: User, db: AsyncSession = Depends(get_db)):
    try:
        
        user = await authService.registration(user.dict(), db)

        return user

    except Exception as e:
        raise HTTPException(505, {"msg": "Server error", "err": e})