from typing import List
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserSchema
from app.database import get_db

class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user: UserSchema):
        db_user = User(**user.dict())
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def read_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    async def read_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    async def update_user(self, user_id: int, user: UserSchema):
        db_user = self.db.query(User).filter(User.id == user_id)
        if db_user is None:
            raise ValueError("User not found")
        db_user.update(user.dict())
        await self.db.commit()
        return db_user.first()

    async def delete_user(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id)
        if db_user is None:
            raise ValueError("User not found")
        db_user.delete()
        await self.db.commit()
        return {"message": "User deleted successfully"}
