'''
订单路由
'''

from typing import List, Optional

from pydantic import BaseModel
from fastapi import APIRouter, Depends,status, HTTPException,Query

from app.interface.dependency import get_get_orders_handler
from app.application.common.exception import DomainException
from app.application.user.queries.get_orders import GetOrdersQuery,GetOrdersHandler

router = APIRouter(prefix="/orders", tags=["订单"])

class OrderResponse(BaseModel):
    '''
    订单响应
    '''
    id:int
    order_number:str
    total_amount:float
    status:str
    created_at:str
    updated_at:str

class GetOrdersResponse(BaseModel):
    '''
    获取订单响应
    '''
    orders:List[OrderResponse]
    total:int
    limit:int
    offset:int

@router.get('/',response_model=GetOrdersResponse)
async def get_orders(
    user_id:int = Query(...,description="用户ID"),
    limit:Optional[int] =Query(10,ge=1,le=100,description="每页数量"),
    offset:Optional[int] =Query(0,ge=0,description="偏移量"),
    handler:GetOrdersHandler = Depends(get_get_orders_handler)
):
    """
    获取用户订单
    """
    try:
        query = GetOrdersQuery(
            user_id=user_id,
            limit=limit,
            offset=offset
        )
        rs = await handler.handle(query)
        return GetOrdersResponse(
            orders= [
                OrderResponse(
                    id=order.id,
                    order_number=order.order_number,
                    total_amount=order.total_amount,
                    status=order.status,
                    created_at=order.created_at,
                    updated_at=order.updated_at
                ) 
                for order in rs.orders],
            total=rs.total,
            limit=limit or 10,
            offset=offset or 0
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='服务器内部错误')