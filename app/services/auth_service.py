from fastapi.responses import RedirectResponse
from app.api.v1.schemas import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Users
from fastapi import HTTPException
from app.services.user_service import userService
import os
from app.utils.password import *


from dotenv import load_dotenv

load_dotenv()

class AuthService:
    async def login(self, user_data: User, db: AsyncSession):
        try:
            exist_user = await userService.get_one_byUsername(user_data.username, db)

            if not exist_user:
                return RedirectResponse(os.getenv("BASE_URL") + "/auth/registration")
            
            if equal_passwords(user_data.password, exist_user.password):
                return {"msg": "Good data"}
            else:
                return HTTPException(400, "Bad request")

            
        except Exception as e:
            raise e
    
    async def registration(self, user_dict: dict, db: AsyncSession):
        try:
            if await userService.get_one_byUsername(user_dict["username"], db):
                return RedirectResponse(os.getenv("BASE_URL") + "/auth/login")
            
            user_dict["password"] = hash_password(user_dict["password"])

            user = Users(**user_dict)
 
            db.add(user)
            await db.commit()
            await db.refresh(user)

            return user
        
        except Exception as e:
            await db.rollback()
            raise HTTPException("505", f"Server error {e}")





authService = AuthService()