'''
依赖注入模块
'''
from fastapi import Depends

from app.domain.user.repository import UserRepository
from app.infrastructure.repository.user_impl import UserRepositoryImpl
from app.application.user.commands.register_user import RegisterUserHandler
from app.application.user.commands.login_user import LoginUserHandler
from app.application.user.queries.get_orders import GetOrdersHandler


def get_user_repository() -> UserRepository:
    '''
    获取用户仓储
    '''
    return UserRepositoryImpl()

def get_register_user_handler(
        user_repository:UserRepository = Depends(get_user_repository)) -> RegisterUserHandler:
    '''
    获取注册用户处理器
    '''
    return RegisterUserHandler(user_repository)

def get_login_user_handler(
        user_repository:UserRepository = Depends(get_user_repository)) -> LoginUserHandler:
    '''
    获取登录用户处理器
    '''
    return LoginUserHandler(user_repository)

def get_get_orders_handler() -> GetOrdersHandler:
    '''
    获取订单处理器
    '''
    return GetOrdersHandler()