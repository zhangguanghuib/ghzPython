'''
实体与ORM映射器
'''
from ..database.orm_models import UserORM
from app.domain.user.entity import User
from app.domain.shared.vo import UserID

class UserMapper:
    '''
    用户映射器
    '''
    @staticmethod
    def to_entity(orm_model: UserORM) -> User:
        '''
        将ORM对象转换为实体对象
        '''
        return User(
            id = UserID(orm_model.id) if orm_model.id else None,
            username = orm_model.username,
            password = orm_model.password
        )
    @staticmethod
    def to_orm(user: User) -> UserORM:
        '''
        将实体对象转换为ORM对象
        '''
        orm_model = UserORM()
        if user.id:
            orm_model.id = user.id.value
        orm_model.username = user.username
        orm_model.password = user.password
        return orm_model