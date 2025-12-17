'''
认证和用户路由
'''

from pydantic import BaseModel
from fastapi import APIRouter, Depends,status, HTTPException

from app.application.common.exception import DomainException
from app.interface.dependency import get_register_user_handler,get_login_user_handler
from app.application.user.commands.register_user import RegisterUserCommand, RegisterUserHandler
from app.application.user.commands.login_user import LoginUserCommand,LoginUserHandler

router = APIRouter(prefix="/auth", tags=["认证"])

class RegisterRequest(BaseModel):
    '''
    注册请求
    '''
    username:str
    password:str
class RegisterResponse(BaseModel):
    '''
    注册响应
    '''
    user_id:int
    username:str
    message:str

class LoginRequest(BaseModel):
    '''
    登录请求
    '''
    username:str
    password:str
class LoginResponse(BaseModel):
    '''
    登录响应
    '''
    user_id:int
    username:str
    message:str


@router.post('/register',response_model=RegisterResponse,status_code=status.HTTP_201_CREATED)
async def register_user(
    request:RegisterRequest,
    handler:RegisterUserHandler = Depends(get_register_user_handler)
    ):
    '''
    用户注册接口
    '''
    try:
        command = RegisterUserCommand(
            username=request.username,
            password=request.password
            )
        result = await handler.handle(command)
        return RegisterResponse(
            user_id=result.user_id,
            username=result.username,
            message="用户注册成功"
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='服务器内部错误')
    
@router.post('/login',response_model=LoginResponse,status_code=status.HTTP_200_OK)
async def login_user(
    request:LoginRequest,
    handler:LoginUserHandler = Depends(get_login_user_handler)
    ):
    '''
    用户登录接口
    '''
    try:
        command = LoginUserCommand(
            username=request.username,
            password=request.password
            )
        result = await handler.handle(command)
        return LoginResponse(
            user_id=result.user_id,
            username=result.username,
            message="用户登录成功"
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='服务器内部错误')