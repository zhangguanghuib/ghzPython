# APIRouter的使用
from fastapi import FastAPI, APIRouter
app = FastAPI()

# main_router = APIRouter(tags=['主应用'], prefix='/main')
# user_router = APIRouter(tags=['用户应用'], prefix='/user')
# item_router = APIRouter(tags=['商品应用'])


v1_router = APIRouter(prefix='/api/v1')
v2_router = APIRouter(prefix='/api/v2')
user_router = APIRouter(tags=['用户应用'], prefix='/user')
item_router = APIRouter(tags=['商品应用'])


# @main_router.get('/info')
# async def get_info1():
#     return 'main:内容成功获取!'


@user_router.get('/info')
async def get_info2():
    return 'user:内容成功获取!'


@user_router.get('/create')
async def create_info2():
    return 'user:内容成功获取!'


@item_router.get('/info')
async def get_info3():
    return 'item:内容成功获取!'

# app.include_router(main_router)
# app.include_router(user_router)
# app.include_router(item_router, prefix='/item')

v1_router.include_router(user_router)
v1_router.include_router(item_router)

app.include_router(v1_router)
app.include_router(v2_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main28:app', host="127.0.0.1", port=8000, reload=True)
