from fastapi import FastAPI, Depends, Request



# 依赖函数：记录请求信息
async def log_request(request: Request):
    print(f"Request received: {request.method} {request.url}")
    return {"logged": True}

app = FastAPI(dependencies=[Depends(log_request)])  # 全局级依赖
# 所有路由都会自动记录请求
@app.get("/items/")
async def list_items():
    return {"items": ["item1", "item2"]}

@app.post("/items/")
async def create_item():
    return {"message": "Item created"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI4:app",host='127.0.0.1',port=8000,reload=True)