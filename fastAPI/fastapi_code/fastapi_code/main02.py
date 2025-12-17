from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    # 这里可以添加查询数据库等操作来获取用户信息
    return {"user_id": user_id, "name": "User Name", "email": "user@example.com"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
