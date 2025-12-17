# ORM基础配置
from crud21 import create_student
from tortoise.contrib.fastapi import register_tortoise
from typing import Dict
from fastapi import FastAPI

app = FastAPI()


# Tortoise-ORM 配置
TORTOISE_ORM: Dict = {
    "connections": {
        # 开发环境使用 SQLite（基于文件，无需服务器）
        # "default": "sqlite://db.sqlite3",
        # 生产环境示例：PostgreSQL
        # "default": "postgres://user:password@localhost:5432/dbname",
        # 生产环境示例：MySQL
        "default": "mysql://root:123456@192.168.31.152:3306/fastapi_db3",
    },
    "apps": {
        "models": {
            "models": ["model21", "aerich.models"],  # 模型模块和 Aerich 迁移模型
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

register_tortoise(app,
                  config=TORTOISE_ORM,
                  generate_schemas=True,  # 开发环境自动生成表结构
                  add_exception_handlers=True  # 添加默认异常处理
                  )


@app.get('/create')
async def create():
    stu = await create_student('孙权', 18, 'sunquan@163.com')
    return stu

# 生成一个传递参数创建学生数据的路由


@app.post('/create2')
async def create2(name: str, age: int = None, email: str = None):
    stu = await create_student(name, age, email)
    return stu

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main21:app', host='127.0.0.1', port=8000, reload=True)
