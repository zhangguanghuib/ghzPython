# 查询参数Query
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items1")
def read_item1(item_id: str = Query(123)):
    return {"item_id": item_id}


@app.get("/items2")
def read_item2(item_id: str = Query(...)):
    '''必须传递'''
    return {"item_id": item_id}


@app.get("/items3")
def read_item3(item_id: str = Query(..., min_length=3, max_length=6)):
    '''必须传递,限制内容长度'''
    return {"item_id": item_id}


@app.get("/items4")
def read_item4(item_id: int = Query(..., gt=0, lt=100)):
    '''必须传递,限制内容大小'''
    return {"item_id": item_id}


@app.get("/items5")
def read_item5(item_id: int = Query(..., alias='id')):
    '''必须传递,修改名称'''
    return {"item_id": item_id}


@app.get("/items6")
def read_item6(item_id: int = Query(..., description="这个字段是来筛选产品的ID")):
    '''必须传递,说明'''
    return {"item_id": item_id}


@app.get("/items7")
def read_item7(item_id: int = Query(..., deprecated=True)):
    '''必须传递,被抛弃了'''
    return {"item_id": item_id}


@app.get("/items8")
def read_item8(item_id: str = Query(..., regex='^a\d{2}$')):
    '''必须传递,通过正则匹配，pattern,regex'''
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main07:app', host="127.0.0.1", port=8000, reload=True)
