from dataclasses import dataclass
from typing import Optional

from ..shared.vo import UserID

@dataclass
class User:
    '''
    用户实体类
    '''
    id: Optional[UserID]
    username: str
    password: str

    def __post_init__(self):
        if not self.username:   
            raise ValueError("用户名不能为空")
        if not self.password:
            raise ValueError("密码不能为空")
    
    def verify_password(self, password: str) -> bool:
        '''
        验证密码是否正确
        '''
        return self.password == password
    
    def change_password(self, new_password: str) ->None:
        '''
        修改密码
        '''
        if not new_password:
            raise ValueError("密码不能为空")
        self.password = new_password