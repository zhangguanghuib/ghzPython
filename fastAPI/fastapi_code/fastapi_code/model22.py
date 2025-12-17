# 关联关系建立1对1
from tortoise import fields, models, Tortoise, run_async


class Student(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    profile = fields.OneToOneField(
        "models.StudentProfile", on_delete=fields.CASCADE, related_name="student")


'''
id name   profile_id
1  张三     1
2  李四     2

id  address  phone      
1    上海     123456        
2    北京     789456       
'''


class StudentProfile(models.Model):
    id = fields.IntField(pk=True)
    address = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=20)


async def init():
    await Tortoise.init(
        db_url="mysql://root:123456@192.168.31.152:3306/fastapi_db4",
        modules={"models": ["model22"]}
    )
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())
