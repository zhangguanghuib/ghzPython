from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header

app = FastAPI()

# 依赖函数：检查用户权限
def check_auth(token: str = Header(...)):
    if token != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"user": "admin"}

router = APIRouter(dependencies=[Depends(check_auth)])  # 路由级依赖
# 路由1：受保护的路由
@router.get("/admin/dashboard")
async def admin_dashboard():
    return {"message": "Welcome to Admin Dashboard"}

# 路由2：受保护的路由
@router.get("/admin/users")
async def list_users():
    return {"users": ["user1", "user2"]}

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI3:app",host='127.0.0.1',port=8000,reload=True)