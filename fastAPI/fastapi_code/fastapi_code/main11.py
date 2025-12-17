# 表单数据
# 安装pip install python-multipart==0.0.20
from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


@app.post('/login1')
def login1(username: str = Form(...), password: str = Form(...)):
    return {'username': username, 'password': password}


class User1(BaseModel):
    username: str
    password: str


@app.post('/login2')
def login2(user: Annotated[User1, Form()]):
    return user


class User2(BaseModel):
    username: str = Form(...)
    password: str = Form(...)


@app.post('/login3')
def login3(user: Annotated[User2, Form()]):
    return user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main11:app', host='127.0.0.1', port=8000, reload=True)
