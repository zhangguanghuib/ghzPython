from fastapi import APIRouter

item_router = APIRouter(tags=['商品应用'], prefix='/item')


@item_router.get('/info')
async def get_info():
    return '商品信息'
