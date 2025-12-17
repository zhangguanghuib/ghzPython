from tortoise import fields, models


class Student(models.Model):
    """
    学生模型，包含基本信息。
    用于演示单表的增删改查操作。
    """
    id = fields.IntField(pk=True, description="学生ID，主键")
    name = fields.CharField(max_length=50, description="学生姓名")
    age = fields.IntField(null=True, description="学生年龄，可为空")
    email = fields.CharField(max_length=100, unique=True,
                             null=True, description="学生邮箱，唯一")

    class Meta:
        table = "students"

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Email: {self.email}"
