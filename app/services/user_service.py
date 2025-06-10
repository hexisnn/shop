from sqlalchemy import select
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from app.models import Users



class UserService:

    async def get_one_byEmail(self, user_email: str, db: AsyncSession):
        try:
            result = await db.execute(
                select(Users).where(Users.email == user_email)
            )

            return result.scalar_one_or_none()

        except Exception as e:
            raise e


    async def get_all(self, db: AsyncSession):
        try:
            users = await db.execute(select(Users))
            return users.scalars().all()
        
        except Exception as e:
            raise e
        
        
userService = UserService()