from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.schemas.user_schema import UserSchema

router = APIRouter()

@router.post("/", response_model=UserSchema)
async def create_user(user: UserSchema, user_service: UserService = Depends()):
    return await user_service.create_user(user)

@router.get("/", response_model=list[UserSchema])
async def read_users(skip: int = 0, limit: int = 100, user_service: UserService = Depends()):
    return await user_service.read_users(skip, limit)

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: int, user_service: UserService = Depends()):
    return await user_service.read_user(user_id)

@router.put("/{user_id}", response_model=UserSchema)
async def update_user(user_id: int, user: UserSchema, user_service: UserService = Depends()):
    return await user_service.update_user(user_id, user)

@router.delete("/{user_id}")
async def delete_user(user_id: int, user_service: UserService = Depends()):
    return await user_service.delete_user(user_id)
