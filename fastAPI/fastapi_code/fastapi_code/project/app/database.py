from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


def register_db(app: FastAPI, config: dict, generate_schemas: bool = True, add_exception_handlers: bool = True):
    register_tortoise(app,
                      config=config,
                      generate_schemas=True,  # 开发环境自动生成表结构
                      add_exception_handlers=True  # 添加默认异常处理
                      )
