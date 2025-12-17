'''
FastAPI 应用入口文件
'''

from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise


from config.settngs import settings
from app.interface.api.v1.order_router import router as order_router
from app.interface.api.v1.auth_router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    应用生命周期管理
    '''
    # 启动时初始化数据库
    await init_database()
    yield
    # 关闭时断开数据库连接
    await close_database()

async def init_database():
    '''
    初始化数据库
    '''
    await Tortoise.init(
        db_url=settings.db_url,
        modules={'models': ['app.infrastructure.database.orm_models']}
    )
    await Tortoise.generate_schemas()


async def close_database():
    '''
    关闭数据库连接
    '''
    await Tortoise.close_connections()

def create_app() -> FastAPI:
    '''
    创建FastAPI实例
    '''
    app = FastAPI(
        title = settings.app_name,
        version = settings.app_version,
        description = '一个基于FastAPI的DDD示例应用',
        lifespan = lifespan
    )

    # 导入并注册路由
    app.include_router(auth_router, prefix="/api/v1")
    app.include_router(order_router, prefix="/api/v1")
    return app

app = create_app()

@app.get("/")
async def root():
    '''
    根路由
    '''
    return {"message": "欢迎使用 FastAPI DDD 应用","version": settings.app_version,"docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=settings.debug)
