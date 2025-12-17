# 关联关系建立1对多
from tortoise import fields, models, Tortoise, run_async


class Student(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    profile = fields.OneToOneField(
        "models.StudentProfile", on_delete=fields.CASCADE, related_name="student")


'''
学生表
id name   profile_id  score_ids            score_id1   score_id2 ...
1  张三     1           1-2-3-5-8-6-7         1          2
2  李四     2

成绩表
id score stu_id
1  90     1
2  80     1
3  70     1
4  60     2
5  50     1
'''


class StudentProfile(models.Model):
    id = fields.IntField(pk=True)
    address = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=20)


class Grade(models.Model):
    id = fields.IntField(pk=True)
    score = fields.FloatField()
    student = fields.ForeignKeyField(
        "models.Student", related_name="grades", on_delete=fields.CASCADE)


async def init():
    await Tortoise.init(
        db_url="mysql://root:123456@192.168.31.152:3306/fastapi_db4",
        modules={"models": ["model23"]}
    )
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())
