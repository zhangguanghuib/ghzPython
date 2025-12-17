'''
共享值对象（Value Object）定义模块
'''
from dataclasses import dataclass
 
@dataclass(frozen=True)   # dataclass会自动实现__init__()和__eq__()方法 frozen=True使实例不可变
class UserID:
    '''
    用户ID值对象
    '''
    value: int

    def __post_init__(self):
        '''
        初始化检查
        '''
        if self.value < 0:
            raise ValueError('用户ID不能小于0')