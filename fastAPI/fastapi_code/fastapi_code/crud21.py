from model21 import Student
from tortoise import Tortoise, run_async


async def create_student(name: str, age: int = None, email: str = None) -> Student:
    try:
        stu = await Student.create(name=name, age=age, email=email)
        return stu
    except Exception as e:
        print("创建失败！")


async def update_student(stu_id: int, name: str = None, age: int = None, email: str = None) -> Student:
    stu = await Student.get(id=stu_id)
    # 判断用户传递了哪个数据，如果没有传递，就不更新
    if name:
        stu.name = name
    if age is not None:
        stu.age = age
    if email is not None:
        stu.email = email
    # 保存
    await stu.save()
    return stu


async def delete_student(stu_id: int) -> None:
    stu = await Student.get(id=stu_id)
    await stu.delete()

# 单条数据


async def get_student(stu_id: int) -> Student:
    stu = await Student.get(id=stu_id)
    return stu
# 多条数据


async def get_students(name: str) -> list[Student]:
    '''
    完成匹配
    '''
    stus = await Student.filter(name=name)
    return stus


async def get_students2(name: str) -> list[Student]:
    '''
    模糊查询
    '''
    stus = await Student.filter(name__contains=name)
    return stus


async def get_students3() -> list[Student]:
    '''
    获取所有数据
    '''
    stus = await Student.all()
    return stus

# 编写查询名字为曹操的年龄等于20的记录


async def get_students4() -> list[Student]:
    stus = await Student.filter(name="曹操", age=20)
    return stus

    # 1. 直接测试脚本
    # 2. 直接应用到接口


async def init():
    await Tortoise.init(
        db_url="mysql://root:123456@192.168.31.152:3306/fastapi_db3",
        modules={"models": ["model21"]}
    )
    await Tortoise.generate_schemas()


async def main():
    await init()
    # stu1 = await create_student(name="曹操")
    # print(f"创建成功 ID:{stu1.id}  Name:{stu1.name} Email:{stu1.email}")
    # stu2 = await create_student(name="刘备", age=30)
    # print(f"创建成功 ID:{stu2.id}  Name:{stu2.name} Email:{stu2.email}")
    # stu3 = await create_student(name="张飞", age=30, email="zf@163.com")
    # print(f"创建成功 ID:{stu3.id}  Name:{stu3.name} Email:{stu3.email}")
    # stu4 = await create_student(name="关羽", age=30, email="zf@163.com")
    # print(f"创建成功 ID:{stu4.id}  Name:{stu4.name} Email:{stu4.email}")

    # await update_student(stu_id=3, age=36)
    # await update_student(stu_id=1, email="cc@qq.com", age=40)
    # await delete_student(stu_id=9)

    stu = await get_student(3)
    print(stu)
    stus1 = await get_students("刘备")
    print(stus1)
    stus2 = await get_students2("曹")
    print(stus2)
    stus3 = await get_students3()
    print(stus3)

if __name__ == '__main__':
    run_async(main())
