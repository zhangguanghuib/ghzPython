'''
ORM模型

'''
from tortoise.models import Model
from tortoise import fields

class UserORM(Model):
    '''
    用户表
    '''
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'users'