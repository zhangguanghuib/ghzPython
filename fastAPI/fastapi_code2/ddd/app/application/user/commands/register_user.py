from dataclasses import dataclass

from app.domain.user.repository import UserRepository
from app.domain.user.entity import User
from app.application.common.exception import DuplicateError,ValidationError

@dataclass
class RegisterUserCommand:
    '''
    用户注册命令
    '''
    username: str
    password: str

@dataclass
class RegisterUserResult:
    '''
    用户注册结果
    '''
    user_id: int
    username: str

class RegisterUserHandler:
    '''
    用户注册处理器
    '''
    def __init__(self,user_repository:UserRepository):
        self.user_repository = user_repository
    
    async def handle(self, command:RegisterUserCommand) -> RegisterUserResult:
        '''
        处理用户注册
        '''
        # 验证用户名
        if not command.username or not command.username.strip():
            raise ValidationError("用户名不能为空")
        # 验证密码
        if not command.password or not command.password.strip():
            raise ValidationError("密码不能为空")
        
        # 检查用户名是否已存在
        if await self.user_repository.exists_by_username(command.username):
            raise DuplicateError("用户名已存在")

        # 创建用户实体
        user = User(
            id = None,
            username = command.username,
            password = command.password
        )
        # 保存用户
        saved_user = await self.user_repository.save(user)

        return RegisterUserResult(
            user_id = saved_user.id.value if saved_user.id else 0,
            username = saved_user.username
        )