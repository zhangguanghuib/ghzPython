from tortoise.models import Model
from tortoise.fields import CharField, TextField, IntField, BooleanField, DatetimeField


class User(Model):
    id = CharField(max_length=36, pk=True)
    name = CharField(max_length=64, unique=True)
    email = CharField(max_length=255)
    is_active = BooleanField(default=True)
    age = IntField(default=0)
    # 创建时间
    created_at = DatetimeField(auto_now_add=True)

    class Meta:
        table = 't_user'  # table/view
        unique_together = ('name', 'email')  # 联合唯一
        ordering = ['-created_at']  # -降序 默认升序
        # 创建索引
        indexes = [
            'email',
        ]


'''
aerich init -t main20.TORTOISE_ORM   # 初始化
aerich init-db  # 创建迁移脚本

aerich migrate --name "注释"    # 迁移
aerich upgrade  # 同步迁移
'''
