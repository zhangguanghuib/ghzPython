# Field验证方式
from enum import Enum
from pydantic import field_validator
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    name: str = Field(default='吕布')
    age: int = Field(...)  # 必填


@app.post('/users/')
def create_user(user: User):
    return user


class Product(BaseModel):
    price: float = Field(..., gt=0, le=1000, description='价格')


@app.post('/products/')
def create_product(product: Product):
    return product


class Account(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., pattern=r'^\w{6,}$')


@app.post('/accounts/')
def create_account(account: Account):
    return account


class Item(BaseModel):
    name: str = Field(..., title='商品名称',
                      description="必填，长度不要超过50字符", example='手机')


@app.post('/items/')
def create_item(item: Item):
    return item


class User2(BaseModel):
    email: str

    @field_validator('email')
    def email_validator(cls, v):
        if '@' not in v:
            raise ValueError('邮箱格式错误')
        return v


@app.post('/users2/')
def create_user2(user: User2):
    return user


class Order(BaseModel):
    items: list = Field(..., min_items=1)
    address: str = Field(..., description="配送地址")


@app.post('/orders/')
def create_order(order: Order):
    return order


class Status(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class Task(BaseModel):
    status: Status = Field(default=Status.ACTIVE)


@app.post('/tasks/')
def get_task():
    return Task()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main10:app', host='127.0.0.1', port=8000, reload=True)
