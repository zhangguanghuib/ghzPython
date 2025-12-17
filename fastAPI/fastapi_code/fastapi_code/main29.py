# FastAPI项目结构
from typing import Dict

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from tortoise import fields, models
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

# Tortoise-ORM 配置
TORTOISE_ORM: Dict = {
    "connections": {
        # 生产环境示例：MySQL
        "default": "mysql://root:123456@192.168.31.152:3306/fastapi_db5",
    },
    "apps": {
        "models": {
            "models": ["main29", "aerich.models"],  # 模型模块和 Aerich 迁移模型
            "default_connection": "default",
        }
    },
    # 连接池配置（推荐）
    "use_tz": False,  # 是否使用时区
    "timezone": "UTC",  # 默认时区
    "db_pool": {
        "max_size": 10,  # 最大连接数
        "min_size": 1,   # 最小连接数
        "idle_timeout": 30  # 空闲连接超时（秒）
    }
}

v1_router = APIRouter(prefix='/api/v1')
user_router = APIRouter(tags=['用户应用'], prefix='/user')
item_router = APIRouter(tags=['商品应用'])


@app.middleware("http")
async def middleware(request, call_next):
    print("请求前:")
    response = await call_next(request)
    print("请求后:")
    return response


class UserSchema(BaseModel):
    name: str
    email: str
    age: int


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=255)
    age = fields.IntField(default=1)
    create_at = fields.DatetimeField(auto_now_add=True)


@user_router.post('/create')
async def create_user(user: UserSchema):
    user2 = await User.create(**user.model_dump())
    return user2


@user_router.get('/info')
async def get_info():
    user = await User.first()
    user_schema = UserSchema.model_validate(user.__dict__)
    return user_schema


@item_router.get('/info')
async def get_info():
    return '商品信息'

v1_router.include_router(user_router)
v1_router.include_router(item_router)
app.include_router(v1_router)


register_tortoise(app,
                  config=TORTOISE_ORM,
                  generate_schemas=True,  # 开发环境自动生成表结构
                  add_exception_handlers=True  # 添加默认异常处理
                  )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main29:app', host="127.0.0.1", port=8000, reload=True)
