from dataclasses import dataclass
from functools import total_ordering
from typing import Optional,List



@dataclass
class GetOrdersQuery:
    '''
    获取用户订单查询
    '''
    user_id: int
    limit:Optional[int] =10
    offset:Optional[int] =0

@dataclass
class OrderDTO:
    '''
    订单数据传输对象
    '''
    id:int
    order_number:str
    total_amount:float
    status:str
    created_at:str
    updated_at:str

@dataclass
class GetOrdersResult:
    ''''
    获取用户订单结果
    '''
    orders:List[OrderDTO]
    total:int

class GetOrdersHandler:
    '''
    获取订单查询处理器
    '''
    def __init__(self):
        # 这里应该注入订单仓储，为了简化，我们使用模拟数据
        pass
    async def handle(self, query:GetOrdersQuery) -> GetOrdersResult:
        '''
        处理获取用户订单查询

        '''
        # 验证输入的参数
        if query.user_id <= 0:
            raise ValueError('用户ID必须大于0')
        if query.limit <= 0 or query.limit > 100:
            raise ValueError('限制数量必须大于0且小于100')
        if query.offset < 0:
            raise ValueError('偏移量不能为负数')
        
        # 模拟订单数据
        orders = [
            OrderDTO(id=1, order_number='ORD-001', total_amount=99.99, status='待处理', created_at='2030-05-01 10:00:00', updated_at='2023-05-01 10:00:00'),
            OrderDTO(id=2, order_number='ORD-002', total_amount=149.99, status='已发货', created_at='2030-05-02 11:00:00', updated_at='2023-05-02 11:00:00'),
            OrderDTO(id=3, order_number='ORD-003', total_amount=199.99, status='已完成', created_at='2030-05-03 12:00:00', updated_at='2023-05-03 12:00:00'),
        ]
        # 应用分页
        start = query.offset or 0
        end = start + (query.limit or 2)
        paginated_orders = orders[start:end]
        
        return GetOrdersResult(orders=paginated_orders, total=len(orders))
