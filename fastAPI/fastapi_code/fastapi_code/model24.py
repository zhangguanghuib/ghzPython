# 关联关系建立多对多
from tortoise import fields, models, Tortoise, run_async


'''
学生表
id name   profile_id     
1  张三     1             
2  李四     2

成绩表
id score stu_id
1  90     1
2  80     1
3  70     1
4  60     2
5  50     1

课程表
id name       
1  python     
2  java
3  c++

学生课程表
stu_id  course_id
1        1
1        2
2        3
'''


class Student(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    profile = fields.OneToOneField(
        "models.StudentProfile", on_delete=fields.CASCADE, related_name="student", null=True)


class StudentProfile(models.Model):
    id = fields.IntField(pk=True)
    address = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=20)


class Grade(models.Model):
    id = fields.IntField(pk=True)
    score = fields.FloatField()
    student = fields.ForeignKeyField(
        "models.Student", related_name="grades", on_delete=fields.CASCADE)


class Course(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    # students = fields.ManyToManyField(
    #     "models.Student", related_name="courses", through="studentcourse")


class StudentCourse(models.Model):
    students = fields.ForeignKeyField("models.Student", related_name="courses")
    courses = fields.ForeignKeyField("models.Course", related_name="students")

    class Meta:
        unique_together = ("students", "courses")


async def init():
    await Tortoise.init(
        db_url="mysql://root:123456@192.168.31.152:3306/fastapi_db4",
        modules={"models": ["model24"]}
    )
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())
