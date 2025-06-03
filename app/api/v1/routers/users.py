from fastapi import APIRouter, Depends
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas import User
from app.models import Users
from fastapi import HTTPException
from app.services.user_service import userService

router = APIRouter()


@router.get("/test")
async def get_users(db: AsyncSession = Depends(get_db)):
     
    users = await userService.get_all(db)

    if len(users) == 0:
        return {"msg": "Gondon"}

    return {"msg": users}




   
