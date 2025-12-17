'''
用户仓储接口
'''
from abc import ABC, abstractmethod
from typing import Optional

from .entity import User
from ..shared.vo import UserID

class UserRepository(ABC):

    @abstractmethod
    async def save(self, user:User) -> User:
        '''保存用户'''
        pass

    @abstractmethod
    async def find_by_id(self, user_id:UserID) -> Optional[User]:
        '''通过ID查找用户'''
        pass

    @abstractmethod
    async def find_by_username(self, username:str) -> Optional[User]:
        '''通过用户名查找用户'''
        pass

    @abstractmethod
    async def exists_by_username(self, username:str) -> bool:
        '''检查用户名是否存在'''
        pass
    @abstractmethod
    async def delete(self, user_id:UserID) -> bool:
        '''删除用户'''
        pass    
    @abstractmethod
    async def find_all(self) -> list[User]:
        '''查找所有用户'''
        pass