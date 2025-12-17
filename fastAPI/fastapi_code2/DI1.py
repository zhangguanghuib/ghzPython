from fastapi import FastAPI,Depends

app = FastAPI()

# 简单依赖函数
def get_query_param(q: str = "default"):
    return q.upper()

# 使用依赖的路由
@app.get("/items1/")
async def read_items1(query: str = Depends(get_query_param)):
    return {"query": query}


# 定义一个依赖函数
def common_params(q: str = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items2/")
async def read_items2(params: dict = Depends(common_params)):
    return params


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI1:app",host='127.0.0.1',port=8000,reload=True)