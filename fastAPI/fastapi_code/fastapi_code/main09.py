# 路径参数Path
from typing import Annotated
from pydantic import BeforeValidator
from enum import Enum
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items1/{item_id}")
def read_item1(item_id: int):
    return {'item_id': item_id}


@app.get('/items2/{item_id}')
def read_item2(item_id: int = Path(...)):
    return {'item_id': item_id}


@app.get('/items3/{item_id}')
def read_item3(item_id: int = Path(..., lt=100, gt=18)):
    return {'item_id': item_id}


@app.get('/items4/{item_id}')
def read_item4(item_id: str = Path(..., pattern=r'^a\d{2}$')):
    '''regex或者pattern'''
    return {'item_id': item_id}


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/items5/{model}')
def read_item5(model: ModelName):
    return {'model': model}


def validate(value):
    if not value.startswith('P-'):
        raise ValueError('必须以P-开头')
    return value


# 创建带验证的类型别名
Item = Annotated[str, BeforeValidator(validate)]


@app.get('/items6/{item_id}')
def read_item6(item_id: Item):
    return {'item_id': item_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main09:app', host='127.0.0.1', port=8000, reload=True)
