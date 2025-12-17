from fastapi import APIRouter
from app.schemas import UserSchema
from app.models import User

user_router = APIRouter(tags=['用户应用'], prefix='/user')


@user_router.post('/create')
async def create_user(user: UserSchema):
    user2 = await User.create(**user.model_dump())
    return user2


@user_router.get('/info')
async def get_info():
    user = await User.first()
    user_schema = UserSchema.model_validate(user.__dict__)
    return user_schema
