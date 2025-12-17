from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=255)
    age = fields.IntField(default=1)
    create_at = fields.DatetimeField(auto_now_add=True)
