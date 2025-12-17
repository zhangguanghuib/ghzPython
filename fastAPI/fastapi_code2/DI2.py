from fastapi import FastAPI,Depends, HTTPException, status,Header, Query

app = FastAPI()
# 依赖函数：检查用户权限
def check_user_permission(token: str = Header(...)):
    if token != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )
    return {"user": "admin"}

# 路径级依赖注入
@app.get("/admin/", dependencies=[Depends(check_user_permission)])
async def admin_dashboard():
    return {"message": "Welcome to Admin Dashboard"}


# 依赖函数：获取分页参数
def get_pagination_params(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    return {"page": page, "page_size": page_size}

# 路径级依赖注入
@app.get("/items/")
async def list_items(pagination: dict = Depends(get_pagination_params)):
    return {
        "items": ["item1", "item2", "item3"],
        "current_page": pagination["page"],
        "page_size": pagination["page_size"]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI2:app",host='127.0.0.1',port=8000,reload=True)