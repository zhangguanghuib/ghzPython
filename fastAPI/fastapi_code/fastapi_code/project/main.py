# 启动项目
from fastapi import FastAPI
from app.routers import v1_router
from app.database import register_db
from app.config import TORTOISE_ORM
from app.middleware import request_middleware

app = FastAPI()

# 注册路由
app.include_router(v1_router)

# 注册数据库
register_db(app, TORTOISE_ORM, generate_schemas=False)

# 注册中间件
app = request_middleware(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
